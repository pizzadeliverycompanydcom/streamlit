import streamlit as st

MATH_Score = [80, 70, 55, 30, 15, 9, 7, 3, 3, 2, 1, 0]

st.write("# 21113053_구시진")
st.write("## 수학시험 점수 분포")

MATH_Score

st.bar_chart(MATH_Score)