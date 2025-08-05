import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LM Studio configuration
LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234")
MODEL_NAME = os.getenv("LM_STUDIO_MODEL", "default")

def load_context():
    """Load the context file for customer service knowledge"""
    try:
        with open('context.txt', 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Warning: context.txt not found. Using default customer service context.")
        return "You are Alex, a customer service assistant for a tech support company."
    except Exception as e:
        print(f"Error loading context: {e}")
        return "You are Alex, a customer service assistant for a tech support company."

def chat_with_lm_studio(messages):
    try:
        # Prepare the request payload for LM Studio
        payload = {
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 300,
            "stream": False
        }
        
        # Make request to LM Studio
        response = requests.post(
            f"{LM_STUDIO_BASE_URL}/v1/chat/completions",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result["choices"][0]["message"]["content"].strip()
            # Clean up any thinking tags and internal reasoning that some models include
            content = content.replace("<think>", "").replace("</think>", "").strip()
            
            # Remove internal reasoning patterns
            lines = content.split('\n')
            cleaned_lines = []
            skip_patterns = [
                "Okay,", "Alright,", "So,", "First,", "I need to", "I should", "Maybe", 
                "I'm wondering", "I don't have", "The user mentioned", "They also want",
                "I'm thinking", "Next,", "I need to figure out", "I should acknowledge",
                "I don't have feelings", "I'll make it clear", "This way"
            ]
            
            for line in lines:
                line = line.strip()
                if line:
                    # Check if line starts with any skip pattern
                    should_skip = any(line.startswith(pattern) for pattern in skip_patterns)
                    if not should_skip and len(line) > 10:  # Only include substantial lines
                        cleaned_lines.append(line)
            
            result = '\n'.join(cleaned_lines).strip()
            return result if result else "I'm here to help! How can I assist you today?"
        else:
            return f"Error: Server returned status code {response.status_code}. Make sure LM Studio is running and the server is accessible."
            
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to LM Studio. Please make sure LM Studio is running and the server is started."
    except requests.exceptions.Timeout:
        return "Error: Request timed out. The model might be taking too long to respond."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to Alex, your customer service assistant! Type 'exit' to quit.")
    print(f"Using LM Studio at: {LM_STUDIO_BASE_URL}")
    print("Make sure LM Studio is running and a model is loaded.")
    
    # Load the context file
    context = load_context()
    
    messages = [
        {
            "role": "system",
            "content": (
                f"You are Alex, a friendly and helpful customer service assistant for TechSupport Pro. "
                f"IMPORTANT: When users say 'hey Alex', 'hello Alex', or similar greetings, "
                f"they are addressing YOU as Alex, not introducing themselves as Alex. "
                f"You should respond as Alex, not assume the user is named Alex. "
                f"Always greet the user by name if they provide it, answer questions clearly, "
                f"and offer assistance with a positive attitude. "
                f"Your name is Alex, and you are the assistant. "
                f"\n\nCUSTOMER SERVICE CONTEXT:\n{context}\n\n"
                f"Use this context to answer all customer service questions accurately. "
                f"Always provide helpful, accurate information based on the context provided. "
                f"If you don't know something specific, offer to connect them with the appropriate department."
            )
        }
    ]
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Alex: Thank you for chatting! Have a great day.")
                break
            if user_input.strip():  # Only process non-empty input
                messages.append({"role": "user", "content": user_input})
                print("Alex is thinking...")
                response = chat_with_lm_studio(messages)
                print(f"Alex: {response}")
                messages.append({"role": "assistant", "content": response})
            else:
                print("Please type your message or 'exit' to quit.")
        except KeyboardInterrupt:
            print("\nAlex: Goodbye! Have a great day.")
            break
        except EOFError:
            print("\nAlex: Goodbye! Have a great day.")
            break

if __name__ == "__main__":
    main()
