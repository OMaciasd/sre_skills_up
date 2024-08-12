ARG PYTHON_VERSION=3.19
FROM python:alpine${PYTHON_VERSION} AS build
LABEL Name="WebApp" \
      Version="1.0"
WORKDIR /app
COPY webapp /app/webapp
RUN apk add --no-cache gcc musl-dev libffi-dev libxml2-dev libxslt-dev postgresql-dev curl \
      && pip install --upgrade pip \
      && pip install --no-cache-dir --prefix=/install -r /app/webapp/requirements.txt
FROM python:alpine${PYTHON_VERSION}
WORKDIR /app
COPY --from=build /install /usr/local
COPY webapp /app/webapp
ENV PYTHONPATH=/app
ENV FLASK_ENV=development
ENV FLASK_APP=webapp.__init__:create_app
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
