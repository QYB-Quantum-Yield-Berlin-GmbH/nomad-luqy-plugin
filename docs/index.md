# Welcome to the **LuQY Pro NOMAD Plugin** documentation

This plugin provides **data parsing and analysis capabilities** for measurements from the **LuQY Pro system**, developed at **Quantum Yield Berlin GmbH (QYB)**.
It allows automatic extraction of measurement settings, results, and spectral data for integration into the [NOMAD](https://nomad-lab.eu) materials data infrastructure.

---

## 🚀 Overview

- **Parses LuQY measurement files** (`.txt`)
- Extracts **scalar parameters** (Laser Intensity, Bias Voltage, PLQY, QFLS, etc.)
- Extracts **spectral data arrays** (wavelength–intensity pairs)
- Produces structured NOMAD entries based on the **LuQYPro schema**

---

## 🧩 Repository structure

| Path | Description |
|------|--------------|
| `src/nomad_luqy_plugin/` | Source code of the parser and schema |
| `tests/` | Unit and integration tests |
| `docs/` | Documentation (this site) |
| `pyproject.toml` | Python project configuration |
| `mkdocs.yml` | Documentation site configuration |

---

## 🔍 Learn more

<div markdown="block" class="home-grid">
<div markdown="block">

### 🛠 How-to Guides
Step-by-step instructions for common tasks:
- [Install this plugin](how_to/install_this_plugin.md)
- [Use this plugin in NOMAD](how_to/use_this_plugin.md)

</div>
</div>

---

*Maintained by [Quantum Yield Berlin GmbH](https://quantum-yield-berlin.com/).*
