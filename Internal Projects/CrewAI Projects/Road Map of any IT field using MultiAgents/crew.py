from crewai import Crew
from tasks.learning_tasks import get_tasks

def run_crew(user_input):
    tasks = get_tasks(user_input)
    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        verbose=True
    )
    return crew.kickoff()
