import streamlit as st
import pickle
import pandas as pd

# Load the trained model
loaded_model=pickle.load(open('C:/Users/ACER/.spyder-py3/spyder.lock/career_recommendation.pkl','rb'))

# Streamlit app title and description
st.title("Career Recommendation System")
st.write("Discover your potential and take the first step towards your dream career.")
# Sidebar for user input
st.sidebar.header("Input Details")
part_time_job = st.sidebar.checkbox("Part-Time Job")
absence_days = st.sidebar.number_input("Number of Absence Days", min_value=0, max_value=30, value=0)
extracurricular_activities = st.sidebar.checkbox("Extracurricular Activities")
weekly_self_study_hours = st.sidebar.number_input("Weekly Self-Study Hours", min_value=0, value=0)

# Score inputs
st.sidebar.header("Subject Scores")
math_score = st.sidebar.number_input("Math Score", min_value=0, max_value=100, value=0)
history_score = st.sidebar.number_input("History Score", min_value=0, max_value=100, value=0)
physics_score = st.sidebar.number_input("Physics Score", min_value=0, max_value=100, value=0)
chemistry_score = st.sidebar.number_input("Chemistry Score", min_value=0, max_value=100, value=0)
biology_score = st.sidebar.number_input("Biology Score", min_value=0, max_value=100, value=0)
english_score = st.sidebar.number_input("English Score", min_value=0, max_value=100, value=0)
geography_score = st.sidebar.number_input("Geography Score", min_value=0, max_value=100, value=0)

# Button to predict
if st.sidebar.button("Predict Career Aspiration"):
    # Prepare the DataFrame
    data = {
        'part_time_job': part_time_job,
        'absence_days': absence_days,
        'extracurricular_activities': extracurricular_activities,
        'weekly_self_study_hours': weekly_self_study_hours,
        'math_score': math_score,
        'history_score': history_score,
        'physics_score': physics_score,
        'chemistry_score': chemistry_score,
        'biology_score': biology_score,
        'english_score': english_score,
        'geography_score': geography_score
    }

    df = pd.DataFrame([data])
    df['total_score'] = df[['math_score', 'history_score', 'physics_score', 'chemistry_score', 'biology_score', 'english_score', 'geography_score']].sum(axis=1)
    df['average_score'] = df['total_score'] / 7  # number of subjects

    # Make predictions
    predictions = loaded_model.predict(df)

    # Career aspiration mapping
    career_aspiration_map = {
        0: 'Lawyer', 1: 'Doctor', 2: 'Government Officer', 3: 'Artist', 4: 'Social Network Studies',
        5: 'Software Engineer', 6: 'Teacher', 7: 'Business Owner', 8: 'Scientist',
        9: 'Banker', 10: 'Writer', 11: 'Accountant', 12: 'Designer',
        13: 'Construction Engineer', 14: 'Game Developer', 15: 'Stock Investor',
        16: 'Real Estate Developer'
    }

    # Get predicted career aspiration
    predicted_career_aspiration = career_aspiration_map[predictions[0]]

    # Display results
    st.success(f"**Total Score:** {df['total_score'].iloc[0]}")
    st.success(f"**Average Score:** {df['average_score'].iloc[0]:.2f}")
    st.success(f"**Predicted Career Aspiration:** {predicted_career_aspiration}")

    st.write("Feel free to ask us anything! We're here to support you on your path to success.")

