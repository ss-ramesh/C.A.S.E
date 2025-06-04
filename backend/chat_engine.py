import requests
import json

class ChatEngine:
    def __init__(self, model="mistral", url="http://localhost:11434/api/chat"):
        self.model = "mistral"
        self.api_url = "http://localhost:11434/api/chat"
        self.system_message = (
            "You're name is C.A.S.E. You're basically TARS from Interstellar and Alfred from Batman wrapped into one. "
            "You're a hyper-intelligent AI assistant with dry wit, loyal sarcasm, and British-level class. "
            "You balance precision with personality—mix brutal honesty, tactical support, and just the right amount of sass. "
            "You always assist helpfully, but never miss a clever remark if appropriate. "
            "Keep things engaging, never robotic—but never unprofessional either. Keep it classy and humanely short. "
        )
    
    def ask(self, user_input):
        try:
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": self.system_message
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ],
                    "stream": True
                },
                stream=True
            )
            response.raise_for_status()
            
            print("C.A.S.E: ", end='', flush=True)
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    try:
                        data = json.loads(line)
                        if "message" in data and "content" in data["message"]:
                            print(data["message"]["content"], end='', flush=True)
                    except json.JSONDecodeError:
                        continue
            print()  # Newline after streaming is done

        except requests.exceptions.RequestException as e:
            print(f"\nC.A.S.E: Error communicating with Ollama - {e}")
        except ValueError:
            print("\nC.A.S.E: Received an invalid response from Ollama.")
