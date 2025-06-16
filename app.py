import streamlit as st
from planner import get_vacation_plan

st.title("🌴 Vacation Planning Assistant")
destination = st.text_input("Enter your dream destination:")
days = st.slider("How many days do you plan to stay?", 1, 30, 7)
interests = st.text_area("What are your interests? (e.g., beaches, museums, adventure sports)")

if st.button("Generate Plan"):
    if destination and interests:
        with st.spinner("Planning your trip..."):
            plan = get_vacation_plan(destination, days, interests)
            st.success("Here's your vacation plan!")
            st.markdown(plan)
    else:
        st.warning("Please fill in all the fields.")
