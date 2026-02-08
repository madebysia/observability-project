import structlog
import time
import random
import uuid # For a unique, anonymous ID

# Initialize a structured logger
log = structlog.get_logger()

# Generate a random, non-personal ID for this session
NODE_ID = f"node-{uuid.uuid4().hex[:8]}"

def capture_metrics():
    return {
        "cpu_usage_percent": round(random.uniform(2.0, 15.0), 2),
        "memory_rss_mb": random.randint(40, 100),
    }

def main():
    # Use generic identifiers only
    log.info("service_initialized", 
             node_id=NODE_ID,
             os_type="posix", 
             status="isolated")

    try:
        while True:
            metrics = capture_metrics()
            log.info("telemetry_heartbeat", node_id=NODE_ID, **metrics)
            time.sleep(5)
    except KeyboardInterrupt:
        log.info("service_shutdown")

if __name__ == "__main__":
    main()