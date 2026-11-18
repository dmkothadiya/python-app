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

- `GET /api/v1/healthz` returns `{"status":"ok"}` when the app is running.
- `GET /api/v1/details` returns the app name, description, and framework as JSON.

## Build and publish with GitHub Actions

The workflow in `.github/workflows/dockerhub.yml` builds the image for pull requests to `main`. On pushes to `main` and version tags such as `v1.0.0`, it also publishes the image to Docker Hub as `dmkothadiya/python-app`, with branch/tag, commit SHA, and (for `main`) `latest` tags.

Add these repository secrets in **GitHub → Settings → Secrets and variables → Actions**:

- `DOCKERHUB_USERNAME`: your Docker Hub username.
- `DOCKERHUB_TOKEN`: a Docker Hub access token with permission to push to `dmkothadiya/python-app`.

If your Docker Hub namespace is different, update `images` in the workflow to match it.

## Kubernetes

The app Deployment, Service, and Ingress are in the `default` namespace. Build the image and make it available to your cluster:

```powershell
docker build -t python-app:latest -f dockerfile .
```

Install the official F5 NGINX Ingress Controller Helm chart in the `ingress` namespace, then apply the app manifests to `default`:

```powershell
helm upgrade --install nginx-ingress oci://ghcr.io/nginx/charts/nginx-ingress --version 2.8.1 --namespace ingress --create-namespace --skip-crds --set controller.enableCustomResources=false --set controller.appprotect.enable=false --set controller.appprotectdos.enable=false
kubectl apply -n default -f k8s\app.yaml
```

The chart creates the `nginx` IngressClass. The Ingress routes `http://python-app.localhost` to the app. Helm is available from the official [Helm installation guide](https://helm.sh/docs/intro/install/); the controller chart and installation instructions are maintained by [F5 NGINX](https://docs.nginx.com/nginx-ingress-controller/install/helm/open-source/).
python-app
