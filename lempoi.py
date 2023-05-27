import streamlit as st
import pandas as pd

# Create a sample DataFrame with time data
data = {
    'Event': [st.text_input, 'Lunch', 'Presentation'],
    'Time': ['09:00', '12:30', '15:45']
}

df = pd.DataFrame(data)

# Display the DataFrame as a table in Streamlit
st.table(df)
