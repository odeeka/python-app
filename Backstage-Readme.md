# Backstage

npx in this image

```bash
docker pull node:18-bookworm-slim
docker pull node:lts
```

```bash
mkdir backstage-app
pwd ./backstage-app
docker run --rm -p 3000:3000 -ti -v /home/admin_pet/github/python-app/backstage-app:/app -w /app node:18-bookworm-slim bash
apt-get update
apt-get install curl
```

> Note you can run in the container `npx @backstage/create-app@latest`

Configure the `/app/backstage/app-config.yaml` and set the host to `0.0.0.0` for `app`

Run the development server in the `/app/backstage# yarn dev`

Run container with backend exposure:

```bash
docker run --rm -p 3000:3000 -p 7007:7007 -ti -v /home/admin_pet/github/python-app/backstage-app:/app -w /app node:18-bookworm-slim bash

docker run --rm -e AUTH_GITHUB_CLIENT_ID="" -e AUTH_GITHUB_CLIENT_SECRET="" -p 3000:3000 -p 7007:7007 -ti -v /home/admin_pet/github/python-app/backstage-app:/app -w /app node:18-bookworm-slim bash
```

RUN THE BACKSTAGE -> `yarn dev`

Open the WebBrowser on host machine and navigate to `localhost:3000`

## User auth

Make the Github Auth setup

Examples: https://github.com/backstage/backstage/blob/master/packages/catalog-model/examples/acme/team-a-group.yaml

```bash
mkdir catalog/entities -p
nano catalog/entities/users.yaml
```

> Note that you should set this file for configuration -> `catalog` block in `app-config.yaml` file

```yaml
catalog:
  rules:
    - allow: [User, Component, System, API, Resource, Location]
  locations:
    # Local example data, file locations are relative to the backend process, typically `packages/backend`
    - type: file
      target: /app/backstage/catalog/entities/users.yaml
```

Configuration file for creating user object:

```yaml
apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: odeeka
spec:
  profile:
    # Intentional no displayName for testing
    # displayName: Tibor Petroczy
    email: ptibor@netbuild.hu
    picture: https://api.dicebear.com/7.x/avataaars/svg?seed=Leo&backgroundColor=transparent
  memberOf: [development]
```

Similary we can create group object `catalog/entities/groups.yaml`

```yaml
apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: development
  description: Development Team
spec:
  type: team
  profile:
    # Intentional no displayName for testing
    email: dev@example.com
    picture: https://api.dicebear.com/7.x/identicon/svg?seed=Fluffy&backgroundType=solid,gradientLinear&backgroundColor=ffd5dc,b6e3f4
  children: []
```

## Catalog

Create `catalog-info.yaml` in the target application repo.

## TechDocs

https://stackedit.io/app#

Create base folder `docs/index.md`

Integrate the `mkdocs` -> https://example-mkdocs-basic.readthedocs.io/en/latest/#example-project-usage

Copy the `mkdocs.yaml` file from Backstage Github Repo (https://github.com/backstage/backstage/blob/master/mkdocs.yml)

Create the file under root `mkdocs.yaml` and configure it

Create the annotation in `catalog-info.yaml` file for referencing the mkdocs.yaml (techdocs-ref)

```yaml
annotations:
  backstage.io/techdocs-ref: dir:.
```

Need to install the `mkdocs` for Backstage > Check the `/app/backstage/packages/app/src/App.tsx` file and it contains the import `@backstage/plugin-techdocs` ???

Create the config in `app-config.local.yml`

```yaml
techdocs:
  builder: 'local'
  publisher:
    type: 'local'
  generator:
    runIn: local
```

Install the `mkdocs` on the server / container -> [`apt-get install mkdocs`](https://backstage.io/docs/features/techdocs/getting-started)

You have to use the `pip` installation (in the container in /app folder):

```bash
apt-get update && apt-get install -y python3 python3-pip python3-venv
VIRTUAL_ENV=/opt/venv
python3 -m venv $VIRTUAL_ENV
PATH="$VIRTUAL_ENV/bin:$PATH"
pip3 install mkdocs-techdocs-core
```

## Software Catalog

Need to create github token with `repo` and `workflow` permissions:

```bash
docker run --rm -e GITHUB_TOKEN="" -e AUTH_GITHUB_CLIENT_ID="" -e AUTH_GITHUB_CLIENT_SECRET="" -p 3000:3000 -p 7007:7007 -ti -v /home/admin_pet/github/python-app/backstage-app:/app -w /app node:18-bookworm-slim bash
```


Create new repo that is fully deticated for the template -> backstage-software-templates

Add the `Template` location into `app-config.local.yaml` (catalog/locations)

