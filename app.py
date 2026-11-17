from http.server import BaseHTTPRequestHandler, HTTPServer


PAGE = """<!doctype html>
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
      <p>Your demo Python application is up and running.</p>
    </main>
  </body>
</html>
"""


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path != "/":
            self.send_error(404, "Page not found")
            return

        content = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


def main() -> None:
    address = ("127.0.0.1", 8000)
    with HTTPServer(address, HelloHandler) as server:
        print(f"Serving the Backstage demo at http://{address[0]}:{address[1]}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping the server.")


if __name__ == "__main__":
    main()
