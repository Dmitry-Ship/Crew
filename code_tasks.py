from textwrap import dedent
from crewai import Task

class CodeTasks():
	def code_task(self, agent, requirements):
		return Task(description=dedent(f"""You need to implement {requirements}

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
			expected_output="Python code",
			agent=agent
		)

	def review_task(self, agent, requirements):
		return Task(description=dedent(f"""\
			You are helping to implement {requirements}

			Using the code you got, check for errors. Check for logic errors,
			syntax errors, missing imports, variable declarations, mismatched brackets,
			and security vulnerabilities.

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
            expected_output="Python code",
			agent=agent
		)

	def evaluate_task(self, agent, requirements):
		return Task(description=dedent(f"""\
			You are helping to implement {requirements}

			You will look over the code to insure that it is complete and
			does the job that it is supposed to do.

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
            expected_output="full python code, only the python code and nothing else",
			agent=agent,
			output_file='result.py'
		)