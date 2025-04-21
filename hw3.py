from fastapi import FastAPI, HTTPException
import openai

app = FastAPI()

openai.api_key = "example"

job_postings_list = []

@app.get("/")
async def root():
    return {"message": "Hello, please enter a valid endpoint: /resume, /optimized-resume, or /job-posting"}

@app.post("/job-posting")
async def add_string(job_posting: str = ""):
    job_postings_list.append(job_posting)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Suggest 2 similar job titles for this job posting: {job_posting}"}
            ]
        )
        suggestions = response['choices'][0]['message']['content']
        
        return {
            "Added Job Posting": job_posting,
            "AI Suggestions": suggestions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/job-posting")
async def del_string(job_posting: str = ""):
    if len(job_postings_list > 0):
        job_postings_list.pop(-1)
    return {"Job Posting List: ": job_postings_list}

@app.get("/job-posting")
async def get_string():
    return {"Job Posting List": job_postings_list}
