<div align="center">

  <!-- Header Banner -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=10,14,24&height=220&section=header&text=Aradhya%20Shinde&fontSize=50&fontColor=ffffff&animation=fadeIn&subtext=Systems%20%26%20Machine%20Learning%20Researcher%20%7C%20High-Performance%20Computing&subfontSize=17&subfontColor=94a3b8" width="100%" />

  <!-- Animated Terminal Typing Headline -->
  <a href="https://github.com/aradhyags7">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2800&pause=1000&color=38BDF8&center=true&vCenter=true&width=780&lines=%3E_Architecting+hardware-accelerated+SIMD+vector+retrieval+(AdaptiveVec);%3E_Continual+neural+memory+without+catastrophic+forgetting+(AdaMem-FDE);%3E_100%25+offline+sovereign+voice+intelligence+(Aegis);%3E_Zero-knowledge+asymmetric+cryptographic+systems+(TwoOfUs);%3E_Offline-first+clinical+cognitive+care+platforms+(Smriti)" alt="Typing Headline" />
  </a>

  <br/>

  <!-- Quick Command Badges -->
  <p align="center">
    <a href="https://aradhyags7.github.io/Portfolio/" target="_blank">
      <img src="https://img.shields.io/badge/Live_3D_Portfolio-07070B?style=for-the-badge&logo=googlechrome&logoColor=38BDF8&labelColor=0d1117" alt="Live Portfolio" />
    </a>
    <a href="https://www.linkedin.com/in/aradhya-shinde-5797b8304" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d1117" alt="LinkedIn" />
    </a>
    <a href="mailto:aradhyashinde2330@gmail.com">
      <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117" alt="Email" />
    </a>
    <a href="https://github.com/aradhyags7">
      <img src="https://img.shields.io/github/followers/aradhyags7?label=Followers&style=for-the-badge&color=238636&labelColor=0d1117" alt="Followers" />
    </a>
  </p>

</div>

---

### 🧠 First Principles & Research Philosophy

> *"Mechanical sympathy and mathematical elegance beat throwing brute-force compute at inefficient algorithms."*

I engineer software at the confluence of **bare-metal silicon efficiency** and **theoretical machine learning**. Rather than treating AI models as high-level black boxes, I design systems from first principles — optimizing CPU cache hierarchies, vectorizing computational kernels directly onto Intel AVX2 SIMD registers, formulating neural architectures that learn continuously without catastrophic forgetting, and deploying sovereign intelligence platforms with zero cloud telemetry.

* ⚡ **Low-Level HPC & SIMD**: Hand-vectorized AVX2 256-bit kernels, CPU cache hierarchy profiling, microsecond-latency beam-search graph traversal.
* 🔬 **Continual Neural Memory**: Mitigating catastrophic representation drift via Feature Distribution Estimation (FDE) and selective episodic replay.
* 🛡️ **Sovereign Local-First AI**: 100% offline edge intelligence — on-device INT8 quantized speech & LLM inference with zero cloud telemetry.
* 🔐 **Verifiable Cryptography**: Zero-knowledge private architectures with Curve25519 asymmetric ECDH and XSalsa20-Poly1305 symmetric ciphers.
* 🩺 **Human Consequence**: Designing offline-first clinical platforms for dementia care and memory preservation in underserved communities.

---

### ⚡ Verified Research & Production Benchmarks

The core systems engineered across my open-source research workspace:

