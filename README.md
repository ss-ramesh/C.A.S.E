# AI Assistant Project

This project is an AI assistant that interacts with users through the terminal. It is designed to provide a conversational experience and can be extended with various features.


## To-Do
- Model Mixing: Integrate Ollama for lightweight tasks and fallback to GPT-4 for complex queries.
- Voice Interface: Add TTS (Text-to-Speech) and STT (Speech-to-Text) modules for two-way vocal communication.
- Personality: Use ElevenLabs to clone C.A.S.E's voice from Interstellar for TTS
- Selfspy Integration: Analyze usage patterns from Selfspy (https://github.com/selfspy/selfspy) and store them privately.
- Personality: Look at Linguflex (https://github.com/KoljaB/Linguflex) to understand the custom personalities for local LLM

## Project Structure

```
C.A.S.E/
├── main.py                      # Entry point, event loop & orchestration
├── config.yaml                  # Config for API keys, models, DB
│
├── frontend/
│   ├── hologram_display.py      # Animated 2D hologram (PyQt5 / tkinter + matplotlib)
│   └── news_feed_widget.py      # Live RSS feed based on changeable keywords
│
├── vision/
│   ├── gaze_detector.py         # OpenCV + MediaPipe for gaze + head pose
│   └── trigger_engine.py        # Wakeword (e.g., "Hey CASE") via Silero or VAD
│
├── audio/
│   ├── mic_listener.py          # Real-time audio stream + buffering
│   ├── stt_engine.py            # whisper.cpp for offline speech-to-text
│   └── tts_engine.py            # Coqui TTS for low-latency cloned voice
│
├── brain/
│   ├── chat_engine.py           # Personality + LLM orchestrator (Ollama + GPT fallback)
│   ├── memory_store.py          # Vector store + conversation memory
│   ├── rag_engine.py            # Local knowledge embedding + retrieval
│   └── summarizer.py            # Optionally summarize sessions
│
├── database/
│   ├── azure_connector.py       # Secure push/pull to Azure (SQL / Cosmos)
│   └── logs.sqlite              # Local fallback + sync to cloud
│
├── monitor/
│   └── selfspy_adapter.py       # Collect data on local activity (like Selfspy)
│
├── cloud/
│   └── sync.py                  # Async log/embedding syncing to Azure
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd ai-assistant
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the AI assistant, execute the following command in your terminal:
```
python src/main.py
```

## Features

- Interactive terminal-based conversation
- Customizable responses
- Easy to extend with additional functionalities

## License

This project is licensed under the MIT License. See the LICENSE file for more details.