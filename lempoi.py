import streamlit as st
import pandas as pd
import numpy as np
import datetime
import streamlit.components.v1 as components



# Sample event data
events = []

for i in range(1, 19):
    event_name = st.text_input(f'Event {i}:')
    event_date = st.date_input("When's?", datetime.date(2019, 7, i))
    events.append({'Event': event_name, 'Date': str(event_date)})

# Convert event data to a Pandas DataFrame
df = pd.DataFrame(events)

# Display the table using Streamlit
st.table(df)
