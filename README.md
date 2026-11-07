<div align="center">

<img src="assets/signal-atelier-hero.gif" alt="Animated Signal Atelier scene: a central microcontroller connected to glowing circuit paths, signal waveforms and telemetry nodes" width="100%">

<p>
  <a href="https://www.linkedin.com/in/ron-rex">LINKEDIN</a> ·
  <a href="https://www.credly.com/users/ronaldrex">AWS CREDENTIALS</a> ·
  <a href="https://skillsprofile.skillbuilder.aws/user/ron">AWS SKILL BUILDER</a> ·
  <a href="https://github.com/RONALD-REX-7">GITHUB</a>
</p>

# RONALD REX C H

**Electronics & Communication Engineering · Chennai, India · Class of 2028**

*Embedded systems, firmware and connected intelligence — built close to the hardware.*

</div>

---

## 01 / Engineering signal

I’m an ECE undergraduate at **S.A. Engineering College, Chennai**, focused on **embedded systems and microcontroller firmware**. I work across sensing, peripheral interfaces, firmware behaviour, debugging and verification.

My core direction is supported by **Industrial IoT, connected-device security and cloud services**. I’m exploring **Edge AI and TinyML** where constrained devices can benefit from local intelligence.

<img src="assets/signal-system-map.svg" alt="Engineering signal path connecting electronics and sensing, firmware control, connected IoT systems, edge intelligence and cloud telemetry" width="100%">

| Hardware & firmware | Connected and intelligent systems |
|:--|:--|
| Embedded C/C++, MCU fundamentals and firmware structure | Industrial IoT, telemetry and device connectivity |
| ATmega328P, ESP32-S3 and ARM Cortex-M concepts | Edge AI, TinyML and signal processing |
| GPIO, ADC, PWM, I2C, SPI, UART and timing | Cloud platforms, application security and CI |
| State machines, fault handling, testing and debugging | System architecture and technical documentation |

> **Engineering principle:** make system behaviour observable, make faults explicit, and make every performance claim traceable to evidence.

---

## 02 / Featured engineering work

Four projects. Four different engineering problems. Maturity labels are deliberate: a browser simulation is not an MCU emulator, synthetic telemetry is not field data, and a demonstrator is not a certified safety system.

### 01 — LumaGuard

<img src="assets/project-lumaguard-signal.svg" alt="LumaGuard architecture: HC-SR04 and flame sensing feed an Arduino Nano controller, which drives an OLED, buzzer and visual alert" width="100%">

**PHYSICAL PROTOTYPE · HARDWARE BENCH TESTED**

**Context-aware micro-workspace proximity and hazard guard**

Arduino Nano / ATmega328P · Embedded C/C++ · PlatformIO · HC-SR04 · IR flame module · SSD1306 OLED

- Physical breadboard prototype integrating ultrasonic proximity sensing, optical flame detection, local display and audible/visual alerts.
- Firmware implements proximity hysteresis, temporal flame-candidate persistence, non-blocking scheduling, echo-fault handling and EEPROM event counting.
- The project report documents **nine end-to-end bench integration scenarios**, including intrusion, flame confirmation, alert silence, arm/disarm, hysteresis clearing, echo timeout and persistence.

<p align="center"><img src="assets/project-lumaguard.jpg" alt="Photograph of the LumaGuard physical breadboard prototype" width="86%"></p>

