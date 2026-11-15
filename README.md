<div align="center">

<img src="assets/hero-signal-atlas.svg" width="100%" alt="Project Universe — animated multicolour engineering project archive">

<p>
  <img src="https://img.shields.io/badge/PROJECTS-06-8B5CF6?style=for-the-badge&labelColor=171A35" alt="Nine projects">
  <img src="https://img.shields.io/badge/HARDWARE-IOT-06B6D4?style=for-the-badge&labelColor=171A35" alt="Hardware and robotics">
  <img src="https://img.shields.io/badge/FIRMWARE-IOT-10B981?style=for-the-badge&labelColor=171A35" alt="Firmware and IoT">
  <img src="https://img.shields.io/badge/SOFTWARE-TOOLS-F97316?style=for-the-badge&labelColor=171A35" alt="Software tools">
</p>

</div>

# PROJECT ARCHIVE

A visual index of selected builds, prototypes, simulations and engineering tools. Each entry links to its source repository or live demonstrator. Implementation status is stated explicitly.

---

## 01 / Featured builds

---

<img src="assets/project-lumaguard-signal.svg" width="100%" alt="Animated LumaGuard project graphic">

### LumaGuard

<sub><strong>PHYSICAL PROTOTYPE · BENCH TESTED</strong> · Arduino Nano · ATmega328P · HC-SR04 · Flame sensor · SSD1306</sub>

A proximity and flame-hazard demonstrator with local sensing, state handling and alerts.

- HC-SR04 proximity sensing and optical flame detection feed a local hazard-state machine.
- SSD1306 OLED, LEDs and buzzer provide local status and annunciation.
- Firmware includes proximity hysteresis, flame-candidate persistence, non-blocking scheduling, stale-echo handling and EEPROM event counting.
- Project report documents **nine end-to-end bench integration scenarios**.

[Source code, wiring and test report](https://github.com/RONALD-REX-7/LumaGuard)

<p align="center"><img src="assets/project-lumaguard.jpg" width="78%" alt="LumaGuard Arduino Nano breadboard prototype"></p>

<sub>Educational bench demonstrator only — not a certified fire alarm or life-safety instrument. DHT22 was excluded from the final hardware baseline.</sub>

---

<img src="assets/project-embeddedlab-signal.svg" width="100%" alt="Animated EmbeddedLab OS project graphic">

### EmbeddedLab OS

<sub><strong>SOFTWARE SIMULATOR</strong> · GPIO · PWM · ADC · UART · React · Vitest</sub>

A browser-based virtual embedded laboratory for exploring microcontroller peripheral behaviour without physical hardware.

- Interactive software models for GPIO, PWM, ADC and UART, with guided labs and challenge validation.
- Deterministic peripheral-state and timing models, including ADC quantization and reference scaling.
- Scoped AI learning assistant with request validation, rate limits and deterministic offline fallback.
- Automated Vitest coverage spans simulator mathematics, challenge validators, state stores, AI route security and release invariants.

[<img src="https://img.shields.io/badge/LAUNCH_LAB-06B6D4?style=flat-square" alt="Launch lab">](https://embeddedlab-os.vercel.app) [Source & architecture](https://github.com/RONALD-REX-7/EmbeddedLab-OS)

<p align="center"><img src="assets/project-embeddedlab-os.png" width="86%" alt="EmbeddedLab OS virtual embedded laboratory interface"></p>

<sub>Educational software simulation — not a physical MCU, CPU-core emulator, transistor-level circuit simulator or hardware-validation tool.</sub>

---

<img src="assets/project-mineguard-signal.svg" width="100%" alt="Animated MineGuard project graphic">

### MineGuard · SIH26025

<sub><strong>SOFTWARE PROTOTYPE · PARTIAL HARDWARE BENCH WORK · FIELD INTEGRATION INCOMPLETE</strong> · ESP32-S3 · LoRa / IN865 · Edge analytics</sub>

An edge-intelligence concept for mine-subsidence monitoring, developed around Smart India Hackathon problem statement SIH26025.

- ESP32-S3 firmware and a multi-node sensing / telemetry architecture, with LoRa IN865 communication concepts.
- Software demonstrator models deformation, tilt, strain and acoustic telemetry with a risk-analysis workflow.
- Repository reports **93% recall on 1,000 synthetic geotechnical test vectors** — a generated-data benchmark, not field performance.
- Partial bench work and firmware build evidence are documented; full multi-sensor integration and underground / field validation remain incomplete.

[<img src="https://img.shields.io/badge/OPEN_DEMO-F59E0B?style=flat-square" alt="Open demo">](https://mineguard-sih26025.vercel.app) [Source, architecture & evidence](https://github.com/RONALD-REX-7/sih26025)

<p align="center"><img src="assets/project-mineguard.png" width="86%" alt="MineGuard mine-subsidence monitoring software demonstrator"></p>

---

## 02 / More builds

<img src="assets/project-quartzsentry-v3.svg" width="100%" alt="Animated QUARTZSENTRY project graphic">

### QUARTZSENTRY

<sub><strong>SOFTWARE DEMONSTRATOR · BATTERY EARLY WARNING</strong></sub>

A lithium-ion battery early-warning demonstrator modelling temperature, electrochemical impedance, acoustic activity and off-gas precursor channels. Displayed telemetry is synthetic; physical transducer and analogue-front-end integration is incomplete.

[Source repository](https://github.com/RONALD-REX-7/QUARTZSENTRY)

<p align="center"><img src="assets/project-quartzsentry.png" width="82%" alt="QUARTZSENTRY software demonstrator interface"></p>

---

<img src="assets/project-classy.svg" width="100%" alt="Animated CLASSY CS project graphic">

### CLASSY_CS

<sub><strong>SOFTWARE TOOLING · ACADEMIC COMPUTATION</strong></sub>

GPA / CGPA, academic evaluation and admissions-planning engines with documented automated tests.

[Source repository](https://github.com/RONALD-REX-7/CLASSY_CS)

---

<img src="assets/project-rush-hour.svg" width="100%" alt="Animated RUSH HOUR 2026 project graphic">

### ProblemChain / RUSH_HOUR_2026

<sub><strong>COLLABORATIVE CIVIC-TECH HACKATHON PROTOTYPE</strong></sub>

Collaborative project work includes scaffolding, security remediation, CI, TypeScript fixes and backend hardening.

[Source repository & contribution record](https://github.com/RONALD-REX-7/RUSH_HOUR_2026)

<p align="center"><img src="assets/project-rush-hour.jpg" width="82%" alt="RUSH HOUR 2026 project interface"></p>

---

<div align="center">
  <sub>END OF PROJECT ARCHIVE · SOURCE LINKS LEAD TO THE IMPLEMENTATIONS</sub>
</div>
