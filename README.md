## SRE-Toolkit (fastapi)

### A simple API that contains some sre tools such as password_generator and epoch time converter

Built on Python 3.x, it has Linter and Unit Test

##### Python linter

```bash
$ pylint ./*.py
```

##### Unit Test

```bash
$ pytest test/
```

#### Quickstart Installation (Locally)

##### Manual Installation

Install the `virtualenv` and create new virtualenv in the root folder of the project

```bash
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

##### Docker run

You can also run it directly in docker

```bash
$ docker run -p 8000:8000 -d s7even/sre-toolkit:0.0.2
```

##### docker-compose

Or using docker-compose

```bash
docker-compose up -d
```

#### Kubernetes (Helm) Installation

This project contain the helm chart for you to install it in kubernetes. Create a new file inside the `helm` directory of this repo (example: `demo-values.yaml`) and fill it up with below values

```bash
image:
  repository: s7even/sre-toolkit
  pullPolicy: Always
  # Overrides the image tag whose default is the chart appVersion.
  tag: "0.0.2"

env_vars:
  APP_NAME: "zype-demo"
  DEPLOY_ENV: "demo"
  AUTHOR: "stvn.org@gmail.com"
```

and then deploy the helm chart using below command:

```bash
$ cd sre_toolkit/helm
$ helm install --values=./demo-values.yaml sre-toolkit sre-toolkit
```

Note: The helm chart has the `autoscaling` feature enabled

#### Usage

It has only 2 endpoints

```bash
$ curl http://<API_URL>/tools/password-generator
```
and

```bash
$ curl http://<API_URL>/tools/epoch-to-utc/<EPOCH_TIME>
```

example
```bash
$ curl http://localhost:8000/tools/epoch-to-utc/1630976762
```

To see all the details of the endpoints you can access the `swagger` endpoint on `http://<API_URL>/docs`

#### Monitoring

It has Prometheus monitoring enabled exposed on endpoint `http://<API_URL>/docs`
