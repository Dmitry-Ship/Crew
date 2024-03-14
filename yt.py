from crewai import Agent, Task, Crew
from crewai_tools import YoutubeVideoSearchTool
from dotenv import load_dotenv
load_dotenv()

tool = YoutubeVideoSearchTool()

retriever = Agent(
  role='Retriever',
  goal='Retrieve information from the video',
  backstory="You retrieve infromation from the video",
  verbose=True,
  allow_delegation=False,
  tools=[tool],
)

# query = input("Enter your query: ")

task1 = Task(
  description="list all the book mentioned in this video with a very short summary for each of them",
  expected_output="Build a list",
  agent=retriever
)

crew = Crew(
  agents=[retriever],
  tasks=[task1],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("######################")
print(result)