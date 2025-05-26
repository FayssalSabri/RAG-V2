from flask import Flask, render_template, request, jsonify
from chatbot import query_rag  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "")
    if not user_question.strip():
        return jsonify({"error": "Empty question"}), 400

    response_text = query_rag(user_question)
    return jsonify({"response": response_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
