import streamlit as st
import pandas as pd

# Sample event data
events = [
    {'Event': 'Event 1', 'Date': '2023-06-10'},
    {'Event': 'Event 2', 'Date': '2023-06-15'),
    {'Event': 'Event 3', 'Date': '2023-06-20'}
]

# Convert event data to a Pandas DataFrame
df = pd.DataFrame(events)


# Display the table using Streamlit
st.table(df)
