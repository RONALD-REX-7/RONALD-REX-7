<div align="center">

<img src="assets/signal-hero.gif" alt="Looping lavender and cyan circuit animation surrounding an embedded processor" width="100%">

# RONALD REX C H

**Electronics & Communication Engineering · Chennai, India · Class of 2028**

*Embedded firmware • Connected devices • Edge intelligence*

[LinkedIn](https://www.linkedin.com/in/ron-rex) · [GitHub](https://github.com/RONALD-REX-7) · [Credly](https://www.credly.com/users/ronaldrex) · [AWS Skill Builder](https://skillsprofile.skillbuilder.aws/user/ron)

<img src="assets/signal-ticker.svg" alt="Sense, process, connect, verify — engineering signal path" width="100%">

</div>

---

## 01 / Engineering identity

I’m an ECE undergraduate at **S.A. Engineering College, Chennai**, building depth in **embedded systems, microcontroller firmware and electronics**. I work close to the hardware: sensing, peripheral interfaces, firmware behaviour, debugging and verification.

My supporting interests are **Industrial IoT, connected-device security, cloud services and Edge AI/TinyML**—especially where local intelligence has a clear purpose on constrained devices.

<img src="assets/engineering-signal-map.svg" alt="Engineering workflow connecting electronics, firmware, connected devices, edge intelligence and cloud services" width="100%">

> **Engineering principle:** make system behaviour observable, make faults explicit, and make every performance claim traceable to evidence.

### Current technical focus

| Hardware & firmware | Connected & intelligent systems |
|:--|:--|
| Embedded C/C++, MCU fundamentals, firmware structure | Industrial IoT, telemetry and device connectivity |
| ATmega328P, ESP32-S3 and ARM Cortex-M concepts | Edge AI, TinyML and signal processing |
| GPIO, ADC, PWM, I2C, SPI, UART and timing | Cloud platforms, device security and CI |
| State machines, fault handling, testing and debugging | System architecture and technical documentation |

---

## 02 / Selected engineering work

Four projects, four different engineering problems. Their maturity labels are intentional: a physical prototype, a browser simulation, synthetic telemetry and a software demonstrator are not interchangeable forms of validation.

### 01 — LumaGuard
<img src="assets/lumaguard-signal.svg" alt="LumaGuard architecture: ultrasonic and flame sensors feed an Arduino Nano, which drives an OLED and audible or visual alerts; nine bench scenarios documented" width="100%">

**PHYSICAL BREADBOARD PROTOTYPE · HARDWARE BENCH TESTED**

**Context-aware micro-workspace proximity and hazard guard**

Arduino Nano / ATmega328P · Embedded C/C++ · PlatformIO · HC-SR04 · IR flame module · SSD1306 OLED

- Integrates ultrasonic proximity sensing, optical flame detection, local display and audible/visual alerts.
- Firmware implements proximity hysteresis, temporal flame-candidate persistence, non-blocking scheduling, echo-fault handling and EEPROM event counting.
- The project report documents **nine end-to-end bench integration scenarios**, including intrusion, flame confirmation, alert silence, arm/disarm, hysteresis clearing, echo timeout and persistence.

<p align="center"><img src="assets/breadboard_prototype.jpg" alt="Photograph of the LumaGuard physical breadboard prototype" width="78%"></p>

[Source code, pin mapping and test report](https://github.com/RONALD-REX-7/LumaGuard)

### 02 — EmbeddedLab OS
<img src="assets/embeddedlab-signal.svg" alt="EmbeddedLab OS virtual lab flow showing GPIO, PWM and ADC, UART, deterministic software models and 169 Vitest tests" width="100%">

**SOFTWARE TESTED · BROWSER-BASED VIRTUAL LABORATORY**

**A laboratory for learning embedded fundamentals**

Next.js · TypeScript · React · Zustand · Vitest · Supabase

- Interactive software models for GPIO, PWM, ADC and UART peripheral concepts.
- Guided laboratories, challenge-based learning and deterministic validation of simulated microcontroller states.
- **169 documented Vitest tests.** This is an educational software simulation—not a physical MCU, CPU-core emulator or hardware-validation environment.

<p align="center"><img src="assets/project-embeddedlab-os.png" alt="EmbeddedLab OS application interface" width="78%"></p>

[Open the live laboratory](https://embeddedlab-os.vercel.app) · [Source repository](https://github.com/RONALD-REX-7/EmbeddedLab-OS)

### 03 — MineGuard / SIH26025
<img src="assets/mineguard-signal.svg" alt="MineGuard concept showing underground LoRa sensor nodes and edge monitoring; reported recall is based on synthetic vectors" width="100%">

**SOFTWARE PROTOTYPE · HARDWARE INTEGRATION INCOMPLETE**

**Edge-intelligence concept for mine subsidence monitoring and early warning**

ESP32-S3 firmware concepts · LoRa / IN865 architecture · TinyML methods · Next.js · Supabase

- Proposed multi-node monitoring architecture developed around Smart India Hackathon problem statement **SIH26025**.
- Repository work includes system architecture, software components, firmware build work and a web telemetry demonstrator.
- Reported **93% recall** on **1,000 synthetic geotechnical test vectors**. This is not field performance or validation on deployed mine sensors.
- Some hardware bench work is documented; full multi-sensor integration and field validation remain incomplete.

<p align="center"><img src="assets/project-mineguard.png" alt="MineGuard software telemetry dashboard" width="78%"></p>

[Explore the demonstrator](https://mineguard-sih26025.vercel.app) · [Source repository](https://github.com/RONALD-REX-7/sih26025)

### 04 — QUARTZSENTRY
<img src="assets/quartzsentry-signals.svg" alt="Four synthetic QUARTZSENTRY signal channels: temperature, impedance, acoustic activity and off-gas" width="100%">

**SOFTWARE DEMONSTRATOR · PHYSICAL SENSOR INTEGRATION INCOMPLETE**

**Multimodal early-warning demonstrator for lithium-ion battery thermal runaway**

React · Vite · TypeScript · SVG signal visualisation

- Models four precursor channels: temperature, electrochemical impedance, acoustic activity and off-gas readings.
- Dashboard telemetry, Nyquist curves, acoustic values and gas readings are **synthetic signals generated in software**.
- Physical transducers and analogue front-end integration remain incomplete. This is not a certified battery-management or protection system.

<p align="center"><img src="assets/project-quartzsentry.png" alt="QUARTZSENTRY software demonstrator interface" width="78%"></p>

[Open the demonstrator](https://quartzsentry-prototype.vercel.app) · [Source repository](https://github.com/RONALD-REX-7/QUARTZSENTRY)

---

## 03 / More work

| Project | Scope | Evidence |
|:--|:--|:--|
| **CLASSY_CS** | Academic evaluation, GPA/CGPA calculation and admissions-planning engines | 31 documented test assertions · [Repository](https://github.com/RONALD-REX-7/CLASSY_CS) |
| **ProblemChain / RUSH_HOUR_2026** | Collaborative civic-tech hackathon prototype; my documented work includes initial scaffolding, security remediation, CI, TypeScript fixes and backend hardening | [Contribution record](https://github.com/RONALD-REX-7/RUSH_HOUR_2026) |
| **todo-rainmeter** | Windows desktop productivity skin using Rainmeter, Lua and PowerShell | [Repository](https://github.com/RONALD-REX-7/todo-rainmeter) |

---

## 04 / Technical toolkit

| Domain | Technologies and concepts |
|:--|:--|
| **Microcontrollers** | Arduino Nano / ATmega328P, ESP32-S3; ARM Cortex-M concepts |
| **Firmware** | Embedded C/C++, PlatformIO, state machines, non-blocking scheduling, interrupts, EEPROM |
| **Interfaces** | GPIO, ADC, PWM, I2C, SPI, UART; LoRa / IN865 system concepts |
| **Edge intelligence** | Python, sensor-data analysis, MAD, EWMA, robust Z-score and TinyML exploration |
| **Cloud & application layer** | AWS, TypeScript, React, Next.js, Node.js, Supabase |
| **Engineering workflow** | Git, GitHub Actions, testing, linting, Linux, Docker and technical documentation |

<img src="https://skillicons.dev/icons?i=c,cpp,arduino,python,typescript,react,nextjs,nodejs,aws,supabase,git,github,docker,linux,vscode" alt="Selected engineering technologies" width="100%">

*This is a practical toolkit, not a claim of equal proficiency in every technology. Some are used in projects; others are active learning areas.*

---

## 05 / AWS certifications

- [AWS Certified Cloud Practitioner](https://www.credly.com/badges/9176f0c6-a291-4072-a332-55abd5c9b6f8)
- [AWS Certified AI Practitioner](https://www.credly.com/badges/42dd44ed-6a82-4ee9-8733-e7bc202223b9)
- [AWS Certified Developer – Associate](https://www.credly.com/badges/5e338e11-1247-412a-926c-031eb4d5e2a4)
- [AWS Certified Solutions Architect – Associate](https://www.credly.com/badges/b662ec17-f239-48bd-b5d9-a7685d13be7a)

[View the public credential portfolio](https://www.credly.com/users/ronaldrex)

---

## 06 / GitHub achievements

- **Pull Shark** — unlocked
- **Quickdraw** — unlocked

[View my GitHub profile](https://github.com/RONALD-REX-7)

---

## 07 / Education

**B.E. Electronics and Communication Engineering**  
S.A. Engineering College · Chennai, Tamil Nadu, India  
2024–2028 · Expected graduation: **May 2028**

---

## 08 / Engineering values

- **Understand before abstracting.** Know what the sensor, peripheral or interface is doing before hiding it behind layers.
- **Verify the boundary.** Separate a successful build, a passing software test, a bench-tested circuit and a field-validated system.
- **Design for failure.** Timeouts, stale data, invalid states and recovery paths deserve explicit treatment.
- **Document for the next engineer.** Reproducible steps and honest limitations are part of the system.

I’m interested in student engineering collaborations and opportunities involving **embedded firmware, electronics, IoT, edge computing and device security**.

<div align="center">

<img src="assets/signal-ticker.svg" alt="Sense, process, connect, verify — engineering signal path" width="100%">

[LinkedIn](https://www.linkedin.com/in/ron-rex) · [GitHub](https://github.com/RONALD-REX-7) · [Credly](https://www.credly.com/users/ronaldrex) · [AWS Skill Builder](https://skillsprofile.skillbuilder.aws/user/ron)

<sub>Lavender × signal blue · Built close to the hardware · Documented with evidence</sub>

</div>
