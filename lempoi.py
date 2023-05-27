
import streamlit as st
import pandas as pd
import numpy as np
for i in range(5):
   df = pd.DataFrame(
      np.random.randn(10, 5),

      columns=('col %d'))

st.table(df)
