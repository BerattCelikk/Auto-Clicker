<div align="center">

# 🖱️ ClickForge: High-Performance Automation Utility
### *A Precision-Engineered Framework for Rapid Peripheral Simulation & Human-Like Automation*

---

[![Overview](https://img.shields.io/badge/📖_Overview-blue?style=for-the-badge)](#-project-overview)
[![Key Features](https://img.shields.io/badge/✨_Key_Features-6f42c1?style=for-the-badge)](#-key-features)
[![Tech Stack](https://img.shields.io/badge/🛠️_Tech_Stack-success?style=for-the-badge)](#-tech-stack)
[![Architecture](https://img.shields.io/badge/🏗️_Architecture-orange?style=for-the-badge)](#-technical-architecture)
[![Installation](https://img.shields.io/badge/🚀_Quick_Start-red?style=for-the-badge)](#-getting-started)
[![Contact](https://img.shields.io/badge/📩_Contact-lightgrey?style=for-the-badge)](#-contact)

---

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pynput](https://img.shields.io/badge/Library-Pynput-blueviolet?style=flat-square)](https://pynput.readthedocs.io/)
[![Automation](https://img.shields.io/badge/Focus-System_Automation-005850?style=flat-square)](https://en.wikipedia.org/wiki/Automation)
[![Codiom](https://img.shields.io/badge/Powered_By-Codiom-FF4B4B?style=flat-square)](https://codiom.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-4caf50?style=flat-square)](https://opensource.org/licenses/MIT)

**Optimizing repetitive workflows through high-fidelity peripheral simulation.**

</div>

---

## 📖 Project Overview

The **ClickForge Automation Utility** is a robust software solution designed to simulate high-frequency mouse interactions with millisecond precision. Developed as a utility-focused asset of the **Codiom** initiative, this project focuses on low-latency execution and customizable event triggers.

As a Software Engineering student at Istanbul Aydın University, I architected this system to bridge the gap between manual repetitive tasks and programmatic efficiency, ensuring that the automation remains lightweight and resource-effective.

---

## ✨ Key Features

* **⚡ Ultra-Low Latency:** Optimized event loop for high-frequency clicking without system lag.
* **🛠️ Customizable Triggers:** Integrated keyboard listeners for instant start/stop control.
* **🎭 Stealth Mimicry:** Capabilities to implement non-deterministic click intervals to simulate human behavior.
* **📱 Cross-Platform Logic:** Architected to operate across different desktop environments with consistent timing.
* **⚙️ Precise Configuration:** Granular control over click frequency, button selection, and duration.

---

## 🛠️ Tech Stack

| Category | Technology | Usage |
| :--- | :--- | :--- |
| **Development** | **Python 3.9+** | Core logic and automation orchestration. |
| **Input Control** | **Pynput / PyAutoGUI** | Managing global keyboard listeners and mouse simulation. |
| **Multithreading** | **Threading Library** | Separating the GUI/Listener from the clicking execution engine. |
| **Mathematics** | **Random / Time** | Calculating precise intervals and jitter for human-like timing. |
| **Version Control** | **Git / GitHub** | Management of source code and architectural revisions. |

---

## 🏗️ Technical Architecture

The utility utilizes a **Threaded Controller Architecture**, where the listener runs as a daemon thread to monitor for global hotkeys while the executor manages the simulation loop.



### Mathematical Validation (Human-Like Jitter)

To ensure the automation bypasses basic pattern detection, the interval between clicks follows a **Gaussian Distribution**:

$$f(t) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{t-\mu}{\sigma}\right)^2}$$

Where:
* $t$ is the delay between clicks.
* $\mu$ is the target interval.
* $\sigma$ represents the intentional jitter (variance).

---

## 📂 Project Structure

```bash
.
├── 📄 main.py               # Application entry point and controller
├── 📄 clicker_engine.py     # Core clicking logic and threading
├── 📄 listener.py           # Global hotkey monitoring
├── 📄 config.yaml           # User-defined hotkeys and speed settings
├── 📄 requirements.txt      # Dependency manifest
└── 📄 README.md             # System Documentation
```

## 🚀 Getting Started

### 1. Installation

```bash
# Clone the repository
git clone [https://github.com/BerattCelikk/Auto-Clicker.git](https://github.com/BerattCelikk/Auto-Clicker.git)
cd Auto-Clicker

# Initialize virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```

### 2. Dependency Injection

```bash
pip install -r requirements.txt
```

### 3. Execution
To start the auto-clicker with default hotkeys:
```bash
python main.py

```


## 🗺️ Roadmap

- [ ] GUI Dashboard: Developing a modern interface using CustomTkinter for visual configuration.
- [ ] Macro Sequences: Recording and replaying complex mouse/keyboard movement paths.
- [ ] Image Recognition: Triggering clicks based on specific visual elements on the screen (Computer Vision).
- [ ] Profile Management: Saving different speed/pattern profiles for various applications.

---

<div align="center" id="contact">

Architected with precision by Berat Erol Çelik Founder of Codiom

Software Engineering @ Istanbul Aydın University

</div>


















