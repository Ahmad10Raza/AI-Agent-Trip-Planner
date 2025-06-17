

from crewai import Task

def location_task(agent, from_city, destination_city, date_from, date_to):
    return Task(
        description=f"""
        🇫🇷 In French: Provide travel-related info for {destination_city}, including:
        - Accommodations
        - Cost of living
        - Visa requirements
        - Transportation
        - Weather
        - Local events

        Travel from: {from_city}
        Dates: {date_from} to {date_to}

        Respond in FRENCH if destination is French-speaking.
        """,
        expected_output="📄 A detailed markdown report with relevant travel data.",
        agent=agent,
        output_file='city_report.md',
    )

def guide_task(agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""
        ✈️ Create a travel guide for {destination_city} based on user interests:
        - Interests: {interests}
        - Arrival: {date_from}
        - Departure: {date_to}

        Include:
        - Attractions
        - Food recommendations
        - Local events
        """,
        expected_output="📄 A markdown itinerary with points of interest, food, and activities.",
        agent=agent,
        output_file='guide_report.md',
    )

def planner_task(context, agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""
        🧳 Synthesize all gathered travel information into one cohesive itinerary.

        Include:
        - Introduction to {destination_city} in 4 paragraphs
        - Daily travel plan (timings, locations)
        - Estimated expenses and pro tips

        Interests: {interests}
        Dates: {date_from} to {date_to}
        """,
        expected_output="📄 A full markdown travel plan for the trip.",
        context=context,  # Must be [location_task, guide_task]
        agent=agent,
        output_file='travel_plan.md',
    )
