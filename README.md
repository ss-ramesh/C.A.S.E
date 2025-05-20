# AI Assistant Project

This project is an AI assistant that interacts with users through the terminal. It is designed to provide a conversational experience and can be extended with various features.


## To-Do
- Model Mixing: Integrate Ollama for lightweight tasks and fallback to GPT-4 for complex queries.
- Voice Interface: Add TTS (Text-to-Speech) and STT (Speech-to-Text) modules for two-way vocal communication.
- Local UI: Develop a simple, locally-running GUI for users who prefer a graphical interface.
- Selfspy Integration: Analyze usage patterns from Selfspy (https://github.com/selfspy/selfspy) and store them privately.
- Personality: Look at Linguflex (https://github.com/KoljaB/Linguflex) to understand the custom personalities for local LLM

## Project Structure

```
ai-assistant
├── src
│   ├── main.py
│   ├── assistant
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── utils.py
├── requirements.txt
├── .gitignore
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