from crewai import Task

class CodeTasks():
	def design_task(self, requirements):
		return Task(
			description=f'Design the architecture of the Python application based on the {requirements}', 
			expected_output='A detailed design of the Python application, including the architecture, data structures, and algorithms used.'
		)
	
	def code_task(self, requirements):
		return Task(
			description=f"""You need to implement {requirements} bases on the design.""",
			expected_output="Your Final answer must be the full python code, only the python code and nothing else.",
		)

	def review_task(self):
		return Task(
			description='Review the code for quality and adherence to best practices.', 
			expected_output='Your Final answer must be the full python code, only the python code and nothing else..'
		)
