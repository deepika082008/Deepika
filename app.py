import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Sselakkiya AI Argument Backend is Running!"})

@app.route('/argue', methods=['POST'])
def argue():
    data = request.json
    topic = data.get('topic', 'No topic')
    
    # Simple AI Logic
    response_text = f"Your topic is '{topic}'. Here is a strong argument: This topic is very important because it has both pros and cons that need to be discussed deeply."
    
    return jsonify({
        "topic": topic,
        "argument": response_text,
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT",
                                    5000)))
