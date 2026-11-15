<div align="center">

<img src="assets/hero-signal-atlas.svg" width="100%" alt="Project Universe — animated multicolour engineering project archive">

<p>
  <img src="https://img.shields.io/badge/PROJECTS-09-8B5CF6?style=for-the-badge&labelColor=171A35" alt="Nine projects">
  <img src="https://img.shields.io/badge/HARDWARE-ROBOTICS-06B6D4?style=for-the-badge&labelColor=171A35" alt="Hardware and robotics">
  <img src="https://img.shields.io/badge/FIRMWARE-IOT-10B981?style=for-the-badge&labelColor=171A35" alt="Firmware and IoT">
  <img src="https://img.shields.io/badge/SOFTWARE-TOOLS-F97316?style=for-the-badge&labelColor=171A35" alt="Software tools">
</p>

</div>

# PROJECT ARCHIVE

A visual index of selected builds, prototypes, simulations and engineering tools. Each entry links to its source repository or live demonstrator. Implementation status is stated explicitly.

---

## 01 / Featured builds

<img src="assets/project-robotic-arm.svg" width="100%" alt="Animated robotic arm project graphic">

### Gesture-Controlled Robotic Arm

<sub><strong>PHYSICAL ROBOTICS SYSTEM</strong> · Arduino · MPU6050 · nRF24L01 · PCA9685</sub>

A wearable IMU glove wirelessly controls a physical multi-joint robotic arm.

- Arduino Nano transmitter and Arduino Uno receiver.
- MPU6050 orientation estimation with complementary filter and dead zone.
- nRF24L01 wireless link, PCA9685 PWM driver and SG90 / MG996R servos.
- Bounded joint targets, smoothed actuation and a 1-second radio watchdog with configured failsafe park coordinates.
- Two-link planar inverse-kinematics helper with workspace rejection.

[<img src="https://img.shields.io/badge/OPEN_SOURCE-7C3AED?style=flat-square&logo=github&logoColor=white" alt="Source repository">](https://github.com/RONALD-REX-7/gesture-controlled-robotic-arm) [<img src="https://img.shields.io/badge/PHYSICAL_DEMO-EC4899?style=flat-square&logo=youtube&logoColor=white" alt="Physical demonstration">](https://github.com/RONALD-REX-7/gesture-controlled-robotic-arm/blob/main/docs/media/physical_actuation_evidence.mp4) [Wiring & evidence](https://github.com/RONALD-REX-7/gesture-controlled-robotic-arm/tree/main/docs)

<p align="center"><img src="https://raw.githubusercontent.com/RONALD-REX-7/gesture-controlled-robotic-arm/main/docs/images/arm-and-glove.png" width="86%" alt="Physical robotic arm and wearable gesture glove"></p>

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

<img src="assets/project-edge-payload.svg" width="100%" alt="Animated Edge Payload Guard project graphic">

### Edge Payload Guard

<sub><strong>PUBLISHED SOFTWARE PACKAGE</strong> · Python · JSON Schema · CLI / API · Docker · GHCR</sub>

An offline-first JSON Schema validator for embedded and IoT telemetry payloads.

- Python API and CLI for validating JSON objects and arrays against trusted schemas.
- File and standard-input support, text or JSON output, deterministic issue paths and stable exit codes.
- External schema references are rejected to keep validation offline.
- Non-root container images published for Linux amd64 and arm64.
- CI covers Python 3.10–3.13, unit tests, CLI checks and container smoke tests.

```bash
docker pull ghcr.io/ronald-rex-7/edge-payload-guard:1.0.0
```

[Source repository](https://github.com/RONALD-REX-7/edge-payload-guard) · [Published container package](https://github.com/RONALD-REX-7/edge-payload-guard/pkgs/container/edge-payload-guard)

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

<img src="assets/project-todo-rainmeter.svg" width="100%" alt="Animated Todo Rainmeter project graphic">

### todo-rainmeter

<sub><strong>WINDOWS DESKTOP TOOL · RAINMETER · LUA · POWERSHELL</strong></sub>

A configurable desktop productivity skin for managing tasks and presenting a compact Windows widget interface.

[Source repository](https://github.com/RONALD-REX-7/todo-rainmeter)

<p align="center"><img src="assets/project-todo-rainmeter.jpg" width="82%" alt="Todo Rainmeter desktop widget"></p>

---

<div align="center">
  <sub>END OF PROJECT ARCHIVE · SOURCE LINKS LEAD TO THE IMPLEMENTATIONS</sub>
</div>
