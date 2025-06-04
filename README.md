# AI Assistant Project

This project is an AI assistant that interacts with users through the terminal. It is designed to provide a conversational experience and can be extended with various features.


## To-Do
- Model Mixing: Integrate Ollama for lightweight tasks and fallback to GPT-4 for complex queries.
- Voice Interface: Add TTS (Text-to-Speech) and STT (Speech-to-Text) modules for two-way vocal communication.
- Personality: Use ElevenLabs to clone C.A.S.E's voice from Interstellar for TTS
- Selfspy Integration: Analyze usage patterns from Selfspy (https://github.com/selfspy/selfspy) and store them privately.
- Personality: Look at Linguflex (https://github.com/KoljaB/Linguflex) to understand the custom personalities for local LLM

## Usage
- cd backend && uvicorn main:app --reload (sets backend host to 8000)
- cd ... && ollama serve (starting the LlaMa Mistral server to talk)
- cd frontend && npm start (starting the frontend)
