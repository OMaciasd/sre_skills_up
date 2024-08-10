# Docker Rapid Scaling Lab

![alt text][diagram]

## Clone the repo to your local infra

``` git
git clone --recursive --depth=1 https://github.com/OMaciasd/Docker_Rapid_Scaling_Lab.git; cd .\Docker_Rapid_Scaling_Lab\;
```

## Publish the App Docker Images

### First: Build the image with your respective last tag version

``` go
docker build -t omaciasd/python-microservice:last .
docker images
```

### Analize: Actual vulnebaribilities

``` go
docker scout cves python-microservice:last
```

![alt text][docker]

### Second: Login into Docker Hub Platfform

``` go
docker login
docker push omaciasd/python-microservice:v0.0.7
```

![alt text][hub]

### Validate Actual image

``` go
docker pull omaciasd/python-microservice:last
docker-compose up -d --scale python-microservice=3
```

## Build the App, by Kubernetes with the next commands, over the root folder

### First: Create the prerequesites over the node

``` go
kubectl create namespace tech-prod
kubectl apply -f service.yaml
kubectl apply -f networkpolicy.yaml
```

### Second: Validate, and Run the deployment

``` go
kubectl apply -f deployment.yaml -n tech-prod --dry-run=client
kubectl apply -f deployment.yaml -n tech-prod
```

### Validate Builded Infra

``` go
kubectl get deployments -n tech-prod
kubectl get pods -n tech-prod
```

### Validate manifiest replics

``` go
minikube service python-microservice -n tech-prod
kubectl delete pods -l app=python-microservice -n tech-prod
kubectl get pods -n tech-prod
```

![alt text][web]

![alt text][kubernetes]

## For the next files, I don´t have any account or labs for run  and validate the goals

### First: From Azure DevOps (Pipelines), import the CI file (azure-pipelines.yaml), fro evaluate yhe build of the Artifact

### Second: Also for CloudFlare, evaluate the worker

### Third: ...And, with Grafana, use the json file as a Diagram in a Dashboard, equal for Prometeus in the monitoring with the yaml file

#### I´m Sorry for the late, Thank's for you account me

#### Any question, My WhatsApp account: +57 305 828 8031

[docker]: assets/images/docker.png
[hub]: assets/images/hub.png
[web]: assets/images/web.png
[diagram]: assets/images/diagram.png
[kubernetes]: assets/images/kubernetes.png
