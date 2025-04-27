from crewai import Agent
from langchain_community.chat_models import ChatOllama

recommendation_agent = Agent(
    role="Movie Recommendation Expert",
    goal="Provide the best movie recommendations",
    backstory="Understands movie quality, popularity, and personal taste alignment.",
    verbose=True,
    llm=ChatOllama(model="ollama/mistral")
)
