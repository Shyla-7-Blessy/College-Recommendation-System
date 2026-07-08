from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
template = """
Student Details

Cutoff: {cutoff}
Caste: {caste}
Eligible Group: {eligible_group}

Recommended Colleges

{colleges}

Explain why these colleges are recommended.
"""

prompt = PromptTemplate(
    input_variables=[
        "cutoff",
        "caste",
        "eligible_group",
        "colleges"
    ],
    template=template
)

chain = prompt | llm


def explain_recommendation(
    cutoff,
    caste,
    eligible_group,
    colleges
):
    try:
        result = chain.invoke({
            "cutoff": cutoff,
            "caste": caste,
            "eligible_group": eligible_group,
            "colleges": colleges
        })

        return result.content

    except Exception as e:
        print("Groq Error:", e)

        return (
            f"The recommended colleges are selected based on "
            f"the student's cutoff ({cutoff}), caste ({caste}), "
            f"and eligible group ({eligible_group})."
        )