import os
from crewai import Agent, Task, Crew
from crewai_tools import  PDFSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

DOCUMENT_PATH = os.environ.get("DOCUMENT_PATH")
pdf_search = PDFSearchTool(pdf=DOCUMENT_PATH)

retriever = Agent(
  role='Retriever',
  goal='Retrieve information from the PDF',
  backstory="Your task is to retrieve information from the PDF.",
  verbose=True,
  allow_delegation=False,
  tools=[pdf_search],
)

query = input("Enter your query: ")

task1 = Task(
  description=query,
  expected_output="2-3 sentences",
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