| System | Domain & Architecture | Key Benchmark & Verified Metric | Stack |
| :--- | :--- | :--- | :--- |
| [**AdaptiveVec**](https://github.com/aradhyags7/AdaptiveVec) | Density-aware vector graph proximity index | **`< 0.42 ms`** P99 Latency • **`98.7%`** Recall@10 • **`3.4x`** SIMD Speedup | `C++17` `AVX2 SIMD` `Python` `CMake` |
| [**AdaMem-FDE**](https://github.com/aradhyags7/AdaMem-FDE) | Continual learning neural memory framework | **`89.2%`** Retention across streaming tasks • **`15/15`** Tests Passing | `PyTorch 2.2+` `CUDA` `NumPy` |
| [**Aegis**](https://github.com/aradhyags7/Aegis) | Sovereign local AI desktop assistant | **`< 350 ms`** STT Latency • **`100%`** Offline & Private • Zero Telemetry | `TypeScript` `Faster-Whisper` `Ollama` |
| [**Smriti (स्मृति)**](https://github.com/aradhyags7/Smriti) | Offline-first cognitive care platform | **`87`** Backend & **`323`** Flutter Tests • Dialect-adapted clinical care | `Flutter` `Dart` `FastAPI` `SQLite` |
| [**TwoOfUs**](https://github.com/aradhyags7/TwoOfUs) | Zero-knowledge E2EE private space | **`35/35`** Cryptographic Tests • Curve25519 ECDH • XSalsa20-Poly1305 | `Flutter` `FastAPI` `PostgreSQL` |
| [**CosmoLens**](https://github.com/aradhyags7/CosmoLens) | Deep sky celestial & satellite visualization | **`10,000+`** Orbital objects tracked • SGP4 propagation • Ephemeris | `Python` `SGP4` `TLE` `NumPy` |

---

### 🔬 Silicon & Mathematical Execution

```cpp
// [AdaptiveVec] 256-bit Intel AVX2 SIMD Euclidean distance kernel
inline float euclidean_distance_avx2(const float* a, const float* b, size_t dim) {
    __m256 v_sum = _mm256_setzero_ps();
    for (size_t i = 0; i < dim; i += 8) {
        __m256 va = _mm256_loadu_ps(a + i);
        __m256 vb = _mm256_loadu_ps(b + i);
        __m256 v_diff = _mm256_sub_ps(va, vb);
        v_sum = _mm256_fmadd_ps(v_diff, v_diff, v_sum);
    }
    return horizontal_add(v_sum); // < 0.42ms p99 retrieval at 98.7% Recall@10
}
```

---

### 🛠️ Technical Stack & Arsenal

<div align="center">
  <img src="https://skillicons.dev/icons?i=cpp,python,pytorch,dart,flutter,ts,react,fastapi,postgres,mongodb,sqlite,redis,git,docker,linux,vscode" />
</div>

<br/>

| Tier | Technologies, Frameworks & Libraries |
| :--- | :--- |
| **Low-Level & HPC** | `C++ (C++17 / AVX2 SIMD)` • `Intel Intrinsics` • `Cache Hierarchy Profiling` • `CMake` |
| **Machine Learning & AI** | `PyTorch 2.2+` • `Vector Retrieval (ANN / HNSW Graphs)` • `Ollama` • `Faster-Whisper` • `NumPy` • `SciPy` |
| **Cross-Platform & Backends**| `Flutter` • `Dart` • `React 19` • `FastAPI (Python)` • `Node.js` • `Three.js WebGL` • `TailwindCSS` |
| **Databases & Telemetry** | `PostgreSQL` • `SQLite (Offline-First)` • `Redis` • `MongoDB` |
| **Tooling & Infrastructure** | `Git` • `GitHub Actions CI/CD` • `Docker` • `Linux (Ubuntu / Arch)` • `Postman` • `VS Code` |

---

### 🚀 Flagship Project Showcases

<table>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">⚡ <a href="https://github.com/aradhyags7/AdaptiveVec">AdaptiveVec</a></h3>
      <p align="center">
        <img src="https://img.shields.io/badge/C%2B%2B17-AVX2%20SIMD-00599C?style=flat-square&logo=c%2B%2B" />
        <img src="https://img.shields.io/badge/Recall%4010-98.7%25-brightgreen?style=flat-square" />
        <img src="https://img.shields.io/badge/Latency-%3C0.42ms-blueviolet?style=flat-square" />
      </p>
      <p>A density- and dimension-aware proximity graph index engineered for resource-constrained vector retrieval. Features hand-vectorized AVX2 kernels providing 3.4x throughput acceleration over baseline scalar algorithms.</p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🧠 <a href="https://github.com/aradhyags7/AdaMem-FDE">AdaMem-FDE</a></h3>
      <p align="center">
        <img src="https://img.shields.io/badge/PyTorch-2.2+-ee4c2c?style=flat-square&logo=pytorch" />
        <img src="https://img.shields.io/badge/Memory_Retention-89.2%25-brightgreen?style=flat-square" />
        <img src="https://img.shields.io/badge/Tests-15%2F15_Passing-blue?style=flat-square" />
      </p>
      <p>Deep continual learning foundation framework mitigating catastrophic forgetting through dynamic feature distribution estimation (FDE) and selective episodic replay buffers for non-stationary streaming distributions.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🛡️ <a href="https://github.com/aradhyags7/Aegis">Aegis</a></h3>
      <p align="center">
        <img src="https://img.shields.io/badge/Offline-100%25_Local-black?style=flat-square" />
        <img src="https://img.shields.io/badge/STT-%3C350ms-blueviolet?style=flat-square" />
        <img src="https://img.shields.io/badge/Ollama-Llama_3-3178C6?style=flat-square" />
      </p>
      <p>A privacy-first local AI desktop assistant inspired by J.A.R.V.I.S. Runs real-time speech recognition and LLM inference entirely on localhost with zero cloud telemetry and zero external API dependencies.</p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🩺 <a href="https://github.com/aradhyags7/Smriti">Smriti (स्मृति)</a></h3>
      <p align="center">
        <img src="https://img.shields.io/badge/Tests-410_Passing-brightgreen?style=flat-square" />
        <img src="https://img.shields.io/badge/Flutter-Cross--Platform-02569B?style=flat-square&logo=flutter" />
        <img src="https://img.shields.io/badge/Healthcare-Offline--First-teal?style=flat-square" />
      </p>
      <p>Offline-first, AI-assisted cognitive care and reminiscence therapy platform for elderly individuals with mild cognitive impairment & early dementia, featuring localized dialect voice prompts and caregiver metrics.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🔐 <a href="https://github.com/aradhyags7/TwoOfUs">TwoOfUs</a></h3>
      <p align="center">
        <img src="https://img.shields.io/badge/Crypto-Curve25519-teal?style=flat-square" />
        <img src="https://img.shields.io/badge/Cipher-XSalsa20-orange?style=flat-square" />
        <img src="https://img.shields.io/badge/Tests-35%2F35_Passing-brightgreen?style=flat-square" />
      </p>
      <p>Intimate zero-knowledge private sanctuary for couples. Built with Curve25519 ECDH key agreement, XSalsa20-Poly1305 symmetric encryption, out-of-band safety numbers, and multi-method 2FA.</p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🌌 <a href="https://github.com/aradhyags7/CosmoLens">CosmoLens</a></h3>
      <p align="center">
        <img src="https://img.shields.io/badge/Ephemeris-SGP4-purple?style=flat-square" />
        <img src="https://img.shields.io/badge/Tracking-10%2C000%2B_Objects-blue?style=flat-square" />
        <img src="https://img.shields.io/badge/Python-Astronomy-3776AB?style=flat-square&logo=python" />
      </p>
      <p>Interactive deep-sky astronomy and real-time orbital satellite pass tracking system calculating high-precision celestial ephemeris, overhead visibility passes, and interactive orbital ground tracks.</p>
    </td>
  </tr>
</table>

---

### 📬 Connect & Collaborate

<p align="center">
  <a href="https://aradhyags7.github.io/Portfolio/" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-aradhyags7.github.io-FF4D5A?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" />
  </a>
  &nbsp;
  <a href="https://www.linkedin.com/in/aradhya-shinde-5797b8304" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Aradhya_Shinde-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="mailto:aradhyashinde2330@gmail.com">
    <img src="https://img.shields.io/badge/Email-aradhyashinde2330%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  &nbsp;
  <a href="https://github.com/aradhyags7">
    <img src="https://img.shields.io/badge/GitHub-aradhyags7-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

<!-- Footer Wave Decoration -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=10,14,24&height=100&section=footer" width="100%" />
</div>
