from client.rq_client import queue as wq
from rqueue.worker import process_query

from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/health")
def check_system_health():
    return {"status": "ok"}

@app.post("/chat")
def chat_input(query: str = Query(..., description="User chat query")):
    job = wq.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}

@app.get("/job-res")
def get_resByJobId(job_id: str = Query(..., description="job id")):
    job = wq.fetch_job(job_id=job_id)
    res = job.return_value()
    return {"message": res}