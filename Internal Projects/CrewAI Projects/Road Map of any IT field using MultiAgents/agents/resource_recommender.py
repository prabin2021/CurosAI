from crewai import Agent
from langchain_community.chat_models import ChatOllama

resource_recommender = Agent(
    role="Resource Recommender",
    goal="Find the best online resources for each milestone",
    backstory="Knows where to find the best up-to-date courses, articles, and tutorials.",
    verbose=True,
    llm=ChatOllama(model="ollama/mistral")
    
)
