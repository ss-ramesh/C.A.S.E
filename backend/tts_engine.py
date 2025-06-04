import pyttsx3
import threading
import queue

engine = pyttsx3.init()
engine.setProperty('rate', 175)

speech_queue = queue.Queue()
stop_flag = threading.Event()

def _speak_worker():
    while not stop_flag.is_set():
        text = speech_queue.get()
        if text is None:
            break
        engine.say(text)
        engine.runAndWait()

# Launch background thread on import
threading.Thread(target=_speak_worker, daemon=True).start()

def speak_stream(text: str):
    speech_queue.put(text)

def stop():
    stop_flag.set()
    speech_queue.put(None)