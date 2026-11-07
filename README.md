<!--
  RONALD REX C H | Engineering Portfolio
  Visual system: lavender / indigo / signal cyan
  Evidence policy: distinguish physical hardware, software tests and synthetic data.
-->

<div align="center">

<img src="assets/hero-v2.svg" alt="Ronald Rex C H — Embedded Systems, Firmware and Industrial IoT" width="100%">

<p>
  <a href="https://www.linkedin.com/in/ron-rex"><img src="https://img.shields.io/badge/LinkedIn-Connect-6D5AE6?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://www.credly.com/users/ronaldrex"><img src="https://img.shields.io/badge/AWS_Certifications-4_Verified-7C3AED?style=for-the-badge&logo=amazonaws&logoColor=white" alt="Four AWS certifications"></a>
  <a href="https://github.com/users/RONALD-REX-7/projects"><img src="https://img.shields.io/badge/Project_Boards-Explore-8B5CF6?style=for-the-badge&logo=github&logoColor=white" alt="GitHub project boards"></a>
  <a href="https://github.com/RONALD-REX-7"><img src="https://img.shields.io/badge/GitHub-Follow-4F46A5?style=for-the-badge&logo=github&logoColor=white" alt="GitHub profile"></a>
</p>

**ECE Undergraduate · Embedded Systems · Microcontroller Firmware · Industrial IoT**

*Building practical systems at the intersection of electronics, firmware, connectivity and edge intelligence.*

</div>

<img src="assets/section-rule.svg" alt="" width="100%">

## 01 / Profile

I’m an **Electronics and Communication Engineering undergraduate at S.A. Engineering College, Chennai**, graduating in **2028**. My primary direction is **embedded systems and firmware**, supported by **Industrial IoT, cloud-connected systems and security**. I’m also exploring **Edge AI and TinyML** for constrained devices.

I enjoy engineering work that connects software to real hardware: understanding peripheral behaviour, integrating sensors, designing reliable firmware, debugging interfaces and validating what a system actually does.

### Engineering priorities

| Primary focus | Supporting domains |
|:--|:--|
| Embedded C/C++, microcontroller firmware, sensor interfacing | Industrial IoT, LoRa, telemetry and edge connectivity |
| ATmega328P, ESP32-S3, ARM Cortex-M concepts | Edge AI, TinyML, signal processing |
| I2C, SPI, UART, PWM, ADC and real-time design fundamentals | Cloud platforms, application security and CI |

### Evidence-first engineering

I distinguish **what is physically built**, **what is software-tested**, and **what is simulated**. Project maturity labels below are intentional: a working dashboard is not proof of a working sensor node, and synthetic telemetry is not field data.

<img src="assets/section-rule.svg" alt="" width="100%">

## 02 / Selected projects

The projects below are ordered by relevance to my embedded-systems direction. Each card links to its source repository; the accompanying screenshots are existing project assets.

### 01 — LumaGuard

<p align="center"><img src="assets/project-lumaguard-card.svg" alt="LumaGuard — Arduino Nano embedded hardware project" width="100%"></p>

**Context-aware micro-workspace hazard and proximity guard**

<sub><strong>PHYSICAL PROTOTYPE · STAGE 4 — HARDWARE BENCH TESTED</strong></sub>

Arduino Nano (ATmega328P) · Embedded C/C++ · PlatformIO · HC-SR04 · IR flame sensor · SSD1306 OLED

- Physical breadboard prototype with ultrasonic proximity sensing, optical flame detection, local display and audible/visual alerts.
- Firmware includes proximity hysteresis, temporal candidate persistence, non-blocking scheduling and sensor-fault handling.
- The repository documents the hardware pin map, test evidence and build workflow.

<p align="center"><img src="assets/project-lumaguard.jpg" alt="Photograph of the LumaGuard physical breadboard prototype" width="88%"></p>

<p align="center"><a href="https://github.com/RONALD-REX-7/LumaGuard"><img src="https://img.shields.io/badge/Source_Code-View_Repository-6D5AE6?style=for-the-badge&logo=github&logoColor=white" alt="View LumaGuard repository"></a></p>

---

### 02 — EmbeddedLab OS

<p align="center"><img src="assets/project-embeddedlab-card.svg" alt="EmbeddedLab OS — virtual microcontroller laboratory" width="100%"></p>

**Browser-based virtual laboratory for embedded-systems learning**

<sub><strong>SOFTWARE TESTED · STAGE 3</strong></sub>

Next.js · TypeScript · Zustand · Vitest · Supabase

- Interactive software models for GPIO, PWM, ADC and UART peripheral concepts.
- Challenge-based learning and deterministic validation of simulated microcontroller states.
- **169 unit and integration tests** are documented by the project; this is a browser-based educational simulator, not physical MCU validation.

