

from crewai import Agent, LLM
from TravelTools import search_web_tool

# ✅ Initialize Ollama LLM once and reuse
ollama_llm = LLM(
    model="ollama/llama3",
    base_url="http://localhost:11434"
)

# ✅ Agents
guide_expert = Agent(
    role="City Local Guide Expert",
    goal="Provide detailed suggestions on things to do in a city based on user interests.",
    backstory="A local expert passionate about sharing hidden gems and must-see attractions in their city.",
    #tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=ollama_llm,
    allow_delegation=False,
)

location_expert = Agent(
    role="Travel Trip Expert",
    goal="Offer reliable information on how to get from one city to another, travel routes, transport options, and safety tips.",
    backstory="A seasoned traveler with deep knowledge of travel logistics.",
    #tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=ollama_llm,
    allow_delegation=False,
)

planner_expert = Agent(
    role="Travel Planning Expert",
    goal="Compile travel details into a seamless and personalized travel plan for the user.",
    backstory="An expert planner known for creating fun, practical, and efficient travel itineraries.",
    #tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=ollama_llm,
    allow_delegation=False,
)
