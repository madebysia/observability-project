# Observability Project | Python Telemetry Suite

Core implementation of the observability stack focusing on the **MELT** (Metrics, Events, Logs, Traces) capability model. This project provides the instrumentation layer for the specifications defined in `O11y-Architecture`.

---

## 🏗 Technical Specifications
* **Runtime:** Python 3.10+ (via `uv` managed environments)
* **Standard:** OpenTelemetry (OTLP) 1.2+ compliant
* **Package Management:** [uv](https://github.com/astral-sh/uv)
* **Serialization:** Protocol Buffers (protobuf) for high-efficiency data transport

## 🛠 Project Components
| Component | Function | Implementation |
| :--- | :--- | :--- |
| **Collector** | Data Aggregation | OTel Collector / Prometheus Scraper |
| **Processor** | Data Transformation | Custom Python Middlewares |
| **Exporter** | Data Egress | OTLP/gRPC to Backend |

## 🚀 Local Development Environment

### 1. Project Initialization
Using `uv` for lightning-fast environment synchronization:
```bash
# Sync environment and install dependencies from uv.lock
uv sync

# Or, to manually add the core telemetry stack
uv add opentelemetry-api opentelemetry-sdk structlog

Maintained by: Sia | Version: 0.1.0