import streamlit as st
import pandas as pd
import numpy as np

# Create an empty DataFrame
df = pd.DataFrame(columns=['Event', 'Time'])
events = np.empty(19, dtype=object)

# Add a new row to the DataFrame based on user input
def add_event():
    for n in range(19):
        events[n] = st.text_input(f"Event {n+1}")
    time = st.selectbox("Time", ['09:00', '12:30', '15:45'])  # Use a selectbox for time selection

    if st.button("Add"):
        df.loc[len(df)] = [events, time]

# Display the DataFrame as a table in Streamlit
def display_table():
    for i in range(19):
        st.table(df)

# Main Streamlit app
def main():
    st.title("Time Table")
    add_event()
    display_table()

if __name__ == '__main__':
    main()
