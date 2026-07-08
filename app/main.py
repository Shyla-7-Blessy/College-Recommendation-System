from fastapi import FastAPI, Request, Form
from sqlalchemy import text
from recommendation.rule_engine import get_eligible_colleges
from recommendation.predictor import rank_colleges
from recommendation.llm_chain import explain_recommendation
from app.database import engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

apps = FastAPI()

templates = Jinja2Templates(directory="templates")

apps.mount("/static", StaticFiles(directory="static"), name="static")
#print(type(templates))
#print(templates)

@apps.get("/")

def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@apps.post("/recommend")
def recommend(
    request: Request,
    student_name: str = Form(...),
    email: str = Form(...),
    percentage: float = Form(...),
    cutoff: float = Form(...),
    caste: str = Form(...),
    eligible_group: str = Form(...)
):
    with engine.connect() as conn:

        conn.execute(
            text("""
            INSERT INTO student_profiles
            (
                student_name,
                email,
                percentage,
                cutoff,
                caste,
                eligible_group
            )
            VALUES
            (
                :student_name,
                :email,
                :percentage,
                :cutoff,
                :caste,
                :eligible_group
            )
            """),
            {
                "student_name": student_name,
                "email": email,
                "percentage": percentage,
                "cutoff": cutoff,
                "caste": caste,
                "eligible_group": eligible_group
            }
        )

        conn.commit()


    eligible = get_eligible_colleges(
        cutoff,
        caste,
        eligible_group
    )

    top_colleges = rank_colleges(
        eligible
    )

    print(type(top_colleges))
    print(top_colleges)
    
    if len(top_colleges) == 0:
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "message": "No colleges found."
            }
        )
    
    explanation = explain_recommendation(
        cutoff=cutoff,
        caste=caste,
        eligible_group=eligible_group,
        colleges=top_colleges.to_dict(orient="records")
    )

    print(type(top_colleges))
    print(top_colleges)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "student_name": student_name,
            "recommendations": top_colleges.to_dict(orient="records"),
            "explanation": explanation
        }
    )
