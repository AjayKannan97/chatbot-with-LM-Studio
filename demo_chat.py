import random

def demo_chat_with_ai(messages):
    """Demo responses that simulate AI responses without API calls"""
    demo_responses = [
        "Hello! I'm Alex, your friendly customer service assistant. How can I help you today?",
        "I understand your concern. Let me help you with that right away!",
        "That's a great question! Here's what I can tell you about that...",
        "I'm here to help! Could you provide a bit more detail so I can assist you better?",
        "Thank you for reaching out. I'll do my best to resolve this for you.",
        "I appreciate your patience. Let me look into this for you.",
        "That's definitely something I can help with! Here's what you need to know...",
        "I'm sorry to hear about that issue. Let's get it sorted out together.",
        "Great! I'm glad I could help. Is there anything else you need assistance with?",
        "I'm here to make sure you have the best experience possible. What else can I help with?"
    ]
    
    # Get the last user message
    last_user_message = ""
    for msg in reversed(messages):
        if msg["role"] == "user":
            last_user_message = msg["content"].lower()
            break
    
    # Simple keyword-based responses
    if "hello" in last_user_message or "hi" in last_user_message:
        return "Hello! I'm Alex, your friendly customer service assistant. How can I help you today?"
    elif "help" in last_user_message:
        return "I'm here to help! What specific issue are you experiencing?"
    elif "thank" in last_user_message:
        return "You're very welcome! I'm glad I could help. Is there anything else you need assistance with?"
    elif "bye" in last_user_message or "goodbye" in last_user_message:
        return "Goodbye! Have a wonderful day, and feel free to reach out if you need anything else!"
    elif "name" in last_user_message:
        return "My name is Alex! I'm your dedicated customer service assistant."
    else:
        return random.choice(demo_responses)

def main():
    print("Welcome to Alex, your customer service assistant! (DEMO MODE)")
    print("Type 'exit' to quit.")
    print("Note: This is running in demo mode without API calls.")
    print()
    
    messages = [
        {
            "role": "system",
            "content": (
                "You are Alex, a friendly and helpful customer service assistant. "
                "Always greet the user by name if they provide it, answer questions clearly, "
                "and offer assistance with a positive attitude."
            )
        }
    ]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Alex: Thank you for chatting! Have a great day.")
            break
        messages.append({"role": "user", "content": user_input})
        response = demo_chat_with_ai(messages)
        print(f"Alex: {response}")
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main() 