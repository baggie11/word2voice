import os
import uuid
import requests
import streamlit as st
from PyPDF2 import PdfReader
from elevenlabs.client import ElevenLabs
from gtts import gTTS


# === STEP 1: Download and extract PDF text ===
def extract_text_from_pdf_url(url):
    response = requests.get(url)
    filename = f"temp_{uuid.uuid4()}.pdf"
    with open(filename, "wb") as f:
        f.write(response.content)

    reader = PdfReader(filename)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    os.remove(filename)
    return full_text


# === STEP 2A: Structure the paper with Ollama ===
def structure_with_llama3(text):
    prompt = (
        "You're a science narrator. Read the research paper and extract:\n"
        "1. Abstract\n"
        "2. Motivation\n"
        "3. Background\n"
        "4. Inputs and Assumptions\n"
        "5. Methodology\n"
        "6. Results\n"
        "7. Why it matters\n\n"
        "Present this as a smooth podcast narration (no greetings or filler). Keep it informative and logically structured.\n\n"
        f"=== START ===\n{text[:12000]}\n=== END ==="
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        st.error(f"❌ Ollama (LLaMA 3) error in structuring: {e}")
        return ""


# === STEP 2B: Extract advanced words ===
def extract_advanced_terms(text):
    prompt = (
        "Extract a glossary of the top 15 most advanced, rare, or technical terms used in this research paper. "
        "For each term, give a simple one-line definition that a college student could understand.\n\n"
        f"=== START ===\n{text[:12000]}\n=== END ==="
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        st.error(f"❌ Ollama (LLaMA 3) error in glossary extraction: {e}")
        return ""


# === STEP 3: Convert narration to audio ===
def generate_audio(text):
    try:
        filename = f"podcast_{uuid.uuid4()}.mp3"
        elevenlabs = ElevenLabs(api_key='API_KEY')
        audio = elevenlabs.text_to_speech.convert(
            text=text,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )
        with open(filename, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        return filename
    except Exception as e:
        st.error(f"❌ TTS generation failed: {e}")
        return None


# === Streamlit UI ===
st.set_page_config(page_title="📚 Paper to Podcast", page_icon="🎧")
st.title("📚 Turn Research Papers into Podcasts 🎧")
st.markdown("🎙️ Generate narration + glossary using **LLaMA 3 + ElevenLabs**.")

pdf_url = st.text_input("🔗 Enter Research Paper PDF URL")

if st.button("🎧 Generate Podcast"):
    if not pdf_url:
        st.warning("Please enter a valid PDF URL.")
    else:
        with st.spinner("📥 Extracting PDF..."):
            raw_text = extract_text_from_pdf_url(pdf_url)

        with st.spinner("🧠 Structuring content with LLaMA 3..."):
            narration = structure_with_llama3(raw_text)

        with st.spinner("📘 Extracting advanced terms..."):
            glossary = extract_advanced_terms(raw_text)

        if narration:
            st.subheader("📝 Podcast Narration")
            st.text_area("Narration", narration, height=400)

            st.subheader("📗 Glossary of Advanced Terms")
            st.text_area("Advanced Vocabulary", glossary, height=300)

            with st.spinner("🎙️ Converting narration to audio..."):
                audio_path = generate_audio(narration)

            if audio_path:
                st.success("✅ Podcast Ready!")
                with open(audio_path, "rb") as f:
                    audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.download_button("⬇️ Download Podcast", audio_bytes, "research_podcast.mp3", "audio/mp3")
