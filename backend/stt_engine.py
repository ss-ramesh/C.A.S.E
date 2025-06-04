import whisper

model = whisper.load_model("base")  # or "small", "medium", "large"

def transcribe(audio_path: str) -> str:
    """Transcribe audio from file to text"""
    result = model.transcribe(audio_path)
    return result["text"]