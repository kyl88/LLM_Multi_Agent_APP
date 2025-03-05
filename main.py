import streamlit as st
from profiles import create_profile,get_notes,get_profile

st.title("Personal Fitness Tool")

@st.fragment()
def personal_data_form():

  with st.form("personal_data_form"):
        st.header("Personal Data")

        profile = st.session_state.profile

        

        name = st.text_input("Name",value =profile["general"]["name"])  
        age = st.number_input("Age", min_value=0,max_value=120,step=1,value =profile["general"]["age"])
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1, value=profile["general"]["weight"])
        height = st.number_input("Height (cm)", min_value=0.0, max_value=300.0, step=0.1, value=profile["general"]["height"])
        genders =["Male","Female","Other"]
        gender = st.radio("Gender", genders.index(profile["general"].get("gender","Male")))
        activities = ('Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extra Active')
        activity_level = st.selectbox("Activity Level", activities,index=activities.index(profile['general'].get("activity_level","Sedentary")))

        personal_data_submit = st.form_submit_button("Submit")
        if personal_data_submit:
            if all ([name, age, weight, height, gender, activity_level]):
                with st.spinner("Processing..."):
                    st.success("Personal data submitted successfully!")
            else:
                st.warning("Please fill in all the fields.")

def forms():
    if "profile" not in st.session_state:
        profile_id =1
        profile = get_profile(profile_id)
        if not profile:
            profile_id, profile = create_profile(profile_id)
        st.session_state.profile = profile
        st.session_state.profile_id = profile_id

    if "notes" not in st.session_state:
        st.session_state.notes = get_notes(st.session_state.profile_id)


    personal_data_form()


if __name__ == "__main__":
    forms()   