# Alex - TechSupport Pro Customer Service Chatbot

A context-driven customer service chatbot that uses LM Studio to run local LLMs for technical support interactions. Available as both a command-line interface and a modern web application.

## Features

- Local LLM support via LM Studio
- No API costs or internet dependency
- Context-driven responses using `context.txt`
- Comprehensive technical support knowledge base
- Command-line interface for direct interaction
- Modern web interface with real-time chat
- Session management for conversation history
- Connection status monitoring
- Mobile-responsive design

## Setup

### 1. Install LM Studio

1. Download LM Studio from [https://lmstudio.ai/](https://lmstudio.ai/)
2. Install and launch LM Studio
3. Download a model from the LM Studio interface (recommended: Llama 2, Mistral, or similar)

### 2. Start LM Studio Server

1. In LM Studio, go to the "Local Server" tab
2. Click "Start Server" 
3. The server will start on `http://localhost:1234` by default

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment (Optional)

Create a `.env` file in the project directory:

```
LM_STUDIO_BASE_URL=http://localhost:1234
LM_STUDIO_MODEL=default
```

## Usage

### Command Line Interface

1. Make sure LM Studio is running with a model loaded
2. Start the server in LM Studio
3. Run the chatbot:

```bash
python chat.py
```

### Web Interface

1. Make sure LM Studio is running with a model loaded
2. Start the web application:

```bash
# Option 1: Using the script
./run_web_app.sh

# Option 2: Manual start
source venv/bin/activate
python web_app.py
```

3. Open your browser and go to: http://localhost:5001
4. Start chatting with Alex through the web interface!

### Web Interface Features

- **Real-time Chat**: Instant messaging with Alex
- **Connection Status**: Visual indicator showing LM Studio connection
- **Session Management**: Conversations are maintained during your session
- **Clear Chat**: Reset conversation history with one click
- **Mobile Responsive**: Works great on phones and tablets
- **Typing Indicators**: Shows when Alex is thinking

## Troubleshooting

- **Connection Error**: Make sure LM Studio server is running on the correct port
- **Timeout Error**: The model might be too large for your hardware, try a smaller model
- **No Response**: Check that a model is loaded in LM Studio

## Model Recommendations

For best performance with this chatbot, try these models in LM Studio:
- Llama 2 7B Chat
- Mistral 7B Instruct
- Phi-2
- TinyLlama

## Configuration

You can modify the following parameters in the code:
- `temperature`: Controls randomness (0.0-1.0)
- `max_tokens`: Maximum response length
- `LM_STUDIO_BASE_URL`: Server address (default: http://localhost:1234)

## Files

- `chat.py` - Command-line chatbot
- `web_app.py` - Flask web application
- `templates/index.html` - Web interface template
- `context.txt` - Customer service knowledge base
- `run_web_app.sh` - Script to start web application
- `requirements.txt` - Python dependencies
- `README.md` - This documentation # chat-app
# chatapp
# chat-app
# chat-app
# chatbot-with-LM-Studio
# chatbot-with-LM-Studio
