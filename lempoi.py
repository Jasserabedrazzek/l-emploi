import streamlit as st
import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame(columns=['Event', 'Time'])

n = 0
while True:
    add = st.button("ADD")
    if add:
        n += 1
        event = st.text_input(f"Event {n}:")
        time = st.text_input(f"Time {n}:")
        df = df.append({'Event': event, 'Time': time}, ignore_index=True)
    else:
        break

# Display the table
st.table(df)
