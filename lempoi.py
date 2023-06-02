import streamlit as st
import pandas as pd
from numpy import *
import datetime

T = array([str]*19)
D = array([str]*19)
# Sample event data
for i in range(1,19):
    T[i] = st.text_input(f'envent {i} :')
    D[i] = st.date_input(
        "When\'s ?")
    
events = [
    {'Event': st.text_input(""), 'Date': '2023-06-10'},
    {'Event': 'Event 2', 'Date': '2023-06-15'},
    {'Event': 'Event 3', 'Date': '2023-06-20'}
]

# Convert event data to a Pandas DataFrame
df = pd.DataFrame(events)


# Display the table using Streamlit
st.table(df)
