import streamlit as st
from datetime import datetime

def calculate_age(year, month, day):
    birth_date = datetime(year, month, day)
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    st.title("Age Calculator")
    st.write("Enter your date of birth to calculate your age:")

    # Input widgets for user to enter their date of birth
    year = st.number_input("Year", min_value=1900, max_value=datetime.today().year, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, step=1)
    day = st.number_input("Day", min_value=1, max_value=31, step=1)

    if st.button("Calculate Age"):
        age = calculate_age(year, month, day)
        st.success(f"Your age is {age} years.")

if __name__ == "__main__":
    main()
