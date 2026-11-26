"""Generate the profile's animated banner. Run with Python 3 and Pillow installed."""

from math import hypot, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT, SCALE = 1200, 320, 2
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
BG = "#0d1525"
CYAN = "#67dce8"
PURPLE = "#a69bdf"
LINES = (
    "AdaptiveVec / vector search in C++",
    "AdaMem-FDE / numerical methods in PyTorch",
    "SONICBULK / desktop tools in Python",
)
NODES = ((836, 78), (940, 54), (1013, 129), (1135, 77),
         (850, 210), (956, 263), (1066, 237), (1146, 174))
EDGES = ((0, 1), (0, 2), (0, 4), (1, 2), (2, 3), (2, 4),
         (2, 6), (2, 7), (3, 7), (4, 5), (4, 6), (5, 6), (6, 7))


def font(size, *, mono=False, bold=False):
    family = "DejaVuSansMono" if mono else "DejaVuSans"
    suffix = "-Bold" if bold else ""
    return ImageFont.truetype(str(FONT_DIR / f"{family}{suffix}.ttf"), size * SCALE)


def line(draw, points, fill, width=1):
    draw.line([(round(x * SCALE), round(y * SCALE)) for x, y in points],
              fill=fill, width=width * SCALE)


def circle(draw, x, y, radius, fill=None, outline=None, width=1):
    draw.ellipse(tuple(round(v * SCALE) for v in
                       (x - radius, y - radius, x + radius, y + radius)),
                 fill=fill, outline=outline, width=width * SCALE)


def text(draw, xy, value, face, color):
    draw.text((xy[0] * SCALE, xy[1] * SCALE), value, font=face, fill=color)


def terminal_text(seconds):
    """Hold, erase, and type the next project; the loop starts fully readable."""
    index = int(seconds // 5) % len(LINES)
    phase = seconds % 5
    current, following = LINES[index], LINES[(index + 1) % len(LINES)]
    if phase < 2:
        return current
    if phase < 2.6:
        return current[:round(len(current) * (2.6 - phase) / 0.6)]
    if phase < 4:
        return following[:round(len(following) * (phase - 2.6) / 1.4)]
    return following


def make_background():
    canvas = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), BG)
    draw = ImageDraw.Draw(canvas)
    for x in range(0, WIDTH, 32):
        line(draw, ((x, 0), (x, HEIGHT)), "#131e30")
    for y in range(0, HEIGHT, 32):
        line(draw, ((0, y), (WIDTH, y)), "#131e30")
    line(draw, ((48, 44), (78, 44)), CYAN, 3)
    text(draw, (92, 35), "SYSTEMS / NUMERICAL COMPUTING / APPLIED AI",
         font(12, mono=True), "#9cacc3")
    text(draw, (44, 82), "Aradhya Shinde", font(60, bold=True), "#f0f6fc")
    text(draw, (48, 165), "Computer Engineering student",
         font(20), "#a8bad2")
    draw.rounded_rectangle((48 * SCALE, 229 * SCALE, 754 * SCALE, 282 * SCALE),
                           radius=10 * SCALE, fill="#101e30", outline="#2b4057",
                           width=SCALE)
    text(draw, (65, 244), ">", font(18, mono=True, bold=True), CYAN)
    for a, b in EDGES:
        line(draw, (NODES[a], NODES[b]), "#35465e")
    return canvas


def make_frame(background, seconds):
    canvas = background.copy()
    draw = ImageDraw.Draw(canvas)
    # Moving packets make the graph's connections visibly active.
    for offset, route, color in ((0, (0, 4, 2, 6, 7, 3, 2, 0), CYAN),
                                  (0.45, (1, 2, 4, 5, 6, 2, 1), PURPLE)):
        segments = [(NODES[a], NODES[b]) for a, b in zip(route, route[1:])]
        lengths = [hypot(b[0] - a[0], b[1] - a[1]) for a, b in segments]
        distance = ((seconds / 4 + offset) % 1) * sum(lengths)
        for (a, b), length in zip(segments, lengths):
            if distance <= length:
                fraction = distance / length
                x = a[0] + (b[0] - a[0]) * fraction
                y = a[1] + (b[1] - a[1]) * fraction
                line(draw, (a, (x, y)), color, 2)
                circle(draw, x, y, 5, fill=color)
                break
            distance -= length
    ring = 23 + 6 * sin(seconds * pi)
    circle(draw, 1013, 129, ring, outline="#346476")
    circle(draw, 1013, 129, ring + 9, outline="#234353")
    for index, (x, y) in enumerate(NODES):
        circle(draw, x, y, 6, fill=BG, outline="#8297b1", width=2)
        if index == 2:
            circle(draw, x, y, 7, fill=CYAN)
    value = terminal_text(seconds)
    face = font(18, mono=True)
    text(draw, (94, 244), value, face, "#deedf6")
    if int(seconds * 2) % 2 == 0:
        cursor_x = 94 + draw.textlength(value, font=face) / SCALE + 4
        draw.rectangle((round(cursor_x * SCALE), 245 * SCALE,
                        round((cursor_x + 9) * SCALE), 265 * SCALE), fill=CYAN)
    return canvas.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def main():
    background = make_background()
    frames = [make_frame(background, i / 10) for i in range(150)]
    # One palette keeps text and background colors stable throughout playback.
    palette = frames[0].quantize(colors=128)
    frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE)
              for frame in frames]
    output = ROOT / "assets" / "header.gif"
    output.parent.mkdir(exist_ok=True)
    frames[0].save(output, save_all=True, append_images=frames[1:],
                   duration=100, loop=0, optimize=True, disposal=1)
    print(f"Generated {output}: {len(frames)} frames, {output.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
