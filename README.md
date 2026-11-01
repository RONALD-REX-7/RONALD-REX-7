<div align="center">

# Ronald Rex C H

<!-- Hero Banner -->
<p align="center">
  <img src="assets/hero-banner.svg" alt="Ronald Rex C H — Electronics & Communication Engineering Portfolio" width="100%"/>
</p>

<!-- Dynamic Animated Typing Subtitle -->
<p align="center">
  <a href="https://github.com/RONALD-REX-7">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&duration=3000&pause=1000&color=6D28D9&center=true&vCenter=true&multiline=false&width=760&height=36&lines=B.E.+Electronics+%26+Communication+Engineering+Undergraduate;Microcontroller+Firmware+%26+Embedded+Systems+Engineer;Sub-GHz+LoRa+%26+Industrial+IoT+Telemetry+Architect;Edge+AI+%26+TinyML+Anomaly+Detection+Researcher;4x+AWS+Certified+%7C+Cloud+%2B+AI+%2B+Developer+%2B+Solutions+Architect" alt="Dynamic Engineering Subtitle" />
  </a>
</p>

<!-- Interactive Lavender Navigation Badges -->
<p align="center">
  <a href="https://www.linkedin.com/in/ron-rex"><img src="https://img.shields.io/badge/LinkedIn-ron--rex-7C3AED?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/></a>
  &nbsp;
  <a href="https://www.credly.com/users/ron-rex"><img src="https://img.shields.io/badge/Credly-Verified_4x_AWS-8B5CF6?style=flat-square&logo=credly&logoColor=white" alt="Credly Certifications"/></a>
  &nbsp;
  <a href="https://skillsprofile.skillbuilder.aws/user/ron"><img src="https://img.shields.io/badge/AWS-Skill_Profile-6D28D9?style=flat-square&logo=amazon-aws&logoColor=white" alt="AWS Skill Profile"/></a>
  &nbsp;
  <a href="https://github.com/users/RONALD-REX-7/projects"><img src="https://img.shields.io/badge/GitHub_Projects-3_Public_Boards-5B21B6?style=flat-square&logo=github&logoColor=white" alt="Public Roadmaps"/></a>
  &nbsp;
  <a href="https://github.com/RONALD-REX-7"><img src="https://img.shields.io/badge/GitHub-RONALD--REX--7-4C1D95?style=flat-square&logo=github&logoColor=white" alt="GitHub Profile"/></a>
</p>

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

</div>

## 1. Executive Engineering Profile

I am an **Electronics and Communication Engineering (ECE)** undergraduate at **S.A. Engineering College (Anna University), Chennai** (Expected Graduation: **2028**). My engineering focus centers on **Embedded Systems, Microcontroller Firmware, and Industrial IoT**, with secondary focus on **Edge AI and Intelligent Hardware**.

<table>
<tr>
<td width="50%" valign="top">

### 🔬 Core Technical Focus
- **Firmware & Low-Level C/C++**: Register configuration, interrupt service routines (ISRs), non-blocking cooperative schedulers, volatile qualifiers, Watchdog Timers (WDT), and EEPROM state persistence.
- **Microcontrollers & Buses**: ATmega328P (16 MHz AVR), ESP32-S3 (Xtensa dual-core), STM32 (ARM Cortex-M), I2C (`0x3C`), SPI, UART ring buffers, and sub-GHz LoRa (SX1262 / IN865).
- **Edge AI & TinyML**: On-device running Median Absolute Deviation (MAD), Exponentially Weighted Moving Average (EWMA), and Robust Z-score anomaly detection algorithms.

</td>
<td width="50%" valign="top">

### 🛡️ Zero-Fabrication Charter
- **Hardware Bench Evidence**: Physical silicon execution on hardware test benches is rigorously separated from software behavioral simulations and synthetic telemetry.
- **Seven-Stage Lifecycle**: All projects are cataloged strictly under verifiable maturity tiers: `Planned` → `Implemented in software` → `Software tested` → `Hardware bench tested` → `Hardware integrated` → `Integrated prototype tested` → `Field validated`.
- **Reproducible Engineering**: Every benchmark and architectural claim cites verified test harnesses and auditable CI builds.

</td>
</tr>
</table>

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 2. Featured Engineering Projects

Every featured project represents authentic, auditable engineering work with dedicated visual evidence.

---

