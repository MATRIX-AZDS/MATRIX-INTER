from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set OpenAI Key (we’ll add it later)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]
    
    # Ask OpenAI (like ChatGPT)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    bot_reply = response.choices[0].message["content"]
    return jsonify({"response": f"🤖 MATRIX: {bot_reply}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set OpenAI Key (we’ll add it later)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]
    
    # Ask OpenAI (like ChatGPT)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    bot_reply = response.choices[0].message["content"]
    return jsonify({"response": f"🤖 MATRIX: {bot_reply}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
