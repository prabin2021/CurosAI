from crewai import Agent
from langchain.chat_models import ChatOpenAI

recommendation_agent = Agent(
    role="Movie Recommendation Expert",
    goal="Provide the best movie recommendations",
    backstory="Understands movie quality, popularity, and personal taste alignment.",
    verbose=True,
    llm=ChatOpenAI(temperature=0.7, model="gpt-4")
)
