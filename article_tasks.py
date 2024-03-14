from crewai import Task

class ArticleTasks():
	def research_task(self, agent, topic):
		return Task(
			description=f'Research the latest trends in the {topic} and provide a summary.',
			expected_output=f'A summary of the top 3 trending developments in the {topic} with a unique perspective on their significance.',
			agent=agent
		)

	def write_task(self, agent, topic, file_name):
		return Task(
			description=f'Write an engaging blog post about the {topic}, based on the research analyst’s summary.',
			expected_output=f'A 4-paragraph blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
			agent=agent,
			output_file=f'blog-posts/{file_name}.md'
		)
