import streamlit as st
import pandas as pd
from numpy import *
import datetime

T = array([str]*19)
D = array([str]*19)
df = array([str]*19)
# Sample event data
for i in range(1,19):
    T[i] = st.text_input(f'envent {i} :')
    D[i] = st.date_input(
        "When\'s ?",
        datetime.date(2019, 7, i))
for i in range(1,19):  
    events = [
        {'Event':T[i], 'Date': D[i]},
       
    ]

# Convert event data to a Pandas DataFrame
    df[i] = pd.DataFrame(events)


# Display the table using Streamlit
    st.table(df)