### 1. [LumaGuard](https://github.com/RONALD-REX-7/LumaGuard)
> **Context-Aware Micro-Workspace Hazard & Proximity Guard**  
> **Target:** Arduino Nano (ATmega328P @ 16 MHz, 5V) • PlatformIO • Embedded C/C++  
> **Maturity Lifecycle:** `Stage 4: Hardware Bench Tested (Physical Breadboard Prototype)`

<p align="center">
  <img src="assets/project-lumaguard.jpg" alt="LumaGuard Physical Breadboard Hardware Prototype" width="90%"/>
</p>

- **Physical Embedded System**: Assembled and bench-tested on an 830-point solderless breadboard with the ATmega328P Nano, 0.96" SSD1306 OLED (I2C `0x3C`), HC-SR04 ultrasonic transducer, optical IR flame sensor, passive piezo buzzer, and control pushbutton.
- **Sensory Arbitration**: Non-blocking cooperative scheduler executing bi-level distance hysteresis ($30.0\text{ cm} \to 33.0\text{ cm}$ hold), temporal optical flame candidate persistence ($250\text{ ms}$), and proportional audible urgency modulation ($900\text{ ms} \to 180\text{ ms}$).
- **Fault Detection & Memory**: Detects missing echoes (`NO ECHO` / `ZONE UNKNOWN` after $800\text{ ms}$) and persists hazard counter signatures to internal EEPROM across power cycles.
- **Deterministic Build**: Automated PlatformIO CI build matrix verifying AVR memory constraints (35.6% SRAM, 70.5% Flash).

<p align="right">
  <a href="https://github.com/RONALD-REX-7/LumaGuard"><b>View Repository & Documentation →</b></a>
</p>

---

