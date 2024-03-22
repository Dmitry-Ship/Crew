import datetime
from crewai import Task

class ArticleTasks():
	def research_task(self, topic):
		return Task(
			description=f'Research the {topic} and provide a summary.',
			expected_output=f'A summary the information about {topic}',
		)

	def write_task(self, topic):
		current_date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
		return Task(
			description=f'Write an engaging blog post about the {topic}, based on the research analyst’s summary.',
			expected_output=f'A 4-paragraph blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
			output_file=f'blog-posts/{current_date_time}.md'
		)
