# Ronald Rex C H

**B.E. Electronics and Communication Engineering**  
*Embedded Systems • Edge AI • TinyML • Sensor Instrumentation • Industrial & Automotive Systems*

[![GitHub](https://img.shields.io/badge/GitHub-RONALD--REX--7-181717?style=flat&logo=github)](https://github.com/RONALD-REX-7)
[![Email](https://img.shields.io/badge/Email-ronaldrex.ch%40gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:ronaldrex.ch@gmail.com)

---

## Engineering Overview

I am an Electronics and Communication Engineering undergraduate focused on the intersection of embedded hardware, physical sensor instrumentation, and edge intelligence. My work centers on building deterministic hardware simulations, mission-critical industrial monitoring systems, and TinyML-driven embedded architectures with rigorous testing, statutory compliance, and reproducible engineering baselines.

---

## Featured Systems & Engineering Work

### 1. [EmbeddedLab OS](https://github.com/RONALD-REX-7/EmbeddedLab-OS)
> **Deterministic Virtual Microcontroller Laboratory for ECE Education**  
> *Next.js 16 • TypeScript • Zustand • Vitest (169 Tests) • Supabase • Gemini API*  
> **Live System**: [embeddedlab-os.vercel.app](https://embeddedlab-os.vercel.app)

- Designed and built a browser-based deterministic virtual laboratory modeling STM32-style peripheral architecture without physical hardware dependencies.
- Implemented state models for **GPIO** (pull-up/pull-down internal resistance, floating, TTL thresholds), **PWM** (period, duty cycle, frequency-scaled SVG oscilloscope), **ADC** (quantization equations, 8–16 bit resolution, LSB calculation), and **UART** (baud timing, frame construction).
- Engineered a 12-challenge automated validation suite with 100% pure state assertions and verified by 17 test suites (169 unit and integration tests).
- Licensed under Apache 2.0 with continuous automated testing in GitHub Actions.

### 2. [QUARTZSENTRY](https://github.com/RONALD-REX-7/QUARTZSENTRY)
> **Multi-Precursor Early-Warning System for Li-ion Battery Thermal Runaway**  
> *Vite • React 19 • TypeScript • Oxlint • Vercel*  
> **Live Prototype**: [quartzsentry-prototype.vercel.app](https://quartzsentry-prototype.vercel.app)

- Academic engineering proof-of-concept developed with Team METRYPHOR (S.A. Engineering College) targeting lithium-ion battery safety in automotive and energy storage modules.
- Models multi-spectral sensor fusion: Electrochemical Impedance Spectroscopy (EIS Nyquist impedance drift), ultrasonic acoustic emissions (micro-crack cavitation), off-gas detection ($H_2$ / VOC electrolyte vaporization), and thermodynamics ($V, I, T$).
- Features three escalation alert states (Advisory, Warning, Critical) designed to trigger low-voltage contactor isolation before irreversible thermal propagation.
- Fully accessible interface adhering to WCAG 2.1 AA standards, licensed under Apache 2.0.

### 3. [MINEGUARD (SIH26025)](https://github.com/RONALD-REX-7/sih26025)
> **AI-Enabled Real-Time Mine Subsidence Monitoring & Early Warning System**  
> *ESP32-S3 Firmware • TinyML • Sub-GHz LoRa (IN865) • Next.js 16 • Supabase PostgreSQL • DGMS CMR 2017*  
> **Live Deployment**: [mineguard-sih26025.vercel.app](https://mineguard-sih26025.vercel.app)

- Developed for **Smart India Hackathon 2026** (Problem Statement ID: SIH26025) under the Ministry of Coal / Coal India Limited, benchmarked against Moonidih Underground Project (BCCL, Jharia Coalfield).
- Purpose-built to satisfy mandatory requirements of **DGMS CMR 2017 Regulation 112** (Strata Control and Monitoring Plan - SCAMP) with digital shift sign-offs and immutable audit trails.
- Complete hardware stack designed around the ESP32-S3 MCU: BNO085 2-axis digital inclinometer ($0.01^\circ$ resolution), ADS1220 24-bit Sigma-Delta ADC for vibrating wire strain gauges, Murata geophone for acoustic emission, and SX1262 LoRa (+20 dBm, 865.2 MHz).
- On-device edge TinyML pipeline executing running MAD, EWMA, and robust Z-score rate-of-change detection to dynamically adapt reporting frequency from 300s to 10s upon strata deformation.
- Unit fabrication engineered at ~₹4,850 (~$58 USD), delivering a 30x cost reduction compared to commercial imported strata monitoring stations.

### 4. [ProblemChain](https://github.com/RONALD-REX-7/RUSH_HOUR_2026)
> **Civic Issue Aggregator & Startup Feasibility Analysis Platform**  
> *React • Vite • Node.js / Express • AI Pipeline • MongoDB / Postman*

- Hackathon prototype built during Rush Hour 2026 connecting verified community pain points with structured entrepreneurial feasibility analysis.
- Modular architecture with dedicated services for AI ingestion, document transformation, and community-driven verification.

---

## Technical Competencies

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **Microcontrollers & Architectures** | ESP32-S3, STM32 / ARM Cortex-M (Register-level simulation), FreeRTOS |
| **Buses & Protocols** | I2C, SPI, UART, PWM, GPIO, sub-GHz LoRa (SX1262 / IN865 band), LoRaWAN |
| **Sensors & Instrumentation** | Inclinometers (BNO085), 24-bit Sigma-Delta ADCs (ADS1220), Geophones / Piezoelectric, EIS Impedance, Strain Gauges |
| **Edge AI & TinyML** | Microcontroller Feature Extraction, Running MAD, EWMA, Robust Z-score, Scikit-learn (Isolation Forest), C-Array Quantized Export |
| **Web & Distributed Systems** | TypeScript, Next.js 16 (App Router), React 19, Zustand, Supabase (PostgreSQL, RLS), WebSockets, Tailwind CSS |
| **DevSecOps & Testing** | GitHub Actions CI/CD, Vitest, Testing Library, ESLint, Oxlint, Dependabot, Security Policy (RFC 9116) |

---

## Current Focus & Direction

- Deepening firmware-level validation on physical STM32 / ESP32 platforms and hardware-in-the-loop (HIL) test harness design.
- Developing ultra-low-power TinyML models capable of sub-milliwatt continuous anomalous vibration classification on edge silicon.
- Exploring functional safety principles (ISO 26262 / IEC 61508) in safety-critical automotive BMS architectures.

---

## Contact & Links

- **GitHub**: [@RONALD-REX-7](https://github.com/RONALD-REX-7)
- **Email**: [ronaldrex.ch@gmail.com](mailto:ronaldrex.ch@gmail.com)
- **Location**: Chennai, India
