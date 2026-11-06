from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import make_asgi_app, Counter, Histogram
import random
import time

app = FastAPI(title="FinTech Transaction Scoring API")

# Prometheus Metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

TRANSACTION_COUNT = Counter('transactions_total', 'Total transactions processed', ['status'])
PROCESSING_TIME = Histogram('transaction_processing_seconds', 'Time spent processing transaction')

class PaymentRequest(BaseModel):
    card_id: str
    amount: float

@app.post("/process-payment")
def process_payment(request: PaymentRequest):
    start_time = time.time()
    
    # Simulate processing delay
    time.sleep(random.uniform(0.01, 0.1))
    
    # Mock approval logic
    status = "approved" if random.random() > 0.1 else "declined"
    
    TRANSACTION_COUNT.labels(status=status).inc()
    PROCESSING_TIME.observe(time.time() - start_time)
    
    return {"status": status, "transaction_amount": request.amount}
