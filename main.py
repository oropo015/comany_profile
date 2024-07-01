import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
df = pd.read_csv("data.csv")
st.title("TechTernet")
about_company = """
Techternet is a premier tech blogging platform dedicated to delivering the latest news, insights, and trends in the technology world. Our mission is to provide our readers with in-depth analyses, expert opinions, and comprehensive coverage of the tech industry. Whether it's breakthroughs in artificial intelligence, cybersecurity, software development, or the latest gadgets and innovations, Techternet is your go-to source for staying informed and ahead of the curve.
"""
st.write(about_company)
col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")