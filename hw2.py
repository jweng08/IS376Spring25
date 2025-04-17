#API for job posting list object
from fastapi import FastAPI

app = FastAPI()

job_postings_list = []

@app.get("/")
async def root():
    return {"message": "Hello, please enter a valid endpoint: /job-posting"}

@app.post("/job-posting")
async def add_string(job_posting: str = ""):
    job_postings_list.append(job_posting)
    return {"A new job posting just added": job_posting}

@app.delete("/job-posting")
async def del_string(job_posting: str = ""):
    if len(job_postings_list > 0):
        job_postings_list.pop(-1)
    return {"Job Posting List: ": job_postings_list}

@app.get("/job-posting")
async def get_string():
    return {"Job Posting List": job_postings_list}

#API for resume list object
from fastapi import FastAPI

app = FastAPI()

resume_list = []

@app.get("/")
async def root():
    return {"message": "Hello, please enter a valid endpoint: /resume"}

@app.post("/resume")
async def add_string(resume: str = ""):
    resume_list.append(resume)
    return {"We have a new resume"}

@app.delete("/resume")
async def del_string(resume: str = ""):
    if len(resume_list > 0):
        resume_list.pop(-1)
    return {"Resume List: ": resume_list}


@app.get("/resume")
async def get_string():
    return {"Resume List: ": resume_list}


#API for resume list object
@app.post("/optimized-resume")
async def add_optimized_resume(optimized_resume: str = ""):
    optimized_resume_list.append(optimized_resume)
    return {"Optimized a resume: ": optimized_resume}

@app.delete("/optimized-resume")
async def del_optimized_resume(optimized_resume: str = ""):
    if len(optimized_resume_list) > 0:
        optimized_resume_list.pop(-1)
    return {"Optimized resumes: ": optimized_resume_list}

@app.get("/optimized-resume")
async def get_optimized_resume():
    return {"Optimized resumes: ": optimized_resume_list}
