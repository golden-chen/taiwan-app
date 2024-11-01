import streamlit as st
import pandas as pd
st.markdown("# Story-3 ❄️")
st.sidebar.markdown("# Story-3 ❄️")
st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80", caption="Sunrise by the mountains")
@st.cache_data
def load_data(url):
    df = pd.read_csv(url,encoding="big5")  # 👈 Download the data
    return df

df = load_data("https://data.taipei/api/dataset/e93c7e94-2d3c-4686-b81e-1f1975a1953d/resource/647c171d-8ff1-44bd-beb3-16eed00edc6b/download")
st.dataframe(df)

st.button("Rerun")