### 2. [EmbeddedLab-OS](https://github.com/RONALD-REX-7/EmbeddedLab-OS) • [📋 Project Board #4](https://github.com/users/RONALD-REX-7/projects/4)
> **Deterministic Virtual Microcontroller Laboratory for ECE Education**  
> **Stack:** Next.js 16 • TypeScript • Zustand • Vitest (169 Tests) • Supabase • Apache-2.0  
> **Live System:** [embeddedlab-os.vercel.app](https://embeddedlab-os.vercel.app)  
> **Maturity Lifecycle:** `Stage 3: Software Tested (Browser-based simulator; 169 unit & integration tests passing)`

<p align="center">
  <img src="assets/project-embeddedlab-os.png" alt="EmbeddedLab-OS Virtual Embedded Laboratory Interface" width="90%"/>
</p>

- **Register Behavioral Simulator**: Models STM32-style microcontroller peripheral registers, including GPIO electrical output states, PWM timer duty/period mathematics, ADC quantization transfer equations, and UART frame transmission.
- **Automated Validation**: 12-challenge automated student grading engine verified by 17 Vitest test suites (169 unit and integration tests passing in CI).
- **Engineering Transparency**: Explicitly scoped as an educational browser simulation tool, distinguishing register behavior from physical silicon execution and analog SPICE modeling.

<p align="right">
  <a href="https://embeddedlab-os.vercel.app"><b>Launch Live Simulator</b></a> &nbsp;|&nbsp; 
  <a href="https://github.com/RONALD-REX-7/EmbeddedLab-OS"><b>View Repository →</b></a>
</p>

---

### 3. [sih26025 (MineGuard)](https://github.com/RONALD-REX-7/sih26025) • [📋 Project Board #3](https://github.com/users/RONALD-REX-7/projects/3)
> **Industrial Edge AI & LoRa Strata Early-Warning Telemetry System**  
> **Stack:** ESP32-S3 Firmware (C++) • TinyML • Sub-GHz LoRa (IN865) • Next.js 16 • DGMS CMR 2017  
> **Live Deployment:** [mineguard-sih26025.vercel.app](https://mineguard-sih26025.vercel.app)  
> **Maturity Lifecycle:** `Stage 2: Implemented in Software (ESP32-S3 firmware & software prototype; physical hardware integration incomplete)`

<p align="center">
  <img src="assets/project-mineguard.png" alt="MineGuard SIH26025 Geotechnical Early-Warning Telemetry Platform" width="90%"/>
</p>

- **SIH 2026 Prototype**: Software telemetry prototype engineered for Smart India Hackathon 2026 (Problem Statement ID: SIH26025) under the Ministry of Coal / Coal India Limited.
- **Firmware Architecture**: ESP32-S3 driver implementations for BNO085/MPU6050 and ADS1220 24-bit strain gauge ADC, non-blocking FreeRTOS tasks, and theoretical SX1262 LoRa link budget calculations.
- **Edge Intelligence**: On-device running MAD/EWMA anomaly scoring with adaptive reporting cadences; benchmark achieves 93.00% recall on 1,000 synthetic geomechanical test vectors.

<p align="right">
  <a href="https://mineguard-sih26025.vercel.app"><b>Launch Live Platform</b></a> &nbsp;|&nbsp; 
  <a href="https://github.com/RONALD-REX-7/sih26025"><b>View Repository →</b></a>
</p>

---

### 4. [QUARTZSENTRY](https://github.com/RONALD-REX-7/QUARTZSENTRY) • [📋 Project Board #2](https://github.com/users/RONALD-REX-7/projects/2)
> **Multi-Modal Early-Warning Software Demonstrator for Li-ion Battery Thermal Runaway**  
> **Stack:** Vite • React 19 • TypeScript • Oxlint • WCAG 2.1 AA • Apache-2.0  
> **Live Demonstrator:** [quartzsentry-prototype.vercel.app](https://quartzsentry-prototype.vercel.app)  
> **Maturity Lifecycle:** `Stage 2: Implemented in Software (Academic software demonstrator with synthetic telemetry)`

<p align="center">
  <img src="assets/project-quartzsentry.png" alt="QUARTZSENTRY Thermal Runaway Multi-Modal Demonstrator Interface" width="90%"/>
</p>

- **Academic Simulation Demonstrator**: Software simulation platform modeling early-precursor thermal runaway stages in 16-cell Li-ion battery modules.
- **Multi-Modal Sensory Modeling**: Mathematical representations of Electrochemical Impedance Spectroscopy (EIS Nyquist drift), ultrasonic acoustic cavitation, off-gas emissions ($H_2$ / VOCs), and thermodynamic runaway boundaries.
- **Accessibility & Ethics**: WCAG 2.1 AA compliance (6.16:1 text contrast) with prominent disclaimers establishing that telemetry is synthetic with no physical battery pack or certified protection hardware.

<p align="right">
  <a href="https://quartzsentry-prototype.vercel.app"><b>Launch Live Demonstrator</b></a> &nbsp;|&nbsp; 
  <a href="https://github.com/RONALD-REX-7/QUARTZSENTRY"><b>View Repository →</b></a>
</p>

---

### 5. [CLASSY_CS](https://github.com/RONALD-REX-7/CLASSY_CS)
> **Auditable Academic Evaluation, GPA/CGPA & Admissions Planning Platform**  
> **Stack:** React 19 • TypeScript • Vite • Tailwind CSS v4 • Vitest (31 Tests) • jsPDF • MIT  
> **Maturity Lifecycle:** `Stage 3: Software Tested (31 unit tests passing)`

<p align="center">
  <img src="assets/project-classy-cs.png" alt="CLASSY_CS Academic Evaluation & Admissions Guidance Portal" width="90%"/>
</p>

- **Deterministic Evaluation Engine**: Computes Anna University 10-point GPA/CGPA credit-weighted evaluations with official Tamil Nadu Engineering Admissions (TNEA) 200-point reduced formulas: $\text{Cutoff} = M + \frac{P}{2} + \frac{C}{2}$.
- **Export & Type Safety**: High-resolution client-side PDF/CSV transcript generation and national entrance exam eligibility rulesets (JEE Main, JEE Advanced, NEET UG) verified by 31 Vitest unit tests.

<p align="right">
  <a href="https://github.com/RONALD-REX-7/CLASSY_CS"><b>View Repository & Tests →</b></a>
</p>

---

### 6. Supporting Software & Utilities

<table>
<tr>
<td width="50%" valign="top">

#### [RUSH_HOUR_2026 (ProblemChain)](https://github.com/RONALD-REX-7/RUSH_HOUR_2026)
*Civic Problem Verification & Startup Opportunity Ecosystem*  
`Express.js • React 19 • TypeScript • MongoDB • Apache-2.0`

<p align="center">
  <img src="assets/project-rush-hour.jpg" alt="RUSH_HOUR_2026 ProblemChain Interface" width="100%"/>
</p>

- **Reconciled Contribution Matrix**: Repository documentation separates **Git-Verified Work** (scaffolding `a3ab592`, 8 sprint branches, security scrubbing, CI automation, route authentication) from **Reported Work** (civic problem research, UI co-development).

<p align="right">
  <a href="https://github.com/RONALD-REX-7/RUSH_HOUR_2026"><b>Repository →</b></a>
</p>

</td>
<td width="50%" valign="top">

#### [todo-rainmeter](https://github.com/RONALD-REX-7/todo-rainmeter)
*Modern Desktop Task & Productivity Skin*  
`Rainmeter • Lua • PowerShell • INI • GPL-3.0`

<p align="center">
  <img src="assets/project-todo-rainmeter.jpg" alt="todo-rainmeter Desktop Skin Preview" width="100%"/>
</p>

- **Desktop Engineering**: Mathematical proportional font auto-scaling, PowerShell native Windows `ColorDialog` integration, persistent JSON task storage, and verified package integrity.

<p align="right">
  <a href="https://github.com/RONALD-REX-7/todo-rainmeter"><b>Repository →</b></a>
</p>

</td>
</tr>
</table>

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 3. Embedded Systems & Firmware Architecture

My firmware development adheres to real-time embedded safety and deterministic execution principles:
- **Low-Level Hardware Interfaces**: Direct register configuration, ADC sampling calibration, volatile qualifiers, bounded timing loops, and hardware watchdog timer (WDT) refresh cycles.
- **Bus Protocols**: Hardware I2C (address arbitration, clock stretching, bus recovery), SPI (clock phase/polarity modes), UART (frame buffering, ring buffers), and LoRa sub-GHz packet structures.
- **Noise Mitigation**: Temporal persistence filtering, moving average filters, and bi-level hysteresis thresholds to eliminate contact bounce and sensor chatter.

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 4. Edge AI & Industrial IoT Focus

Bridging physical sensor instrumentation with embedded machine learning:
- **Constrained Anomaly Scoring**: Running Median Absolute Deviation (MAD), Exponentially Weighted Moving Average (EWMA), and Robust Z-score algorithms for low-memory microcontrollers.
- **Adaptive Telemetry**: Dynamic reporting frequency scaling (reducing radio duty cycle during quiescent conditions; escalating packet rate during rapid sensor drift).
- **Geotechnical & Battery Research**: Physical link budget formulation, InSAR geospatial alignment, and multi-spectral early fault precursor identification.

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 5. AWS Certifications

AWS credentials earned through proctored examinations. Public verification links are provided below; raw AWS validation identifiers are intentionally not published in this README.

<table width="100%">
<thead>
<tr bgcolor="#EDE9FE">
<th align="left">Certification</th>
<th align="center">Issuing Body</th>
<th align="center">Issue Date</th>
<th align="center">Expiration Date</th>
<th align="center">Verification Proof</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>AWS Certified Cloud Practitioner</b></td>
<td align="center">Amazon Web Services</td>
<td align="center">August 9, 2026</td>
<td align="center">August 14, 2029</td>
<td align="center"><a href="https://www.credly.com/badges/9176f0c6-a291-4072-a332-55abd5c9b6f8"><img src="https://img.shields.io/badge/Credly-Verified_Badge-7C3AED?style=flat-square&logo=credly&logoColor=white" alt="Credly Cloud Practitioner"/></a></td>
</tr>
<tr>
<td><b>AWS Certified AI Practitioner</b></td>
<td align="center">Amazon Web Services</td>
<td align="center">August 1, 2026</td>
<td align="center">August 1, 2029</td>
<td align="center"><a href="https://www.credly.com/badges/42dd44ed-6a82-4ee9-8733-e7bc202223b9"><img src="https://img.shields.io/badge/Credly-Verified_Badge-7C3AED?style=flat-square&logo=credly&logoColor=white" alt="Credly AI Practitioner"/></a></td>
</tr>
<tr>
<td><b>AWS Certified Developer – Associate</b></td>
<td align="center">Amazon Web Services</td>
<td align="center">August 14, 2026</td>
<td align="center">August 14, 2029</td>
<td align="center"><a href="https://www.credly.com/badges/5e338e11-1247-412a-926c-031eb4d5e2a4"><img src="https://img.shields.io/badge/Credly-Verified_Badge-7C3AED?style=flat-square&logo=credly&logoColor=white" alt="Credly Developer Associate"/></a></td>
</tr>
<tr>
<td><b>AWS Certified Solutions Architect – Associate</b></td>
<td align="center">Amazon Web Services</td>
<td align="center">August 7, 2026</td>
<td align="center">August 7, 2029</td>
<td align="center"><a href="https://www.credly.com/users/ron-rex">Credly Profile</a> &nbsp;|&nbsp; <a href="https://aws.amazon.com/verification">AWS Verification Portal</a></td>
</tr>
</tbody>
</table>

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 6. Technical Competencies Matrix

<table width="100%">
<thead>
<tr bgcolor="#EDE9FE">
<th width="28%" align="left">Domain</th>
<th align="left">Competencies &amp; Verified Toolchains</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>Microcontrollers &amp; Silicon</b></td>
<td>Arduino Nano (ATmega328P @ 16 MHz), ESP32-S3 (Xtensa dual-core), STM32 / ARM Cortex-M architecture, Solderless breadboard prototyping, Voltage domain matching (3.3V / 5V)</td>
</tr>
<tr>
<td><b>Firmware &amp; Low-Level C/C++</b></td>
<td>PlatformIO, Arduino framework, Direct register access, State machines, Non-blocking cooperative schedulers, Interrupt handlers (ISRs), Watchdog timers (WDT), EEPROM</td>
</tr>
<tr>
<td><b>Bus Protocols &amp; RF</b></td>
<td>Hardware I2C (`0x3C`), SPI (CPOL/CPHA), UART ring buffers, PWM timers, Sub-GHz LoRa (SX1262 / IN865 band), LoRaWAN link budgets</td>
</tr>
<tr>
<td><b>Edge AI &amp; Signal Processing</b></td>
<td>Running Median Absolute Deviation (MAD), Exponentially Weighted Moving Average (EWMA), Robust Z-score rate-of-change, Sensor fusion, Scikit-learn</td>
</tr>
<tr>
<td><b>Software Platforms &amp; Web</b></td>
<td>TypeScript, React 19, Next.js 16 (App Router), Express.js, Zustand, Supabase (PostgreSQL, Row Level Security)</td>
</tr>
<tr>
<td><b>DevSecOps &amp; Testing Quality</b></td>
<td>GitHub Actions CI/CD (Node 26 LTS), PlatformIO CI matrix, Vitest, Jest, Oxlint, ESLint, WCAG 2.1 AA accessibility standards</td>
</tr>
</tbody>
</table>

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 7. Engineering Quality & Activity Metrics

<p align="center">
  <img src="assets/engineering-metrics.svg" alt="Engineering Verification & Toolchains Metrics" width="100%"/>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=RONALD-REX-7&theme=violet&background=F8F7FF&border=EDE9FE&stroke=7C3AED&ring=A78BFA&fire=7C3AED&currStreakLabel=7C3AED" alt="GitHub Contribution Streak" width="55%"/>
</p>

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 8. Education & Public Project Boards

<table>
<tr>
<td width="50%" valign="top">

### 🎓 Academic Background
- **Bachelor of Engineering (B.E.) in Electronics and Communication Engineering**  
  **Institution:** S.A. Engineering College (Affiliated to Anna University), Chennai  
  **Duration:** 2024 – 2028 (Expected Graduation: **2028**)  
  **Core Coursework:** Electronic Circuits, Digital Logic Design, Microcontrollers & Microprocessors, Signals & Systems, Linear Integrated Circuits, Communication Engineering, Computer Architecture.

</td>
<td width="50%" valign="top">

### 📋 Public GitHub Project Boards
Live technical roadmaps, issue backlogs, and hardware validation tracking:
1. **[Board #4: EmbeddedLab OS](https://github.com/users/RONALD-REX-7/projects/4)** — Microcontroller firmware architecture and virtual peripheral register modeling.
2. **[Board #3: SIH 2026 · MineGuard](https://github.com/users/RONALD-REX-7/projects/3)** — Mine strata monitoring, LoRa packet telemetry, and Edge AI anomaly detection.
3. **[Board #2: QUARTZSENTRY](https://github.com/users/RONALD-REX-7/projects/2)** — Battery thermal runaway simulation milestones, WCAG AA, and sensor fusion models.

</td>
</tr>
</table>

<p align="center">
  <img src="assets/separator-violet.svg" alt="Section Divider" width="100%"/>
</p>

## 9. Verified External Profiles & Contact

<div align="center">

| Profile | Channel / Identifier | Status |
| :--- | :--- | :---: |
| **LinkedIn** | [linkedin.com/in/ron-rex](https://www.linkedin.com/in/ron-rex) | Verified |
| **Credly Profile** | [credly.com/users/ronaldrex](https://www.credly.com/users/ronaldrex) | Verified (4 AWS Badges) |
| **AWS Skill Builder** | [skillsprofile.skillbuilder.aws/user/ron](https://skillsprofile.skillbuilder.aws/user/ron) | Verified |
| **GitHub Collaboration** | [@RONALD-REX-7](https://github.com/RONALD-REX-7) | Active |

<br/>

<sub>Crafted with engineering precision • Designed with Lavender Cyber-Engineering aesthetic • Zero-Fabrication verified</sub>

</div>
