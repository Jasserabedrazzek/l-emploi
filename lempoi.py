import streamlit as st
import pandas as pd
from numpy import *
n = 0
# Create an empty DataFrame*
ok = False
while ok == False:
  add = st.button("ADD")
  if add:
    n+=1
  T = array([str]*n)
  for i n range(n):
    T[i] = st.text_input(f"envent {i}:")
    
df = pd.DataFrame(columns=['Event', 'Time'],for i in range(5))



st.table(df)
# Add a new row to the DataFrame based on user input
