from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

# 🧠 1. Tool: Web Search Tool (Serper.dev API)
search_tool = SerperDevTool()

# 👤 2. Agent Definition
web_researcher = Agent(
    role='Web Researcher',
    goal='Find accurate and recent information from the internet',
    backstory='You are a skilled internet researcher, specialized in finding factual data from trusted sources.',
    tools=[search_tool],
    verbose=True
)

# 🎯 3. Task assigned to the agent
research_task = Task(
    description='Search and summarize the latest news about Artificial Intelligence.',
    expected_output='A short summary of the top recent news in AI.',
    agent=web_researcher
)

# 🤖 4. Assemble Crew and Run
crew = Crew(
    agents=[web_researcher],
    tasks=[research_task],
    verbose=True
)

# 🚀 5. Kick off the task and print result
result = crew.kickoff()
print("\n🔎 Final Output:\n", result)
