import os
from crewai import Agent, Crew, Process
from crewai_tools import WebsiteSearchTool, YoutubeVideoSearchTool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from article_tasks import ArticleTasks

load_dotenv()
wrapper = DuckDuckGoSearchAPIWrapper()
search_tool = DuckDuckGoSearchResults(api_wrapper=wrapper)
web_rag_tool = WebsiteSearchTool()
yt_rag_tool = YoutubeVideoSearchTool()

researcher = Agent(
    role='Researcher',
    goal='Provide up-to-date analysis',
    backstory='An expert analyst',
    tools=[search_tool, web_rag_tool, yt_rag_tool],
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Craft engaging blog posts',
    backstory='A skilled writer',
    verbose=True
)

topic = input("Enter a topic: ")

tasks = ArticleTasks()
research = tasks.research_task(topic)
write = tasks.write_task(topic)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=2,
    manager_llm=ChatOpenAI(temperature=0, model=os.getenv('OPENAI_MODEL_NAME')),
    process=Process.hierarchical,
)

crew.kickoff()