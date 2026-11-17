# python-app

A tiny Flask application that serves a simple “Hello, Backstage!” page.

## Run

Requires Python 3. Install dependencies from this directory:

```powershell
python -m pip install -r requirements.txt
python src\app.py
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. Press `Ctrl+C` in the terminal to stop the server.

## API endpoints

- `GET /health` returns `{"status":"ok"}` when the app is running.
- `GET /details` returns the app name, description, and framework as JSON.
python-app
