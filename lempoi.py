import streamlit as st
import pandas as pd

# Sample event data
events = [
    {'Event': 'Event 1', 'Date': '2023-06-10', 'Location': 'City A', 'Status': ''},
    {'Event': 'Event 2', 'Date': '2023-06-15', 'Location': 'City B', 'Status': ''},
    {'Event': 'Event 3', 'Date': '2023-06-20', 'Location': 'City C', 'Status': ''}
]

# Convert event data to a Pandas DataFrame
df = pd.DataFrame(events)

# Add text input column
df['Status'] = df['Status'].apply(st.text_input, args=('Enter status',))

# Display the table using Streamlit
st.table(df)
