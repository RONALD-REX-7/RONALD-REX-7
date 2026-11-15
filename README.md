<div align="center">

<img src="assets/hero-signal-atlas.svg" width="100%" alt="Ronald Rex — embedded systems and electronics engineering field notes">

<p>
  <a href="https://www.linkedin.com/in/ron-rex">LINKEDIN</a> &nbsp;·&nbsp;
  <a href="https://www.credly.com/users/ronaldrex">CREDLY</a> &nbsp;·&nbsp;
  <a href="https://skillsprofile.skillbuilder.aws/user/ron">AWS SKILL BUILDER</a> &nbsp;·&nbsp;
  <a href="mailto:ronaldrexch@gmail.com">EMAIL</a>
</p>

</div>

# Ronald Rex C H

**Electronics & Communication Engineering · Chennai, India · Class of 2028**

I work at the intersection of **electronics, embedded firmware and connected systems**. I’m building the fundamentals to design, bring up, debug and validate systems that interact with the physical world — from sensors and peripheral buses to edge processing and cloud telemetry.

[Portfolio](https://ronald-rex-7.github.io) · [GitHub](https://github.com/RONALD-REX-7) · [LinkedIn](https://www.linkedin.com/in/ron-rex)

---

## Engineering focus

| Area | Current focus |
|:--|:--|
| **Embedded systems** | Embedded C/C++, Arduino / ATmega328P, ESP32-S3, MCU fundamentals |
| **Electronics & interfaces** | GPIO, ADC, PWM, I2C, SPI, UART, sensor integration, debugging |
| **Connected devices** | IoT architecture, wireless telemetry, device-side validation |
| **Edge intelligence** | Sensor-data analysis, anomaly detection concepts, TinyML exploration |
| **Cloud & security** | AWS, telemetry pipelines, containerisation, secure software practices |

My preferred engineering workflow: **understand the hardware → establish the signal path → implement firmware → test failure cases → document evidence.**

---

## Selected engineering work

The projects below are presented with their actual implementation maturity. A physical prototype, a software simulator and an early-stage demonstrator are not interchangeable.

### 01 — Gesture-Controlled Robotic Arm

**PHYSICAL ROBOTICS SYSTEM · EMBEDDED WIRELESS CONTROL**

<p align="center">
  <img src="https://raw.githubusercontent.com/RONALD-REX-7/gesture-controlled-robotic-arm/main/docs/images/arm-and-glove.png" width="82%" alt="Physical gesture-controlled robotic arm and wearable IMU glove">
</p>

A wearable gesture controller drives a physical multi-joint arm through a wireless embedded control path.

- **Hardware:** Arduino Nano transmitter, MPU6050 6-axis IMU, nRF24L01 radio, Arduino Uno receiver, PCA9685 PWM controller and SG90 / MG996R servos.
- **Firmware:** complementary-filter orientation estimate, dead zone, bounded joint targets, per-joint motion limits and smoothed actuation.
- **Fault handling:** a 1-second radio watchdog moves the arm toward configured failsafe park coordinates.
- **Kinematics:** two-link planar inverse-kinematics helper rejects targets outside the configured workspace.

[Source code](https://github.com/RONALD-REX-7/gesture-controlled-robotic-arm) · [Hardware and wiring evidence](https://github.com/RONALD-REX-7/gesture-controlled-robotic-arm/tree/main/docs) · [Physical demonstration video](https://github.com/RONALD-REX-7/gesture-controlled-robotic-arm/blob/main/docs/media/physical_actuation_evidence.mp4)

### 02 — LumaGuard

**PHYSICAL PROTOTYPE · HARDWARE BENCH TESTED**

<p align="center">
  <img src="assets/project-lumaguard.jpg" width="76%" alt="LumaGuard Arduino Nano breadboard prototype">
</p>

A context-aware proximity and flame-hazard demonstrator built around an Arduino Nano / ATmega328P.

- HC-SR04 proximity sensing and optical flame detection feed a local hazard-state machine.
- SSD1306 OLED, LEDs and buzzer provide local status and annunciation.
- Firmware includes proximity hysteresis, flame-candidate persistence, non-blocking scheduling, stale-echo handling and EEPROM event counting.
- The project report documents **nine end-to-end bench integration scenarios**.

[Source, wiring and test report](https://github.com/RONALD-REX-7/LumaGuard)

<sub>Educational bench demonstrator only — not a certified fire alarm or life-safety instrument. The DHT22 was excluded from the final hardware baseline.</sub>

### 03 — EmbeddedLab OS

**SOFTWARE TESTED · VIRTUAL EMBEDDED LABORATORY**

<p align="center">
  <img src="assets/project-embeddedlab-os.png" width="82%" alt="EmbeddedLab OS virtual embedded laboratory interface">
</p>

A browser-based learning environment for exploring microcontroller peripheral behaviour without requiring physical hardware.

- Interactive software models for **GPIO, PWM, ADC and UART**, with guided laboratories and challenge validation.
- Deterministic peripheral-state and timing models, including ADC quantization and reference scaling.
- Includes a scoped AI learning assistant with request validation, rate limits and deterministic offline fallback.
- Automated Vitest coverage spans simulator mathematics, challenge validators, state stores, AI route security and release invariants.

[Launch the virtual laboratory](https://embeddedlab-os.vercel.app) · [Source and architecture](https://github.com/RONALD-REX-7/EmbeddedLab-OS)

<sub>Educational software simulation — not a physical MCU, CPU-core emulator, transistor-level circuit simulator or hardware-validation tool.</sub>

### 04 — Edge Payload Guard

**PUBLISHED SOFTWARE PACKAGE · PYTHON CLI / API · OCI CONTAINER**

An offline-first JSON Schema validator for embedded and IoT telemetry payloads.

- Python API and command-line interface for validating JSON objects and arrays against trusted schemas.
- Supports file input and standard input, text or machine-readable JSON output, deterministic issue paths and stable exit codes.
- Rejects external schema references to keep validation offline.
- Runs as a non-root container and publishes **Linux amd64 and arm64** images to GitHub Container Registry.
- CI covers Python 3.10–3.13, unit tests, CLI checks and container smoke tests.

```bash
docker pull ghcr.io/ronald-rex-7/edge-payload-guard:1.0.0
```

[Source repository](https://github.com/RONALD-REX-7/edge-payload-guard) · [Published container package](https://github.com/RONALD-REX-7/edge-payload-guard/pkgs/container/edge-payload-guard)

<sub>Validates message structure and constraints; it does not prove sensor accuracy, freshness, authenticity or safety.</sub>

### 05 — MineGuard · SIH26025

**SOFTWARE PROTOTYPE · PARTIAL HARDWARE BENCH WORK · FIELD INTEGRATION INCOMPLETE**

<p align="center">
  <img src="assets/project-mineguard.png" width="82%" alt="MineGuard mine-subsidence monitoring software demonstrator">
</p>

An edge-intelligence concept for mine-subsidence monitoring, developed around Smart India Hackathon problem statement **SIH26025**.

- ESP32-S3 firmware and a multi-node sensing / telemetry architecture, with LoRa IN865 communication concepts.
- Software demonstrator models deformation, tilt, strain and acoustic telemetry with a risk-analysis workflow.
- The repository reports **93% recall on 1,000 synthetic geotechnical test vectors**. This is a generated-data benchmark, not field performance.
- Partial bench work and firmware build evidence are documented; full multi-sensor integration and underground / field validation remain incomplete.

[Interactive demonstrator](https://mineguard-sih26025.vercel.app) · [Source, architecture and evidence](https://github.com/RONALD-REX-7/sih26025)

---

## Additional work

| Project | Scope |
|:--|:--|
| [QUARTZSENTRY](https://github.com/RONALD-REX-7/QUARTZSENTRY) | Software demonstrator for lithium-ion battery early warning. Displayed telemetry is synthetic; physical transducer and analogue-front-end integration is incomplete. |
| [CLASSY_CS](https://github.com/RONALD-REX-7/CLASSY_CS) | GPA / CGPA, academic evaluation and admissions-planning engines with documented automated tests. |
| [ProblemChain / RUSH_HOUR_2026](https://github.com/RONALD-REX-7/RUSH_HOUR_2026) | Collaborative civic-tech hackathon prototype. My documented work includes scaffolding, security remediation, CI, TypeScript fixes and backend hardening. |
| [todo-rainmeter](https://github.com/RONALD-REX-7/todo-rainmeter) | Windows productivity skin using Rainmeter, Lua and PowerShell. |

### Bare-metal reference

**ATmega328P Timer1 Fast PWM** — 16-bit Timer1, Mode 14 (ICR1 TOP), non-inverting OC1A output and cycle-aware C examples for 25 kHz PC fan / 20 kHz motor-drive use cases.

[Read the public Gist](https://gist.github.com/RONALD-REX-7/4abadd74f1de361fbb809ec717ff5d09)

---

## Technical toolkit

<p>
  <img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="C">
  <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=arduino&logoColor=white" alt="Arduino">
  <img src="https://img.shields.io/badge/ESP32-E7352C?style=flat-square&logo=espressif&logoColor=white" alt="ESP32">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="AWS">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React">
</p>

| Domain | Tools and concepts |
|:--|:--|
| **Microcontrollers & electronics** | Arduino Nano / ATmega328P, ESP32-S3, ARM Cortex-M concepts, sensors, breadboard prototyping |
| **Embedded firmware** | C, C++, PlatformIO, Arduino CLI, state machines, non-blocking scheduling, interrupts, EEPROM, watchdogs |
| **Peripheral interfaces** | GPIO, ADC, PWM, I2C, SPI, UART, nRF24L01, LoRa / IN865 concepts |
| **Edge intelligence** | Python, sensor-data analysis, statistical anomaly methods, TinyML exploration |
| **Cloud & application** | AWS, TypeScript, React, Next.js, Node.js, Supabase |
| **Engineering workflow** | Git, GitHub Actions, Linux, Docker, unit testing, CI, technical documentation |

<sub>Technologies are not all at the same proficiency level. Some are active learning and project-development areas; project descriptions identify implemented scope.</sub>

---

## AWS certifications

- [AWS Certified Cloud Practitioner](https://www.credly.com/badges/9176f0c6-a291-4072-a332-55abd5c9b6f8)
- [AWS Certified AI Practitioner](https://www.credly.com/badges/42dd44ed-6a82-4ee9-8733-e7bc202223b9)
- [AWS Certified Developer – Associate](https://www.credly.com/badges/5e338e11-1247-412a-926c-031eb4d5e2a4)
- [AWS Certified Solutions Architect – Associate](https://www.credly.com/badges/b662ec17-f239-48bd-b5d9-a7685d13be7a)

**NPTEL Cloud Computing** · Elite + Silver · **85%**

[Credly credentials](https://www.credly.com/users/ronaldrex) · [AWS Skill Builder profile](https://skillsprofile.skillbuilder.aws/user/ron)

---

## GitHub activity & recognition

- **Achievements:** Pull Shark · Pair Extraordinaire · Galaxy Brain · Quickdraw.
- Public repositories across embedded firmware, physical robotics, IoT validation tooling, software simulation and cloud-connected prototypes.
- Published GitHub Container Registry package and public bare-metal driver Gist.
- Contributions include collaborative hackathon work, CI automation, documentation, security remediation and project maintenance.

---

## Education

**B.E. Electronics and Communication Engineering**  
S.A. Engineering College · Chennai, Tamil Nadu, India  
2024–2028 · Expected graduation: **May 2028**

---

## Engineering principles

- **Understand before abstracting.** Know what the sensor, peripheral or interface is doing.
- **Verify the boundary.** Separate a successful build, passing software test, bench-tested circuit and field-validated system.
- **Design for failure.** Timeouts, stale data, invalid states and recovery paths deserve explicit treatment.
- **Document for the next engineer.** Reproducible steps and honest limitations are part of the system.

Interested in collaborations involving **embedded firmware, electronics, robotics, IoT, edge computing and device security**.

---

## Connect

**RONALD REX C H** · Chennai, India

- [LinkedIn](https://www.linkedin.com/in/ron-rex)
- [GitHub](https://github.com/RONALD-REX-7)
- [Credly](https://www.credly.com/users/ronaldrex)
- [AWS Skill Builder](https://skillsprofile.skillbuilder.aws/user/ron)
- **Email:** [ronaldrexch@gmail.com](mailto:ronaldrexch@gmail.com)

<sub>ENGINEERING FIELD NOTES · BUILT CLOSE TO THE HARDWARE</sub>
