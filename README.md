# Ronald Rex C H

**B.E. Electronics & Communication Engineering**  
*Embedded Systems • Microcontroller Firmware • Edge AI & TinyML • Sensor Telemetry • Verification & Simulation*

[![GitHub](https://img.shields.io/badge/GitHub-RONALD--REX--7-181717?style=flat&logo=github)](https://github.com/RONALD-REX-7)
[![Projects Portfolio](https://img.shields.io/badge/GitHub_Projects-3_Public_Boards-238636?style=flat&logo=github)](https://github.com/RONALD-REX-7?tab=projects)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ron--rex-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/ron-rex)
[![Credly](https://img.shields.io/badge/Credly-ronaldrex-FF6B00?style=flat&logo=credly&logoColor=white)](https://www.credly.com/users/ronaldrex)
[![AWS Skill Builder](https://img.shields.io/badge/AWS-Skill_Profile-232F3E?style=flat&logo=amazon-aws)](https://skillsprofile.skillbuilder.aws/user/ron)
[![SkillRack](https://img.shields.io/badge/SkillRack-540874-blue?style=flat)](https://www.skillrack.com/profile/540874/)

---

## About Me

I am an Electronics and Communication Engineering undergraduate at S.A. Engineering College (Anna University), Chennai. My core engineering focus lies at the intersection of embedded hardware, firmware design, sensor telemetry, and deterministic software systems.

I believe in rigorous engineering hygiene:
- **Transparent Verification**: Explicitly distinguishing physical silicon execution from software behavioral simulations and mock environments.
- **Deterministic Testing**: Relying on reproducible test suites, static analysis, and automated CI pipelines over unsubstantiated claims.
- **Fail-Safe Design**: Accounting for hardware watchdog timers, volatile registers, interrupt safety, and bounded loops in low-level firmware.

---

## 🧭 Public GitHub Projects Boards

Track live milestones, architectural backlogs, and hardware validation stages across three curated boards:

1. **[Board 4: Embedded Systems, Firmware & Hardware Integration](https://github.com/users/RONALD-REX-7/projects/4)** — Microcontroller firmware (ATmega328P, ESP32-S3), PlatformIO builds, peripheral bus protocols, and physical bench testing.
2. **[Board 3: Full-Stack Applications, Systems & Developer Platforms](https://github.com/users/RONALD-REX-7/projects/3)** — Next.js 16 applications, state machines, Supabase RLS policies, and academic cutoff evaluation engines.
3. **[Board 2: Hackathons, Academic Demonstrators & Edge Research](https://github.com/users/RONALD-REX-7/projects/2)** — Smart India Hackathon mine telemetry (SIH26025), battery runaway demonstrators, and civic problem-tracking prototypes.

---

## 🏆 Featured Engineering Repositories

### 1. [LumaGuard](https://github.com/RONALD-REX-7/LumaGuard)
> **Context-Aware Micro-Workspace Hazard & Proximity Guard**  
> *Arduino Nano (ATmega328P) • PlatformIO • SSD1306 OLED (I2C) • HC-SR04 • IR Flame (HW-084) • MIT*  
> **Lifecycle Status**: `Stage 4: Hardware Bench Tested (Physical Breadboard Prototype)`

- Physical embedded safety prototype executing non-blocking sensory arbitration across ultrasonic echo timing, 10-bit analog flame detection, and pushbutton arming.
- Multi-rate cooperative scheduler implementing temporal candidate persistence (250 ms hold) and bi-level distance hysteresis ($30.0\text{ cm} \to 33.0\text{ cm}$).
- Variable-cadence audible urgency modulation (900 ms idle pulse to 180 ms rapid hazard alarm).
- Automated GitHub Actions PlatformIO build matrix verifying deterministic AVR compilation (35.6% SRAM, 70.5% Flash).

### 2. [EmbeddedLab-OS](https://github.com/RONALD-REX-7/EmbeddedLab-OS) • [📋 Project Board](https://github.com/users/RONALD-REX-7/projects/4)
> **Deterministic Virtual Microcontroller Laboratory for ECE Education**  
> *Next.js 16 • TypeScript • Zustand • Vitest (169 Tests) • Supabase • Apache-2.0*  
> **Live System**: [embeddedlab-os.vercel.app](https://embeddedlab-os.vercel.app)  
> **Lifecycle Status**: `Stage 3: Software Tested (169 Unit & Integration Tests Passing)`

- Browser-based educational simulator modeling STM32-style peripheral registers (GPIO electrical states, PWM duty/period timing, ADC quantization equations, and UART frame transmission).
- 12-challenge automated validation engine verified by 17 test suites (169 unit and integration tests passing in CI).
- Strict architectural boundaries clearly delineating software behavioral simulation from physical silicon and analog SPICE emulation.

### 3. [sih26025 (MineGuard)](https://github.com/RONALD-REX-7/sih26025) • [📋 Project Board](https://github.com/users/RONALD-REX-7/projects/3)
> **Industrial Edge AI & LoRa Strata Early-Warning Telemetry System**  
> *ESP32-S3 Firmware • TinyML • Sub-GHz LoRa (IN865) • Next.js 16 • DGMS CMR 2017*  
> **Live Deployment**: [mineguard-sih26025.vercel.app](https://mineguard-sih26025.vercel.app)  
> **Lifecycle Status**: `Stage 2: Implemented in Software (Telemetry & Software Prototype)`

- Developed for Smart India Hackathon 2026 (Problem Statement ID: SIH26025) under the Ministry of Coal / Coal India Limited.
- Architecture designed around ESP32-S3: software-implemented BNO085/MPU6050 and ADS1220 drivers, LoRa link budget modeling, and non-blocking sensor acquisition; physical hardware is not fully integrated.
- On-device TinyML running MAD/EWMA anomaly scoring with dynamic reporting frequency adaptation; benchmark achieving 93.00% recall on 1,000 synthetic test vectors.
- Reconciles Moonidih geotechnical baseline thresholds with an interactive 16-node Bhowra-West Colliery demonstration scenario.

### 4. [QUARTZSENTRY](https://github.com/RONALD-REX-7/QUARTZSENTRY) • [📋 Project Board](https://github.com/users/RONALD-REX-7/projects/2)
> **Multi-Modal Early-Warning Software Demonstrator for Li-ion Battery Thermal Runaway**  
> *Vite • React 19 • TypeScript • Oxlint • WCAG 2.1 AA • Apache-2.0*  
> **Live Demonstrator**: [quartzsentry-prototype.vercel.app](https://quartzsentry-prototype.vercel.app)  
> **Lifecycle Status**: `Stage 2: Implemented in Software (Academic Software Demonstrator)`

- Academic engineering software demonstrator modeling early-precursor thermal runaway stages in 16-cell Li-ion battery modules (simulating multimodal sensor fusion and mitigation logic).
- Multi-spectral sensing simulation: Electrochemical Impedance Spectroscopy (EIS Nyquist drift), ultrasonic acoustic emissions (cavitation), off-gas detection ($H_2$ / VOCs), and thermodynamic telemetry.
- Accessible interface adhering to WCAG 2.1 AA standards (verified 6.16:1 text contrast) with strict disclaimers distinguishing client-side mathematical models and synthetic telemetry from physical battery hardware.

### 5. [CLASSY_CS](https://github.com/RONALD-REX-7/CLASSY_CS)
> **Auditable Academic Evaluation, GPA/CGPA & Admission Cutoff Engine**  
> *React 19 • TypeScript • Vite 7 • Tailwind CSS v4 • Vitest (31 Tests) • jsPDF • MIT*  
> **Lifecycle Status**: `Stage 3: Software Tested (31 Unit Tests Passing)`

- Client-side academic planning suite with Anna University 10-point GPA/CGPA credit-weighted calculation engine and high-resolution PDF/CSV export.
- Deterministic admission cutoff engine implementing official Tamil Nadu Engineering Admissions (TNEA) 200-point reduced scoring formula: $\text{Cutoff} = M + \frac{P}{2} + \frac{C}{2}$.
- National competitive entrance exam planners for JEE Main (75% board aggregate eligibility), JEE Advanced (category gating), and NEET UG (PCB eligibility and medical competitiveness bands).
- Automated CI pipeline running ESLint, Vitest (31 unit tests passing), and full production bundling.

### 6. [RUSH_HOUR_2026 (ProblemChain)](https://github.com/RONALD-REX-7/RUSH_HOUR_2026)
> **Civic Problem Verification & Startup Opportunity Ecosystem**  
> *Express.js • React 19 • TypeScript • Tailwind CSS v4 • MongoDB • Apache-2.0*  
> **Lifecycle Status**: `Stage 2: Implemented in Software (Hackathon Prototype)`

- Rush Hour 2026 Hackathon prototype bridging verified community civic problems with local entrepreneurship opportunities.
- Full-stack TypeScript architecture with JWT authentication, bcrypt password hashing, and dual-mode persistence (live MongoDB with resilient in-memory fallback store).
- Multi-dimensional contribution matrix documenting team subsystem provenance across historical sprint branches, separating Git-verified repo management/hardening from owner-reported hackathon co-development.

---

## 🛠️ Desktop & System Utilities

### [todo-rainmeter](https://github.com/RONALD-REX-7/todo-rainmeter)
> **Minimalist Ergonomic Desktop To-Do Skin for Rainmeter**  
> *Rainmeter INI • Lua • PowerShell • FontAwesome • GPL-3.0*

- Modern, distraction-free floating desktop widget featuring automatic mathematical proportional scaling across all font sizes.
- Native Windows RGB ColorDialog integration via PowerShell helper and persistent JSON task storage.
- Formal open-source asset licensing ([`ASSET_LICENSES.md`](https://github.com/RONALD-REX-7/todo-rainmeter/blob/main/ASSET_LICENSES.md)) and verified package integrity (`SHA256: 8580F5FFCD3283C528EAF2159FD5A9E4D8F0704C99BC6AFA09EFCF9883A520E6`).

---

## 📐 Seven-Stage Engineering Lifecycle

All repositories and technical specifications adhere strictly to this maturity classification:

| Stage | Classification | Definition |
| :---: | :--- | :--- |
| **1** | `Planned` | Theoretical formulation, pinout mapping, or architecture draft without code. |
| **2** | `Implemented in software` | Code/firmware written and syntactically valid, but lacks formal execution testing. |
| **3** | `Software tested` | Validated in automated test runners, host simulators (Wokwi, QEMU), or unit harnesses. |
| **4** | `Hardware bench tested` | Flashed to isolated physical microcontroller on a test bench; basic I/O and communication verified. |
| **5** | `Hardware integrated` | Connected to physical peripherals, sensors, and buses (I2C, SPI, UART, LoRa). |
| **6** | `Integrated prototype tested`| Full multi-subsystem physical prototype evaluated under laboratory conditions. |
| **7** | `Field validated` | Evaluated under operational, in-situ real-world deployment conditions. |

---

## 💻 Technical Competencies

| Domain | Core Competencies |
| :--- | :--- |
| **Microcontrollers & Firmware** | Arduino Nano (ATmega328P), ESP32-S3, STM32 / ARM Cortex-M architecture, PlatformIO, Register modeling, FreeRTOS |
| **Hardware Protocols & Buses** | UART, SPI, I2C, PWM, GPIO, Sub-GHz LoRa (SX1262 / IN865 band), LoRaWAN |
| **Sensors & Instrumentation** | BNO085 Inclinometry, ADS1220 24-bit Sigma-Delta ADC, Ultrasonic (HC-SR04), IR Flame (HW-084), EIS Impedance |
| **Edge AI & Signal Analysis** | Running MAD, EWMA, Robust Z-score rate-of-change, Scikit-learn (Isolation Forest) |
| **Software & Distributed Systems** | TypeScript, Next.js (App Router), React 19, Express.js, Zustand, Supabase (PostgreSQL, RLS), Convex |
| **DevSecOps & Testing Quality** | GitHub Actions CI/CD, Vitest, Pytest, Oxlint, ESLint, WCAG 2.1 AA Accessibility |

---

## 🤝 Collaboration & Privacy-Safe Contact

Open to collaborative technical work, open-source review, and research inquiries in:
- Firmware architecture, microcontroller peripheral simulation, and embedded register modeling.
- Resource-constrained TinyML algorithms and industrial sensor telemetry.
- Full-stack web platforms and interactive laboratories for engineering education.

- **GitHub Issues / Discussions**: [@RONALD-REX-7](https://github.com/RONALD-REX-7)
- **LinkedIn**: [linkedin.com/in/ron-rex](https://www.linkedin.com/in/ron-rex)
- **Credly Profile**: [credly.com/users/ronaldrex](https://www.credly.com/users/ronaldrex)
- **AWS Skills Profile**: [skillsprofile.skillbuilder.aws/user/ron](https://skillsprofile.skillbuilder.aws/user/ron)
- **SkillRack**: [skillrack.com/profile/540874/](https://www.skillrack.com/profile/540874/)
- **CoCubes Profile**: [cocubes.com/student/ronaldrexch](https://www.cocubes.com/student/ronaldrexch)
- **Public Developer Email**: `211186833+RONALD-REX-7@users.noreply.github.com`
- **Location**: Chennai, Tamil Nadu, India
