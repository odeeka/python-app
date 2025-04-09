# python-app

## Create Python virtua env

Demo Python App for Backstage

```bash
cd github/python-app
python3 -m venv .venv

source .venv/bin/activate
```

Install dependencies

```bash
cd github/python-app/
pip3 install -r requirements.txt
```

> Note that this command will install the Python packages into virtual env

Run the Python app

```bash
python3 src/app.py
```

> Note that you can test with curl or web browser

## Create Docker image with Python app

```bash
docker build -t python-app:v1 .
docker run -p 8080:5000 --rm python-app:v1

docker tag python-app:v1 ptibor84/python-app:v1
docker login
docker push ptibor84/python-app:v1
```

## Create Kubernetes cluster with kind

https://kind.sigs.k8s.io/docs/user/quick-start/

Install

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.27.0/kind-linux-amd64
chmod +x kind
sudo mv kind /usr/local/bin
```

Create & reach the K8s (kind) cluster

```bash
kind create cluster

kubectl cluster-info --context kind-kind
kubectl config use-context kind-kind
```
