import os
from dotenv import load_dotenv
load_dotenv(override=True)
from crewai import Crew, Process
from code_tasks import CodeTasks
from code_agents import senior_engineer_agent, design_agent, review_agent
from langchain_openai import ChatOpenAI

tasks = CodeTasks()

print("## Welcome to the Code Crew")
print('-------------------------------')
request = input("What would you like to build?\n")

# Create Tasks
design = tasks.design_task(design_agent, request)
code = tasks.code_task(senior_engineer_agent, request)
review = tasks.review_task(review_agent)

# Create Crew responsible for Copy
crew = Crew(
	agents=[
		design_agent,
		senior_engineer_agent,
		review_agent
	],
	tasks=[
		design,
		code,
		review,
	],
	verbose=True,
    manager_llm=ChatOpenAI(temperature=0, model=os.getenv('OPENAI_MODEL_NAME')),
    process=Process.hierarchical,
)

result = crew.kickoff()


# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code:")
print(result)