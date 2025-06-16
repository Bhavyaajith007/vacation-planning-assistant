
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI


load_dotenv()

def get_vacation_plan(destination: str, days: int, interests: str) -> str:
    template = (
        "Create a detailed {days}-day vacation plan for {destination}. "
        "The traveler is interested in: {interests}. "
        "Include things like local experiences, food, timing, and logistics."
    )
    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    

    prompt = f"Create a {days}-day vacation itinerary for {destination}. The person is interested in {interests}."
    return llm.predict(prompt)

