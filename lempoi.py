import streamlit as st
import pandas as pd
import datetime

# Sample event data

events = [
    {'Event':ev1 = text_input("") , 'Date': '2023-06-10', 'Location': 'City A'},
    {'Event': 'Event 2', 'Date': '2023-06-15', 'Location': 'City B'},
    {'Event': 'Event 3', 'Date': '2023-06-20', 'Location': 'City C'}
]

# Convert event data to a Pandas DataFrame
df = pd.DataFrame(events)

# Display the table using Streamlit
st.table(df)
