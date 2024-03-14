from crewai import Agent, Crew
from crewai_tools import (
    WebsiteSearchTool
)
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from article_tasks import ArticleTasks

load_dotenv()
search_tool = DuckDuckGoSearchRun() 
web_rag_tool = WebsiteSearchTool()

researcher = Agent(
    role='Researcher',
    goal='Provide up-to-date analysis',
    backstory='An expert analyst with a keen eye for trends.',
    tools=[search_tool, web_rag_tool],
    allow_delegation=False,
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Craft engaging blog posts',
    backstory='A skilled writer',
    verbose=True
)

topic = input("Enter a topic: ")
file_name = input("Enter file name: ")

tasks = ArticleTasks()
research = tasks.research_task(researcher, topic)
write = tasks.write_task(writer, topic, file_name)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=2
)

crew.kickoff()