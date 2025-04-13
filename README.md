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
```

> Note that the first port (8080) is the host port and second port (5000) is the container port

Create tags for Dockerhub:

```bash
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

After create load-balancer and ingress for cluster

https://kind.sigs.k8s.io/docs/user/loadbalancer/

## Create Kubernetes manifest for Python app

1) deployment.yaml
2) service.yaml
3) ingress.yaml

Test with webbrowser:

```bash
curl http://localhost/api/v1/details
curl http://localhost/api/v1/healthz
```

## Create Helm

```bash
mkdir charts
helm create python-app
```

> Note you need to modify the files and value.yaml

Install chart

```bash
cd charts/python-app
helm install python-app --create-namespace -n python  .
```

Uninstall chart

```bash
helmy -n python uninstall python-app
```

## Deploy ArgoCD

https://artifacthub.io/packages/helm/argo/argo-cd

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm install argo-cd argo/argo-cd -n argocd --create-namespace --version 7.8.23 -f argocd/values.yaml

helm upgrade argo-cd argo/argo-cd -n argocd --create-namespace --version 7.8.23 -f argocd/values.yaml
```

> Note that you have to create local usser for image updater

Create port-forward and get secret

```bash
kubectl -n argocd port-forward service/argo-cd-argocd-server 8080:443
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo
```

Open webbrowser and navigate to `https://argocd.example.org`

Install ArgoCD image update

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
cd argocd-image-updater
helm install argocd-image-updater argo/argocd-image-updater -n argocd --version 0.12.1 -f values.yaml
```

Generate token for image updater local user

```bash
argocd login argocd.example.org
argocd acocunt list
argocd account generate-token --account image-updater --id image-updater --grpc-web
```

Install image updater CLI

```bash
wget -O argocd-image-updater https://github.com/argoproj-labs/argocd-image-updater/releases/download/v0.16.0/argocd-image-updater-linux_amd64
chmod +x argocd-image-updater
sudo mv argocd-image-updater /usr/local/bin/
```
