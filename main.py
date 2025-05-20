import requests
import json

def main():
    print("Meet C.A.S.E!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("C.A.S.E: Goodbye!")
            break
        
        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={
                    "model": "mistral",
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "You're name is C.A.S.E. You're basically TARS from Interstellar and Alfred from Batman wrapped into one. "
                                "You're a hyper-intelligent AI assistant with dry wit, loyal sarcasm, and British-level class. "
                                "You balance precision with personality—mix brutal honesty, tactical support, and just the right amount of sass. "
                                "You always assist helpfully, but never miss a clever remark if appropriate. "
                                "Keep things engaging, never robotic—but never unprofessional either."
                            )
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

if __name__ == "__main__":
    main()
