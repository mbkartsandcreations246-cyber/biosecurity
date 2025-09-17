import streamlit as st

# Title
st.set_page_config(page_title="Farm Biosecurity Portal", layout="centered")
st.title("🐓🐖 Digital Farm Biosecurity Portal 🐖🐓")
st.write("Check your farm's biosecurity risk and get best practice guidelines.")

# Questions
questions = [
    "Do you allow outsiders inside your farm?",
    "Do you disinfect equipment regularly?",
    "Do you keep poultry/pigs separate from other animals?",
    "Do you record farm visitors?",
    "Do you vaccinate your animals on schedule?"
]

# Collect answers
st.subheader("📋 Risk Assessment Questionnaire")
answers = []
for q in questions:
    ans = st.radio(q, ["Yes", "No"], key=q)
    answers.append(ans)

# Submit button
if st.button("✅ Submit Answers"):
    risk_score = 0
    for i, ans in enumerate(answers):
        if i == 0:  # outsiders in farm = bad
            if ans == "Yes":
                risk_score += 1
        else:  # other practices should be YES
            if ans == "No":
                risk_score += 1

    # Show result
    if risk_score == 0:
        st.success("Low Risk ✅ Your farm follows strong biosecurity.")
    elif risk_score <= 2:
        st.warning("Medium Risk ⚠️ You need to improve some practices.")
    else:
        st.error("High Risk 🚨 Urgent improvements needed!")

# Guidelines button
if st.button("📘 View Guidelines"):
    st.info("""
    🐓🐖 Biosecurity Guidelines:
    1. Limit visitors inside your farm.  
    2. Disinfect water, feed, and equipment regularly.  
    3. Keep poultry/pigs away from other animals.  
    4. Maintain visitor and vaccination records.  
    5. Report unusual sickness immediately.  

    ✅ Healthy animals = Healthy farm!
    """)
