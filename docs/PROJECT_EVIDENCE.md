# Project evidence register

This is a concise audit index for the projects featured on the profile. Source repositories remain authoritative; this summary does not replace their build instructions, test reports or architecture records.

## Featured projects

| Project | Implemented boundary | Verified evidence | Explicit limitation |
|:--|:--|:--|:--|
| [LumaGuard](https://github.com/RONALD-REX-7/LumaGuard) | Arduino Nano / ATmega328P physical breadboard prototype; proximity and optical flame sensing; local OLED and audible/visual annunciation. | Nine end-to-end bench integration scenarios are documented in the project test report. | Academic bench demonstrator only; not a certified fire alarm or life-safety instrument. The DHT22 was excluded from the final build. |
| [EmbeddedLab OS](https://github.com/RONALD-REX-7/EmbeddedLab-OS) | Browser-based software models of GPIO, PWM, ADC and UART with guided exercises and challenge validation. | 169 documented Vitest tests; CI and application details are in the source repository. | Not a full MCU CPU emulator, electrical simulator or physical hardware validation platform. |
| [MineGuard / SIH26025](https://github.com/RONALD-REX-7/sih26025) | Mine-subsidence monitoring architecture, firmware/software components, machine-learning evaluation and a web telemetry demonstrator. | 93% recall on 1,000 synthetic geotechnical vectors; the repository labels this a reproducible simulation benchmark. It also documents partial bench work, firmware build evidence and software tests. | Not a completed physical monitoring network; full hardware integration and underground/field validation are incomplete. |
| [QUARTZSENTRY](https://github.com/RONALD-REX-7/QUARTZSENTRY) | Software demonstrator modelling temperature, impedance, acoustic and off-gas precursor channels. | Software build, interface and accessibility verification are documented in the repository. | Displayed telemetry and curves are synthetic; physical transducers and analogue front-end integration are incomplete. Not a certified BMS or safety system. |

## Additional projects

| Project | Scope |
|:--|:--|
| [CLASSY_CS](https://github.com/RONALD-REX-7/CLASSY_CS) | GPA/CGPA, academic evaluation and admissions-planning engines; 31 documented test assertions. |
| [ProblemChain / RUSH_HOUR_2026](https://github.com/RONALD-REX-7/RUSH_HOUR_2026) | Collaborative hackathon prototype. Repository history and its contribution matrix distinguish my repository-maintenance, security, CI and backend work from other team members' contributions. |
| [todo-rainmeter](https://github.com/RONALD-REX-7/todo-rainmeter) | Rainmeter-based Windows productivity skin using Lua and PowerShell; includes documented UI configuration and animation behaviour. |

## How to read the maturity labels

- **Physical prototype / bench tested** means the physical components were assembled and the described bench scenarios were executed. It does not imply certification or field deployment.
- **Software tested** means automated or documented tests exercise software behaviour. It does not imply hardware validation.
- **Software prototype / demonstrator** means the architecture or interface is implemented in software; simulated signals must be treated as simulated.
- **Synthetic benchmark** describes a result evaluated on generated test vectors, not measurements from a deployed system.

For reproducibility, use the test reports, CI workflows, build commands and evidence classifications in each source repository.

## Attribution & Engineering System Governance

This portfolio, verification harness, and evidence classification matrix are maintained by **Ronald Rex** ([@RONALD-REX-7](https://github.com/RONALD-REX-7)) with continuous integration and pair engineering support.
