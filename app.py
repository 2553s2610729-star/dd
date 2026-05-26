import streamlit as st
import random

st.title("🎲 랜덤 코디 추천")

tops = ["흰 반팔", "검정 후드", "니트", "셔츠"]
bottoms = ["청바지", "슬랙스", "반바지", "조거팬츠"]

if st.button("코디 추천 받기"):
    top = random.choice(tops)
    bottom = random.choice(bottoms)

    st.write(f"상의: {top}")
    st.write(f"하의: {bottom}")