<p align="center"><img src="assets/project-embeddedlab-os.png" alt="EmbeddedLab OS application interface" width="88%"></p>

<p align="center">
  <a href="https://embeddedlab-os.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-Open-6D5AE6?style=for-the-badge&logo=vercel&logoColor=white" alt="Open EmbeddedLab OS"></a>
  <a href="https://github.com/RONALD-REX-7/EmbeddedLab-OS"><img src="https://img.shields.io/badge/Source_Code-Repository-4F46A5?style=for-the-badge&logo=github&logoColor=white" alt="EmbeddedLab OS repository"></a>
</p>

---

### 03 — MineGuard / SIH26025

<p align="center"><img src="assets/project-mineguard-card.svg" alt="MineGuard — mine subsidence monitoring architecture" width="100%"></p>

**Edge-intelligence concept for mine subsidence monitoring and early warning**

<sub><strong>SOFTWARE PROTOTYPE · STAGE 2 — HARDWARE INTEGRATION INCOMPLETE</strong></sub>

ESP32-S3 firmware concepts · LoRa (IN865) · TinyML methods · Next.js · Supabase

- SIH 2026 problem statement SIH26025: a proposed multi-node monitoring architecture for geotechnical telemetry.
- Repository work includes firmware/software components, system architecture and a web telemetry prototype.
- The reported **93% recall** result is from **1,000 synthetic test vectors**; it is not field performance or validation on deployed mine sensors.
- Physical sensing-node integration and field validation are not claimed as complete.

<p align="center"><img src="assets/project-mineguard.png" alt="MineGuard software telemetry dashboard" width="88%"></p>

<p align="center">
  <a href="https://mineguard-sih26025.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-Open-6D5AE6?style=for-the-badge&logo=vercel&logoColor=white" alt="Open MineGuard demo"></a>
  <a href="https://github.com/RONALD-REX-7/sih26025"><img src="https://img.shields.io/badge/Source_Code-Repository-4F46A5?style=for-the-badge&logo=github&logoColor=white" alt="MineGuard repository"></a>
</p>

---

### 04 — QUARTZSENTRY

<p align="center"><img src="assets/project-quartzsentry-card.svg" alt="QUARTZSENTRY — battery thermal runaway software demonstrator" width="100%"></p>

**Multimodal early-warning software demonstrator for Li-ion battery thermal runaway**

<sub><strong>SOFTWARE DEMONSTRATOR · STAGE 2 — PHYSICAL INTEGRATION INCOMPLETE</strong></sub>

React · Vite · TypeScript · SVG visualisation · WCAG accessibility

- Demonstrates software models for temperature, impedance, acoustic and off-gas precursor signals.
- Dashboard telemetry and sensor curves are **synthetic and generated in software**.
- No physical battery pack, integrated sensor front-end or certified battery protection system is claimed.

<p align="center"><img src="assets/project-quartzsentry.png" alt="QUARTZSENTRY software demonstrator interface" width="88%"></p>

<p align="center">
  <a href="https://quartzsentry-prototype.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-Open-6D5AE6?style=for-the-badge&logo=vercel&logoColor=white" alt="Open QUARTZSENTRY demo"></a>
  <a href="https://github.com/RONALD-REX-7/QUARTZSENTRY"><img src="https://img.shields.io/badge/Source_Code-Repository-4F46A5?style=for-the-badge&logo=github&logoColor=white" alt="QUARTZSENTRY repository"></a>
</p>

---

### Other software work

