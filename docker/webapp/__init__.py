from flask import Flask, Response
from prometheus_client import Summary, Counter, generate_latest, REGISTRY


def create_app():
    app = Flask(__name__)

    # Métrica de tiempo de procesamiento de solicitudes
    REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

    # Métrica de conteo de solicitudes HTTP
    HTTP_REQUESTS_TOTAL = Counter('http_requests_total', 'Total number of HTTP requests')

    @app.route('/')
    @REQUEST_TIME.time()  # Decora la función para medir el tiempo de ejecución
    def hello():
        HTTP_REQUESTS_TOTAL.inc()  # Incrementa el contador de solicitudes
        return 'Hello World!'

    @app.route('/metrics')
    def metrics():
        try:
            # Generar las métricas en formato de texto
            metrics_data = generate_latest(REGISTRY)
            return Response(metrics_data, content_type='text/plain; version=0.0.4; charset=utf-8')
        except Exception as e:
            # Manejo básico de errores
            return Response(f"Error generating metrics: {e}", status=500)

    return app
