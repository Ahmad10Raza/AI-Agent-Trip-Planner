

from TravelAgents import guide_expert, location_expert, planner_expert
from TravelTasks import location_task, guide_task, planner_task
from crewai import Crew, Process
import streamlit as st

# Streamlit UI
st.title("🌍 AI-Powered Trip Planner")
st.markdown("""
💡 **Plan your next trip with AI!**  
Let AI build your dream itinerary including:
- 🏙️ Best Places to Visit
- 🍽️ Local Food & Experiences
- 🧳 Travel Budget & Logistics
""")

# User Inputs
from_city = st.text_input("🏡 From City", "India")
destination_city = st.text_input("✈️ Destination City", "Rome")
date_from = st.date_input("📅 Departure Date")
date_to = st.date_input("📅 Return Date")
interests = st.text_area("🎯 Your Interests", "Sightseeing, food")

# Button logic
if st.button("🚀 Generate Travel Plan"):
    if not from_city or not destination_city or not interests:
        st.error("⚠️ Please fill in all fields.")
    elif date_from > date_to:
        st.error("⚠️ Return date must be after departure date.")
    else:
        st.info("⏳ Preparing your travel plan...")

        # Tasks
        loc_task = location_task(location_expert, from_city, destination_city, date_from, date_to)
        guid_task = guide_task(guide_expert, destination_city, interests, date_from, date_to)
        plan_task = planner_task([loc_task, guid_task], planner_expert, destination_city, interests, date_from, date_to)

        # Crew Setup
        crew = Crew(
            agents=[location_expert, guide_expert, planner_expert],
            tasks=[loc_task, guid_task, plan_task],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

        # Run CrewAI
        result = crew.kickoff()
        result_text = str(result)

        # Output
        st.subheader("✅ Your Travel Itinerary")
        st.markdown(result_text)

        st.download_button(
            label="📥 Download Travel Plan",
            data=result_text,
            file_name=f"Travel_Plan_{destination_city}.txt",
            mime="text/plain"
        )
