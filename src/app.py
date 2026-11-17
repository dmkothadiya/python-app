from flask import Flask, Response, jsonify


app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello, Backstage!</title>
    <style>
      body {
        align-items: center;
        background: #f4f6fb;
        color: #20243a;
        display: flex;
        font-family: system-ui, sans-serif;
        justify-content: center;
        margin: 0;
        min-height: 100vh;
        text-align: center;
      }
      main {
        background: white;
        border-radius: 16px;
        box-shadow: 0 12px 40px #20243a18;
        padding: 3rem;
      }
      p {
        color: #606780;
      }
    </style>
  </head>
  <body>
    <main>
      <h1>Hello, Backstage!</h1>
      <p>Your demo Flask application is up and running.</p>
    </main>
  </body>
</html>"""


@app.route("/api/v1/healthz")
def health() -> Response:
    return jsonify(status="ok"),  200


@app.route("/api/v1/details")
def details() -> Response:
    return jsonify(
        name="python-app",
        description="Hello Backstage demo application",
        framework="Flask",
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