[Source code, pin mapping and test report](https://github.com/RONALD-REX-7/LumaGuard)

---

### 02 — EmbeddedLab OS

<img src="assets/project-embeddedlab-signal.svg" alt="EmbeddedLab OS virtual laboratory modelling GPIO, PWM, ADC and UART behaviour with deterministic software tests" width="100%">

**SOFTWARE TESTED · VIRTUAL LABORATORY**

**A browser-based laboratory for learning embedded fundamentals**

Next.js · TypeScript · React · Zustand · Vitest · Supabase

- Interactive software models for GPIO, PWM, ADC and UART peripheral concepts.
- Guided laboratories, challenge-based learning and deterministic validation of simulated microcontroller states.
- **169 documented Vitest tests.** This is an educational software simulation—not a physical MCU, CPU-core emulator or hardware-validation environment.

<p align="center"><img src="assets/project-embeddedlab-os.png" alt="EmbeddedLab OS application interface" width="86%"></p>

[Open the live laboratory](https://embeddedlab-os.vercel.app) · [Source repository](https://github.com/RONALD-REX-7/EmbeddedLab-OS)

---

### 03 — MineGuard / SIH26025

<img src="assets/project-mineguard-signal.svg" alt="MineGuard proposed mine-monitoring architecture showing underground sensor nodes, LoRa IN865 communication, edge analysis and alerts" width="100%">

**SOFTWARE PROTOTYPE · HARDWARE INTEGRATION INCOMPLETE**

**Edge-intelligence concept for mine subsidence monitoring and early warning**

ESP32-S3 firmware concepts · LoRa / IN865 architecture · TinyML methods · Next.js · Supabase

- Proposed multi-node monitoring architecture developed around Smart India Hackathon problem statement **SIH26025**.
- Repository work includes system architecture, software components, firmware build work and a web telemetry demonstrator.
- The reported **93% recall** is a reproducible result on **1,000 synthetic geotechnical test vectors**. It is not field performance or validation on deployed mine sensors.
- Some hardware bench work is documented, but full multi-sensor integration and field validation are not complete.

<p align="center"><img src="assets/project-mineguard.png" alt="MineGuard software telemetry dashboard" width="86%"></p>

[Explore the demonstrator](https://mineguard-sih26025.vercel.app) · [Source repository](https://github.com/RONALD-REX-7/sih26025)

---

### 04 — QUARTZSENTRY

<img src="assets/project-quartzsentry-signal.svg" alt="QUARTZSENTRY multimodal battery demonstrator with temperature, impedance, acoustic and off-gas signal channels" width="100%">

**SOFTWARE DEMONSTRATOR · PHYSICAL SENSOR INTEGRATION INCOMPLETE**

**Multimodal early-warning demonstrator for lithium-ion battery thermal runaway**

React · Vite · TypeScript · SVG signal visualisation

- Models four precursor channels: temperature, electrochemical impedance, acoustic activity and off-gas readings.
- Dashboard telemetry, Nyquist curves, acoustic values and gas readings are **synthetic signals generated in software**.
- Physical transducers and analogue front-end integration remain incomplete. This is not a certified battery-management or protection system.

<p align="center"><img src="assets/project-quartzsentry.png" alt="QUARTZSENTRY software demonstrator interface" width="86%"></p>

[Open the demonstrator](https://quartzsentry-prototype.vercel.app) · [Source repository](https://github.com/RONALD-REX-7/QUARTZSENTRY)

---

## 03 / Additional work

| Project | Engineering scope | Evidence |
|:--|:--|:--|
| **CLASSY_CS** | Academic evaluation, GPA/CGPA calculation and admissions-planning engines. | 31 documented test assertions · [Repository](https://github.com/RONALD-REX-7/CLASSY_CS) |
| **ProblemChain / RUSH_HOUR_2026** | Collaborative civic-tech hackathon prototype. My documented work includes initial scaffolding, security remediation, CI, TypeScript fixes and backend hardening; team contributions are separately attributed. | [Contribution record and source](https://github.com/RONALD-REX-7/RUSH_HOUR_2026) |
| **todo-rainmeter** | Windows desktop productivity skin using Rainmeter, Lua and PowerShell, with configurable UI and animation behaviour. | [Repository and release](https://github.com/RONALD-REX-7/todo-rainmeter) |

---

## 04 / Engineering toolkit

| Domain | Current toolkit |
|:--|:--|
| **Microcontrollers** | Arduino Nano / ATmega328P, ESP32-S3; ARM Cortex-M concepts |
| **Firmware** | Embedded C/C++, PlatformIO, state machines, non-blocking scheduling, interrupts, EEPROM |
| **Interfaces** | GPIO, ADC, PWM, I2C, SPI, UART; LoRa / IN865 system concepts |
| **Edge intelligence** | Python, sensor-data analysis, MAD, EWMA, robust Z-score and TinyML exploration |
| **Cloud and application layer** | AWS, TypeScript, React, Next.js, Node.js, Supabase |
| **Engineering workflow** | Git, GitHub Actions, testing, linting, Linux, Docker and technical documentation |

<img src="https://skillicons.dev/icons?i=c,cpp,arduino,python,typescript,react,nextjs,nodejs,aws,supabase,git,github,docker,linux,vscode" alt="Selected engineering technologies" width="100%">

*This is a practical toolkit, not a claim of equal proficiency in every technology. Some are used in projects; others are active learning areas.*

---

## 05 / AWS certifications

<img src="assets/credentials-v3.svg" alt="Four AWS certifications across foundational, AI, developer and solutions architect tracks" width="100%">

- [AWS Certified Cloud Practitioner](https://www.credly.com/badges/9176f0c6-a291-4072-a332-55abd5c9b6f8)
- [AWS Certified AI Practitioner](https://www.credly.com/badges/42dd44ed-6a82-4ee9-8733-e7bc202223b9)
- [AWS Certified Developer – Associate](https://www.credly.com/badges/5e338e11-1247-412a-926c-031eb4d5e2a4)
- [AWS Certified Solutions Architect – Associate](https://www.credly.com/badges/b662ec17-f239-48bd-b5d9-a7685d13be7a)

[View the public credential portfolio](https://www.credly.com/users/ronaldrex)

---

## 06 / GitHub engineering milestones

| Milestone | Status / metric | Engineering context |
|:--|:--:|:--|
| **Pull Shark — Bronze** | 34 merged PRs | Peer-reviewed changes across firmware, CI and test repositories |
| **YOLO** | Unlocked | GitHub achievement |
| **Quickdraw** | Unlocked | Rapid issue / PR response |
| **Pair Extraordinaire** | 10 co-authored PRs | Collaborative contribution record |
| **Galaxy Brain** | 4 active solutions | Technical answers and discussions |
| **Releases & packaging** | 4 published releases | LumaGuard, EmbeddedLab-OS, todo-rainmeter and QUARTZSENTRY |
| **GitHub Pro** | Active | Developer account plan |

---

## 07 / Education

**B.E. Electronics and Communication Engineering**  
S.A. Engineering College · Chennai, Tamil Nadu, India  
2024–2028 · Expected graduation: **May 2028**

## 08 / Engineering principles

- **Understand before abstracting.** Know what the sensor, peripheral or interface is doing before hiding it behind layers.
- **Verify the boundary.** Separate a successful build, a passing software test, a bench-tested circuit and a field-validated system.
- **Design for failure.** Timeouts, stale data, invalid states and recovery paths deserve explicit treatment.
- **Document for the next engineer.** Reproducible steps and honest limitations are part of the system.

I’m interested in student engineering collaborations and opportunities involving **embedded firmware, electronics, IoT, edge computing and device security**.

---

## 09 / Connect

<div align="center">

<a href="https://www.linkedin.com/in/ron-rex">LinkedIn</a> ·
<a href="https://github.com/RONALD-REX-7">GitHub</a> ·
<a href="https://www.credly.com/users/ronaldrex">Credly</a> ·
<a href="https://skillsprofile.skillbuilder.aws/user/ron">AWS Skill Builder</a>

<img src="assets/signal-atelier-footer.svg" alt="Engineering sequence: build, measure, debug and verify" width="100%">

<sub>Lavender × signal blue · Built close to the hardware · Documented with evidence</sub>

</div>
