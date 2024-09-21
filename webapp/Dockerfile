ARG PYTHON_VERSION=3.20
FROM python:alpine${PYTHON_VERSION} AS build
LABEL Name="WebApp" \
      Version="1.0"
WORKDIR /app
COPY requirements.txt /app/
RUN apk add --no-cache gcc musl-dev libffi-dev libxml2-dev libxslt-dev postgresql-dev curl nano \
      && pip install --upgrade pip \
      && pip install --no-cache-dir -r /app/requirements.txt
FROM python:alpine${PYTHON_VERSION}
WORKDIR /app
COPY --from=build /usr/local /usr/local
COPY . .
ENV PYTHONPATH=/app/web
ENV FLASK_ENV=development
ENV FLASK_APP=web/app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
