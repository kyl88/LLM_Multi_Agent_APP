from ai import ask_aiv2, get_macros
import streamlit as st
from profiles import create_profile,get_notes,get_profile,update_personal_info

st.title("Personal Fitness Tool")

@st.fragment()
def personal_data_form():

  with st.form("personal_data_form"):
        st.header("Personal Data")

        profile = st.session_state.profile

        

        name = st.text_input("Name",value =profile["general"]["name"])  
        age = st.number_input("Age", min_value=0,max_value=120,step=1,value =profile["general"]["age"])
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1, value=float(profile["general"]["weight"])),
        height = st.number_input("Height (cm)", min_value=0.0, max_value=300.0, step=0.1, value=float(profile["general"]["height"])),
        genders =["Male","Female","Other"]
        gender = st.radio("Gender", genders.index(profile["general"].get("gender","Male")))
        activities = ('Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extra Active')
        activity_level = st.selectbox("Activity Level", activities,index=activities.index(profile['general'].get("activity_level","Sedentary")))

        personal_data_submit = st.form_submit_button("Submit")
        if personal_data_submit:
            if all ([name, age, weight, height, gender, activity_level]):
                with st.spinner("Processing..."):
                    update_personal_info(profile,"general",name=name,age=age,weight=weight,height=height,gender=genders[gender],activity_level=activities[activity_level])
                    st.success("Personal data submitted successfully!")
            else:
                st.warning("Please fill in all the fields.")

@st.fragment()
def goals_form():
    profile = st.session_state.profile
    with st.form("goals_form"):
        st.header("Goals")
        goals = st.multiselect("Select your Goals",["Muscle Gain","Weight Loss","Healthier Lifestyle"],default=profile.get("goals",["Muscle Gain"]))

        goals_submit = st.form_submit_button("Submit")
        if goals_submit:
            if goals:
                with st.spinner("Processing..."):
                   st.session_state.profile = update_personal_info(profile,"goals",goals=goals)
                   st.success("Goals updated successfully!")
            else:
                st.warning("Please select at least one goal.")

@st.fragment()
def macros():
    profile = st.session_state.profile
    nutrition = st.container(border=True)
    nutrition.header("Macros")
    if nutrition.button("Generate with AI"):
        result = get_macros(profile.get("general"),profile.get("goals"))
        profile["nutrition"] = result
        nutrition.success("AI has generated the results.")

    with nutrition.form("nutrition_form",border=False): 
        col1,col2,col3,col4 = st.columns(4)   
        with col1:
            calories = st.number_input("Calories",min_value=0,step=1,value=profile["nutrition"].get("calories",0))
        with col2:
            protein = st.number_input("Protein",min_value=0,step=1,value=profile["nutrition"].get("protein",0))
        with col3:
            fat = st.number_input("Fat",min_value=0,step=1,value=profile["nutrition"].get("fat",0))
        with col4:
            carbs = st.number_input("Carbs",min_value=0,step=1,value=profile["nutrition"].get("carbs",0))    

        if st.form_submit_button("Submit"):
            with st.spinner("Processing..."):
                st.session_state.profile = update_personal_info(profile,"nutrition",calories=calories,protein=protein,fat=fat,carbs=carbs)    
                st.success("Information saved")
@st.fragment()
def notes():
    st.subheader("Notes")
    for i, note in enumerate(st.session_state.notes):
        cols = st.columns([5,1])
        with cols[0]:
            st.write(note["text"])
        with cols[1]:
            if st.button("Delete"):
                delete_note(note.get("_id"))
                st.session_state.notes.pop(i)
                st.rerun()
    new_note = st.text_input("Add a new note: ")
    if st.button("Add Note"):
        if new_note:
            note = add_note(new_note, st.session_state.profile_id)
            st.session_state.notes.append(note)
            st.rerun()
@st.fragment()
def ask_ai_func():
    st.subheader("Ask AI")
    user_question = st.text_input("Ask a question:")
    if st.button("Ask AI"):  
        with st.spinner("Processing..."):
            result = ask_aiv2(st.session_state.profile,user_question)
            st.write(result)          
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
    goals_form()
    macros()
    notes()
    ask_ai_func()


if __name__ == "__main__":
    forms()   