| Project | Focus | Repository |
|:--|:--|:--|
| **CLASSY_CS** | Rule-based academic evaluation, GPA/CGPA and admissions planning; project documents 31 tests. | [Source](https://github.com/RONALD-REX-7/CLASSY_CS) |
| **RUSH_HOUR_2026 / ProblemChain** | Civic problem verification and opportunity platform; contribution scope is documented separately in the repository. | [Source](https://github.com/RONALD-REX-7/RUSH_HOUR_2026) |
| **todo-rainmeter** | Windows desktop productivity skin using Rainmeter, Lua and PowerShell. | [Source](https://github.com/RONALD-REX-7/todo-rainmeter) |

<img src="assets/section-rule.svg" alt="" width="100%">

## 03 / Technical toolkit

<div align="center">

**Embedded & electronics**

<img src="https://skillicons.dev/icons?i=c,cpp,arduino,raspberrypi" alt="C, C++, Arduino and Raspberry Pi" />

**Software, cloud & engineering tools**

<img src="https://skillicons.dev/icons?i=python,typescript,js,react,nextjs,nodejs,aws,supabase,git,github,docker,linux,vscode" alt="Python, TypeScript, React, Next.js, Node.js, AWS, Supabase, Git, GitHub, Docker, Linux and VS Code" />

</div>

| Area | Tools and concepts |
|:--|:--|
| **Microcontrollers** | Arduino Nano / ATmega328P, ESP32-S3; ARM Cortex-M concepts |
| **Firmware** | Embedded C/C++, PlatformIO, state machines, interrupts, non-blocking scheduling, watchdogs and EEPROM |
| **Interfaces** | GPIO, ADC, PWM, I2C, SPI, UART; LoRa / IN865 system concepts |
| **Edge intelligence** | MAD, EWMA, robust Z-score, sensor data analysis and TinyML exploration |
| **Cloud & application layer** | AWS, TypeScript, React, Next.js, Node.js, Supabase |
| **Quality & workflow** | Git, GitHub Actions, unit/integration testing, linting and technical documentation |

*This toolkit lists technologies used in projects or actively studied; it is not a claim of equal proficiency across every item.*

<img src="assets/section-rule.svg" alt="" width="100%">

## 04 / AWS certifications

Four AWS certifications, with public credential verification:

<div align="center">

<a href="https://www.credly.com/badges/9176f0c6-a291-4072-a332-55abd5c9b6f8"><img src="https://img.shields.io/badge/AWS_Cloud_Practitioner-Verified-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Certified Cloud Practitioner"></a>

<a href="https://www.credly.com/badges/42dd44ed-6a82-4ee9-8733-e7bc202223b9"><img src="https://img.shields.io/badge/AWS_AI_Practitioner-Verified-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Certified AI Practitioner"></a>

<a href="https://www.credly.com/badges/5e338e11-1247-412a-926c-031eb4d5e2a4"><img src="https://img.shields.io/badge/AWS_Developer_Associate-Verified-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Certified Developer Associate"></a>

<a href="https://www.credly.com/badges/b662ec17-f239-48bd-b5d9-a7685d13be7a"><img src="https://img.shields.io/badge/AWS_Solutions_Architect_Associate-Verified-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Certified Solutions Architect Associate"></a>

[View all credentials on Credly](https://www.credly.com/users/ronaldrex)

</div>

<img src="assets/section-rule.svg" alt="" width="100%">

## 05 / GitHub activity

These third-party widgets are dynamic and may occasionally be unavailable. They are activity summaries, not measures of engineering skill.

<div align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=RONALD-REX-7&show_icons=true&hide_border=true&bg_color=F8F7FF&title_color=5B4BBD&icon_color=7C6CE0&text_color=45415C" alt="GitHub account statistics">
  <img height="165" src="https://streak-stats.demolab.com?user=RONALD-REX-7&hide_border=true&background=F8F7FF&ring=7C6CE0&fire=8B5CF6&currStreakLabel=5B4BBD&sideLabels=5B4BBD&dates=77718E" alt="GitHub contribution streak">
</div>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=RONALD-REX-7&bg_color=F8F7FF&color=51458A&line=7C6CE0&point=8B5CF6&area=true&hide_border=true" alt="GitHub contribution activity graph" width="100%">
</div>

<img src="assets/section-rule.svg" alt="" width="100%">

## 06 / Education & project boards

**B.E. Electronics and Communication Engineering**  
S.A. Engineering College · Chennai, Tamil Nadu, India  
2024–2028 · Expected graduation: **2028**

**Public project boards**

- [EmbeddedLab OS — Board #4](https://github.com/users/RONALD-REX-7/projects/4)
- [SIH 2026 / MineGuard — Board #3](https://github.com/users/RONALD-REX-7/projects/3)
- [QUARTZSENTRY — Board #2](https://github.com/users/RONALD-REX-7/projects/2)

<img src="assets/section-rule.svg" alt="" width="100%">

## 07 / Connect

I’m interested in meaningful work and learning opportunities involving **embedded firmware, electronics, IoT systems, edge computing and device security**.

<div align="center">

<a href="https://www.linkedin.com/in/ron-rex"><img src="https://img.shields.io/badge/LinkedIn-ron--rex-6D5AE6?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="https://github.com/RONALD-REX-7"><img src="https://img.shields.io/badge/GitHub-RONALD--REX--7-4F46A5?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
<a href="https://www.credly.com/users/ronaldrex"><img src="https://img.shields.io/badge/Credly-Credentials-8B5CF6?style=for-the-badge&logo=credly&logoColor=white" alt="Credly"></a>

<img src="assets/footer-v2.svg" alt="Built with curiosity, tested with evidence, documented with care." width="100%">

<sub>Designed in lavender and signal violet · Engineering claims are scoped to documented evidence</sub>

</div>
