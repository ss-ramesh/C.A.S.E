# AI Assistant Project

This project is an AI assistant that interacts with users through the terminal. It is designed to provide a conversational experience and can be extended with various features.


## To-Do
- Model Mixing: Integrate Ollama for lightweight tasks and fallback to GPT-4 for complex queries.
- Local STT: Use Distil-Whisper Git Repo
- Local TTS:

- Personality: Look at Linguflex (https://github.com/KoljaB/Linguflex) to understand the custom personalities for local LLM

## Upgrades
- Selfspy Integration: Analyze usage patterns from Selfspy (https://github.com/selfspy/selfspy) and store them privately.
- Front-end: Personalizing UI using Text Message front-end responses w/ TARS Image that switches to TARS Video of his display displaying text

## Usage
- cd backend && uvicorn main:app --reload --port 8000 (sets backend host to 8000)
- cd ... && ollama serve (starting the LlaMa Mistral server to talk)
- cd frontend && npm install && npm start (starting the frontend)
