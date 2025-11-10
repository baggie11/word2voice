# Paper to Podcast — Transform Research Papers into Audio Podcasts

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-green.svg)](https://streamlit.io/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-orange.svg)](https://elevenlabs.io/)
[![LLaMA 3](https://img.shields.io/badge/LLaMA-3-purple.svg)](https://ollama.com/)

Author: [Bagavati Narayanan](https://github.com/baggie11)

Convert research papers into **structured audio podcasts** with **glossary generation**, enabling easier consumption of academic content.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [License](#license)

---

## Overview

**Paper to Podcast** transforms academic papers into engaging audio content.  
It extracts text from PDFs, converts them into podcast-style narration, and generates a glossary of key terms for easier understanding.

**Key Highlights:**
- Automated conversion from PDF → structured podcast
- Glossary generation for advanced terminology
- High-quality TTS via ElevenLabs or gTTS
- Interactive Streamlit UI for ease of use
- Works with direct PDF URLs or local files

---

## Features

| Feature | Description |
|--------|-------------|
| **PDF Import** | Provide a direct URL or upload a research paper in PDF format |
| **AI Structuring** | LLaMA 3 (via Ollama) converts paper into podcast-style narration |
| **Glossary Extraction** | Extracts top advanced terms with one-line definitions |
| **Audio Generation** | Generates speech using ElevenLabs, or fallback to gTTS |
| **Streamlit App** | Clean, interactive interface to navigate, listen, and export podcasts |

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| PDF Reader | PyPDF2 |
| LLM Processing | LLaMA 3 (Ollama) |
| Text-to-Speech | ElevenLabs / gTTS |
| Frontend UI | Streamlit |
| Networking | Requests |

---

## Setup Instructions

### 🔌 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/paper-to-podcast.git
cd paper-to-podcast
pip install -r requirements.txt
streamlit run app.py
```
## License

This project is licensed under the **Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)** License.

You are free to:
- **Share** — copy and redistribute the material in any medium or format.  
- **Adapt** — remix, transform, and build upon the material.

Under the following terms:
- **Attribution** — You must give appropriate credit and link back to this repository.  
- **NonCommercial** — You may **not** use this material for commercial purposes.  

No additional restrictions — you may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

📄 Full License: [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)  
© 2025 Bagavati Narayanan. All rights reserved.


