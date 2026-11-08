# Portfolio visual system

## Identity

- **Direction:** human, technically grounded, portfolio-first.
- **Palette:** deep indigo and midnight navy as the canvas; lavender for identity and primary emphasis; signal blue/cyan for data flow and technical highlights; cool off-white for body text.
- **Visual language:** circuit traces, waveform timing, peripheral blocks, sensor nodes, system diagrams and restrained grid geometry.
- **Portrait:** intentionally omitted. The identity is built from engineering motifs and project evidence.

## Motion

Motion is used to communicate signal flow rather than decorate every element:
- Hero: moving trace highlights, pulsing endpoints and a waveform reveal.
- Engineering map: a traveling signal marker.
- Section dividers: slow moving highlight and a pulse.
- Footer: a signal-trace reveal.

The README relies on embedded SVG animation. GitHub clients, cached image proxies and external renderers may display a static frame. All text and project information remain available without animation. There are no scripts, CSS hover dependencies or JavaScript interactions.

## Layout principles

1. A clear narrative: engineering direction → featured projects → supporting work → toolkit → credentials → education → contact.
2. Each featured project has an original diagram and a real screenshot or physical photograph where available.
3. The artwork identifies the system; the screenshots show the actual project.
4. Status labels and limitation notes remain in text, not encoded only in colour.
5. No follower counters, streak widgets, contribution graphs or unverified performance badges.
6. Avoid claims of equal mastery across the entire toolchain.

## Asset register

| Asset | Purpose |
|:--|:--|
| `hero-v3.svg` | Portrait-free engineering identity banner with animated signal traces and MCU motif. |
| `engineering-map-v3.svg` | Hardware-to-cloud engineering pathway. |
| `project-*-v3.svg` | Distinct project-specific technical illustrations. |
| `credentials-v3.svg` | Four AWS certification categories. |
| `section-rule-v3.svg` | Shared animated divider. |
| `footer-v3.svg` | Engineering-loop closing visual. |
| Existing JPG/PNG assets | Actual project photographs and application screenshots; retained as evidence. |

## Maintenance

- Keep diagrams legible at GitHub's responsive image width.
- Preserve meaningful `alt` text and keep evidence statements in Markdown.
- Validate every local image reference and parse all SVGs before updating the branch.
- Keep new assets self-contained; no external fonts, scripts, CSS files or JavaScript.
