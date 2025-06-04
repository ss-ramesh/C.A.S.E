from chat_engine import ChatEngine
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import tts_engine, stt_engine
import requests
import os, io, json

app = FastAPI()
chat_engine = ChatEngine()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def stream_chat_response(user_input: str):
    """Yields chat response line-by-line while also sending to TTS"""
    try:
        response = requests.post(
            chat_engine.api_url,
            json={
                "model": chat_engine.model,
                "messages": [
                    {"role": "system", "content": chat_engine.system_message},
                    {"role": "user", "content": user_input}
                ],
                "stream": True
            },
            stream=True
        )
        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    data = json.loads(line)
                    if "message" in data and "content" in data["message"]:
                        content = data["message"]["content"]
                        tts_engine.speak_stream(content)
                        yield content
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        yield f"\n[ERROR] {str(e)}"

@app.post("/chat/audio")
async def handle_audio(audio: UploadFile):
    # Save temp audio file
    temp_path = f"temp/{audio.filename}"
    with open(temp_path, "wb") as f:
        f.write(await audio.read())
    user_input = stt_engine.transcribe(temp_path)
    os.remove(temp_path)

    return StreamingResponse(stream_chat_response(user_input), media_type="text/plain")

@app.post("/chat/text")
async def handle_text(prompt: str = Form(...)):
    return StreamingResponse(stream_chat_response(prompt), media_type="text/plain")

'''def main():
    print("Meet C.A.S.E!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("C.A.S.E: Goodbye!")
            break
        chat_engine.ask(user_input)

if __name__ == "__main__":
    main()'''
