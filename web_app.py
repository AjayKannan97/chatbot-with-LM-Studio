from flask import Flask, render_template, request, jsonify, session
import json
import os
from dotenv import load_dotenv
from chat import chat_with_lm_studio, load_context

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# LM Studio configuration
LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234")

@app.route('/')
def index():
    """Main page with chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Load the context file
        context = load_context()
        
        # Initialize or get conversation history from session
        if 'messages' not in session:
            session['messages'] = [
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
        
        # Add user message to conversation
        session['messages'].append({"role": "user", "content": user_message})
        
        # Get response from LM Studio
        response = chat_with_lm_studio(session['messages'])
        
        # Add assistant response to conversation
        session['messages'].append({"role": "assistant", "content": response})
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/clear', methods=['POST'])
def clear_chat():
    """Clear conversation history"""
    session.pop('messages', None)
    return jsonify({'status': 'success', 'message': 'Chat history cleared'})

@app.route('/health')
def health_check():
    """Health check endpoint"""
    try:
        import requests
        response = requests.get(f"{LM_STUDIO_BASE_URL}/v1/models", timeout=5)
        if response.status_code == 200:
            return jsonify({'status': 'healthy', 'lm_studio': 'connected'})
        else:
            return jsonify({'status': 'unhealthy', 'lm_studio': 'disconnected'})
    except:
        return jsonify({'status': 'unhealthy', 'lm_studio': 'disconnected'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)