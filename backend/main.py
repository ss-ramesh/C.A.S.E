import re
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
    buffer = ""
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
                        chunk = data["message"]["content"]
                    elif "response" in data:
                        chunk = data["response"]
                    else:
                        continue

                    buffer += chunk
                    yield chunk  # Stream to frontend always
                    print(f"[DEBUG] Chunk received: {chunk}")
                    print(f"[DEBUG] Current buffer: {buffer}")
                    # Trigger TTS if buffer ends in strong punctuation AND is long enough
                    if len(buffer.strip()) > 5 and re.search(r"[.!?]['\"]?\s*$", buffer.strip()):
                        tts_engine.speak_stream(buffer.strip())
                        buffer = ""

                except json.JSONDecodeError:
                    continue

        # Flush leftover buffer
        if buffer.strip():
            tts_engine.speak_stream(buffer.strip())
            yield buffer.strip()

    except Exception as e:
        yield f"\n[ERROR] {str(e)}"
        tts_engine.speak_stream(f"\n[ERROR] {str(e)}")

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
