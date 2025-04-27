from crewai import Agent
from langchain_community.chat_models import ChatOllama
schedule_designer = Agent(
    role="Schedule Designer",
    goal="Design a realistic study schedule based on user availability",
    backstory="Balances workloads efficiently to prevent burnout and promote retention.",
    verbose=True,
    llm=ChatOllama(model="ollama/mistral")

)
