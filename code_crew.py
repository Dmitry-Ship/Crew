from dotenv import load_dotenv
load_dotenv(override=True)
from crewai import Crew
from code_tasks import CodeTasks
from code_agents import senior_engineer_agent, qa_engineer_agent, chief_qa_engineer_agent

tasks = CodeTasks()

print("## Welcome to the Code Crew")
print('-------------------------------')
request = input("What would you like to build?\n")

# Create Tasks
code = tasks.code_task(senior_engineer_agent, request)
review = tasks.review_task(qa_engineer_agent, request)
approve = tasks.evaluate_task(chief_qa_engineer_agent, request)

# Create Crew responsible for Copy
crew = Crew(
	agents=[
		senior_engineer_agent,
		qa_engineer_agent,
		chief_qa_engineer_agent
	],
	tasks=[
		code,
		review,
		approve
	],
	verbose=True
)

result = crew.kickoff()


# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code:")
print(result)