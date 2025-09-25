from prometheus_client import start_http_server, Counter, Histogram
import time, random

builds_total = Counter('github_builds_total', 'Total number of builds', ['status'])
build_duration = Histogram('github_build_duration_seconds', 'Build duration in seconds')

def simulate_build():
    start = time.time()
    duration = random.uniform(1, 3)   # build time
    time.sleep(duration)
    status = random.choice(["success", "failure"])
    builds_total.labels(status=status).inc()
    build_duration.observe(time.time() - start)

if __name__ == "__main__":
    start_http_server(8000)  # exposes /metrics
    while True:
        simulate_build()
        time.sleep(5)
