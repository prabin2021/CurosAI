from crewai import Task
from agents.skill_analyzer import skill_analyzer
from agents.curriculum_builder import curriculum_builder
from agents.resource_recommender import resource_recommender
from agents.schedule_designer import schedule_designer

def get_tasks(user_query):
    task1 = Task(
        description=f"Analyze this learning goal: '{user_query}' and extract prior knowledge, goal, and time constraints.",
        agent=skill_analyzer,
        input_type = dict,
        expected_output="A structured analysis including:\n- Prior Knowledge: [List of topics or skills the user is expected to know before starting].\n- Goal: [The specific learning goal as stated by the user].\n- Time Constraints: [Any specific deadlines or time limits for the learning process].",
    )

    task2 = Task(
        description="Based on the analysis, create a weekly learning plan (12 weeks).",
        agent=curriculum_builder,
        context=[task1],
        input_type = dict,
        expected_output="A detailed 12-week curriculum plan that aligns with the user’s learning goal, broken down by weeks with topics and objectives.",
    )

    task3 = Task(
        description="For each week’s goal, recommend 1-2 high-quality learning resources (courses, articles, etc).",
        agent=resource_recommender,
        context=[task2],
        input_type = dict,
        expected_output="A list of recommended resources (courses, articles, videos, etc.) for each week’s goal. 1-2 resources per week.",
    )

    task4 = Task(
        description="Create a weekly and daily study schedule, respecting the user’s availability.",
        agent=schedule_designer,
        context=[task3],
        input_type = dict,
        expected_output="A weekly and daily study schedule that respects the user’s availability, breaking down study tasks, including time slots and durations for each activity."
    )

    return [task1, task2, task3, task4]
