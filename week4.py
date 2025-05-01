from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import List

# ---------- SQLite Setup ----------
SQLALCHEMY_DATABASE_URL = "sqlite:///./jobs.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":
False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# ---------- SQLAlchemy Model ----------
class JobPostingDB(Base):
    __tablename__ = "job_postings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

## create tables if they don't exist
Base.metadata.create_all(bind=engine)

# ---------- Pydantic Models ----------
class JobPost(BaseModel):
    id: int
    name: str


    class Config:
        orm_mode = True

job_posting_db = [
    JobPost(id=1, name="Software Developer"),
    JobPost(id=2, name="Web Developer"),
    JobPost(id=3, name="Web Designer")
]

# ---------- FastAPI APP ----------
app = FastAPI()

# ---------- Routes ----------
@app.get("/job-posting", response_model=List[JobPost])
def read_job_postings():
    with SessionLocal() as session:
        jobs = session.query(JobPostingDB).all()
        return jobs
    
@app.post("/job-posting", response_model=JobPost)
def create_job_posting(job: JobPost):
    with SessionLocal() as session:
        db_job = JobPostingDB(**job.dict())
        session.add(db_job)
        session.commit()
        session.refresh(db_job)
        return db_job
    
@app.delete("/job-posting", response_model=JobPost)
def delete_job_posting(job_id: int):
    with SessionLocal() as session:
        job = session.query(JobPostingDB).filter(JobPostingDB.id == job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job posting not found")
        session.delete(job)
        session.commit()
        return job
