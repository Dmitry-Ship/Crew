from crewai import Agent, Task, Crew
from crewai_tools import PDFSearchTool
from dotenv import load_dotenv
load_dotenv()

pdf_search = PDFSearchTool()

retriever = Agent(
  role='Retriever',
  goal='Retrieve information from the PDF, using synomis if needed',
  backstory="You can reformulate user query to get more relevant information from the PDF",
  verbose=True,
  allow_delegation=False,
  tools=[pdf_search],
)

query = input("Enter your query: ")

retieve = Task(
  description=query,
  expected_output="Answer that can be understood by someone who never read this PDF",
  agent=retriever
)

crew = Crew(
  agents=[retriever],
  tasks=[retieve],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("######################")
print(result)