import threading
import queue
import pyttsx3

speech_queue = queue.Queue()
stop_flag = threading.Event()

def _speak_worker():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)

    while not stop_flag.is_set():
        try:
            text = speech_queue.get(timeout=1)
        except queue.Empty:
            continue

        if text is None:
            break

        try:
            print("[TTS Worker] Speaking:", text)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("[TTS ERROR] Runtime error during TTS:", e)

def speak_stream(text: str):
    if text.strip():
        print("[TTS] Queued for speech:", text)
        speech_queue.put(text.strip())

def stop():
    stop_flag.set()
    speech_queue.put(None)

# Important: start the worker AFTER function defs
threading.Thread(target=_speak_worker, daemon=True).start()