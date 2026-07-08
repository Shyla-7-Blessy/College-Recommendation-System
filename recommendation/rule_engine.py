from fastapi import FastAPI
from sqlalchemy import text
from fastapi import HTTPException

from app.database import engine

def get_eligible_colleges(cutoff: float, caste: str, eligible_group: str):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(
                    """select 
                        c.college_name,
                        c.city,
                        c.college_tier,
                        c.nirf_rank,
                        c.accreditation,
                
                        co.course_name,
                        co.degree_type,
                        co.top_job_roles,
                
                        cc.annual_fees,
                        cc.total_seats,
                        cc.min_cutoff
               
                    from colleges c
               
                    join college_courses cc
                     on c.college_id = cc.college_id
            
                    join courses co
                     on cc.course_id = co.course_id
                    
            
                    where 
               
                     lower(cc.eligible_caste) = lower(:caste)

                     and lower(co.eligible_groups) = lower(:eligible_group)

                     and :cutoff  >= cc.min_cutoff
               
                    order by 
                     c.nirf_rank asc nulls last,
                     cc.min_cutoff desc
               
                    """),
                {
                "caste": caste,
                "cutoff": cutoff,
                "eligible_group": eligible_group
                }
            )

            recommendations = [
                dict(row._mapping)
                for row in result
            ]
        return recommendations
    
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))
            
