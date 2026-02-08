import structlog
import time
import random
import os

# Initialize a structured logger
log = structlog.get_logger()

def capture_metrics():
    """Simulates capturing system telemetry."""
    return {
        "cpu_usage_percent": round(random.uniform(2.0, 15.0), 2),
        "memory_rss_mb": random.randint(40, 100),
        "active_threads": random.randint(1, 5)
    }

def main():
    log.info("service_initialized", 
             project="observability-project",
             pid=os.getpid(),
             version="0.1.0")

    try:
        while True:
            # Capture simulated telemetry
            metrics = capture_metrics()
            
            # Emit a structured log entry
            log.info("telemetry_heartbeat", **metrics)
            
            # Follow a 5-second pulse
            time.sleep(5)
            
    except KeyboardInterrupt:
        log.info("service_shutdown", reason="manual_interrupt")

if __name__ == "__main__":
    main()