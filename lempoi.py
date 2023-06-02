import streamlit as st
import pandas as pd
from numpy import *

# Create an empty DataFrame
df = pd.DataFrame(columns=['Event', 'Time'],for i in range(5))



st.table(df)
# Add a new row to the DataFrame based on user input
