# Use a pipeline as a high-level helper
import logging
from ollama import chat
from ollama import ChatResponse
from flask import Flask, request
logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S' 
)



logger = logging.getLogger(__name__) 
app = Flask(__name__)


@app.route("/", methods=["POST"])
def llama():
    user_input = request.json["user_input"]
    
    response: ChatResponse = chat(model='llama-3', messages=[
      {
        'role': 'user',
        'content': user_input,
      },
    ])
    
    logger.info(response['message']['content'])
    return {"llama_output": response['message']['content']}




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)