from flask import Flask, render_template, request, response
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(API_KEY=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo"

app = Flask(__name__)
app.secret_key = 'alura'

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)