
from flask import Flask, request, render_template_string
from html import escape

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport"
          content="width=device-width, initial-scale=1">
    <title>BEYCAN Python Quiz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f6ff;
            padding: 30px 15px;
        }
        .card {
            background: white;
            max-width: 500px;
            margin: 30px auto;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 20px #ddd;
        }
        h1 { color: #1254c4; }
        .option {
            display: block;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
        button {
            background: #1254c4;
            color: white;
            border: 0;
            padding: 12px 25px;
            border-radius: 8px;
            cursor: pointer;
        }
        .result {
            padding: 15px;
            background: #eaf4ff;
            border-radius: 8px;
        }
    </style>
</head>
<body>
<div class="card">
    <h1>BEYCAN Coding Quiz</h1>
    <p>Learn Python Through Play!</p>

    <h3>Which function displays text
        on the screen in Python?</h3>

    <form method="POST">
        {% for option in options %}
        <label class="option">
            <input type="radio" name="answer"
                   value="{{ option }}" required>
            {{ option }}()
        </label>
        {% endfor %}
        <button type="submit">Submit Answer</button>
    </form>

    {% if result %}
    <div class="result">
        <h3>{{ result }}</h3>
        <p>Your Score: {{ score }}/10</p>
        <p>{{ explanation }}</p>
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    options = ["input", "print", "show", "display"]
    result = None
    score = 0
    explanation = ""

    if request.method == "POST":
        answer = request.form.get("answer", "")

        if answer == "print":
            result = "Correct! Well Done!"
            score = 10
        else:
            result = "Try Again!"
            explanation = "Correct answer: print()"

    return render_template_string(
        PAGE,
        options=options,
        result=result,
        score=score,
        explanation=explanation
    )

if __name__ == "__main__":
    app.run(debug=True)
