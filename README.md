# SRE Skills Up

![alt text][diagram]

## Clone the repo to your local infra

``` git
git clone --recursive --depth=1 https://github.com/OMaciasd/sre_skills_up.git; cd .\sre_skills_up\;
```

## Publish the App Docker Images

### First: Setting .env

``` .env
grafana_PASSWORD=grafana
POSTGRES_PASSWORD=your_postgres_password
GRAFANA_ADMIN_PASSWORD=your_grafana_admin_password
```

### Second: Build the docker project

``` go
docker-compose up -d --scale python-microservice=3
```

## Validate App observability

### First: Validate Prometheus targets

``` bash
curl http://localhost:9090/targets?search=
```

![alt text][web]

### Second: Validate Grafana's dashboard

![alt text][grafana]

#### I´m Sorry for the late, Thank's for you account me

#### Any question, My WhatsApp account: +57 305 828 8031

[web]: assets/images/web.png
[diagram]: assets/images/diagram.png
[grafana]: assets/images/grafana.png
