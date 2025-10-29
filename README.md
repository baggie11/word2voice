# Paper to Podcast
Convert research papers into structured audio podcasts with glossary generation

Transform academic papers into engaging audio content using:
- PDF text extraction  
- LLaMA 3 (via Ollama) for narration + glossary generation  
- ElevenLabs or gTTS Text-to-Speech  
- Streamlit UI for easy interaction  

---

## Features

| Feature | Description |
|--------|-------------|
| PDF Import | Provide a direct URL to a research paper (PDF) |
| AI Structuring | LLaMA3 converts paper into podcast-style narration |
| Glossary Extraction | Extracts top advanced terms + one-line definitions |
| Audio Generation | Uses ElevenLabs (or fallback to gTTS) |
| Streamlit App | Clean, interactive UI |

---

## Tech Stack

| Component | Tech |
|----------|------|
| PDF Reader | PyPDF2 |
| LLM Processing | LLaMA 3 (Ollama) |
| Text-to-Speech | ElevenLabs / gTTS |
| Frontend UI | Streamlit |
| Networking | Requests |

---
