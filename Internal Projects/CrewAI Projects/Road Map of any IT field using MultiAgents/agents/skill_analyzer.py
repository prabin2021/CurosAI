
from crewai import Agent
from langchain_community.chat_models import ChatOllama

  # Use 'mistral' or another supported model
skill_analyzer = Agent(
    role="Skill Analyzer",
    goal="Analyze the user's current knowledge and learning goal",
    backstory="An expert in understanding learners' needs and mapping out prerequisite knowledge.",
    verbose=True,
    llm=ChatOllama(model="ollama/mistral")
)
