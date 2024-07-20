from prometheus_client import start_http_server, Summary

# Crear una métrica de resumen para tiempos de ejecución
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

def init_metrics_server():
    # Iniciar el servidor para exponer las métricas en el puerto 8000
    start_http_server(8000)
    print("Metrics server started on port 8000")
