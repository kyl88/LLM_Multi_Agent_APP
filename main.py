import streamlit as st

st.title("Personal Fitness Tool")

@st.fragment()
def personal_data_form():

  with st.form("personal_data_form"):
        st.header("Personal Data")

        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0,max_value=120,step=1)
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=0.0, max_value=300.0, step=0.1)
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        activities = ('Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extra Active')
        activity_level = st.selectbox("Activity Level", activities)

        personal_data_submit = st.form_submit_button("Submit")
        if personal_data_submit:
            if all ([name, age, weight, height, gender, activity_level]):
                with st.spinner("Processing..."):
                    st.success("Personal data submitted successfully!")
            else:
                st.warning("Please fill in all the fields.")

def forms():
    personal_data_form()


if __name__ == "__main__":
    forms()   