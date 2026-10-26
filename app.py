
from flask import Flask, request
from html import escape

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>BEYCAN Python Test</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f1f6ff;
                text-align: center;
                padding: 60px 20px;
            }
            h1 { color: #1254c4; }
            input, button {
                padding: 12px;
                margin: 5px;
                border-radius: 6px;
            }
            button {
                background: #1254c4;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to BEYCAN 🚀</h1>
        <h3>My First Python Web Application</h3>
        <p>Python Flask Server is Running!</p>

        <form action="/hello" method="get">
            <input type="text" name="name"
                   placeholder="Enter your name" required>
            <button type="submit">Say Hello</button>
        </form>
    </body>
    </html>
    """

@app.route("/hello")
def hello():
    name = escape(request.args.get("name", "Student"))
    return f"<h1>Hello, {name}!</h1><p>Welcome to BEYCAN.</p><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
