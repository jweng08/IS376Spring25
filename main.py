from fastapi import FastAPI

app = FastAPI()

job_list = [1,2,3]

@app.get("/jobs")
async def get_strings():
    return {"jobs": job_list}

@app.post("/jobs")
async def add_string(name: str = ""):
    job_list.append(name)
    return {"jobs": job_list}

@app.delete("/jobs")
async def delete_string(index: int = 0):
    job_list.pop(index)
    return {"jobs": job_list}
