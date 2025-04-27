from crewai import Agent
from langchain_community.chat_models import ChatOllama

curriculum_builder = Agent(
    role="Curriculum Builder",
    goal="Break down the learning goal into weekly milestones",
    backstory="Specializes in creating effective, goal-oriented learning curriculums.",
    verbose=True,
    llm=ChatOllama(model="ollama/mistral")
)
