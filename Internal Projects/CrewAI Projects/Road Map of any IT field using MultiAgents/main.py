from dotenv import load_dotenv
load_dotenv()

from crew import run_crew

if __name__ == "__main__":
    user_input = input("Describe your learning goal (e.g., 'Become a full-stack dev in 3 months'):\n> ")
    result = run_crew(user_input)
    print("\nYour Personalized Learning Path:\n")
    print(result)
