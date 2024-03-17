from textwrap import dedent
from crewai import Agent
from langchain_community.tools import human

design_agent = Agent(
    role='Software Architect',
    goal='Design the architecture of the Python application',
    backstory='Skilled in designing scalable and maintainable software architectures, with a deep understanding of Python.',
    # tools=[human.HumanInputRun()],
	allow_delegation=False,
    verbose=True
)

senior_engineer_agent = Agent(
	role='Senior Software Engineer',
	goal='Create software as needed',
	backstory=dedent("""\
		You are a Senior Software Engineer at a leading tech think tank.
		Your expertise in programming in python. and do your best to
		produce perfect code"""),
	allow_delegation=False,
	verbose=True,
)

review_agent = Agent(
    role='Code Reviewer',
    goal='Ensure the code is of high quality and meets best practices',
    backstory='Detail-oriented and quality-focused, with extensive experience in code review and software quality assurance.',
    verbose=True
)