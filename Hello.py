import streamlit as st
st.write('Hello World')

import streamlit as st

option = st.selectbox(
    '',
    ('private Email', 'working Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

import matplotlib.pyplot as plt

st.pyplot(chart_data)
