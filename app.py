import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

st.title("AI Text Analyzer")

st.write("분석하고 싶은 글을 입력하세요.")

user_text = st.text_area(
    "텍스트 입력",
    height=250
)

if st.button("분석하기"):
    if user_text.strip() == "":
        st.warning("분석할 내용을 입력해주세요.")

    else:
        with st.spinner("AI가 분석하고 있습니다..."):

            response = client.responses.create(
                model="gpt-6-luna",
                input=f"""
다음 텍스트를 분석해주세요.

1. 핵심 내용을 3줄 이내로 요약
2. 중요한 포인트 3개
3. 초등학생도 알 수 있는 설명 3줄
4. 연관되어있는 분야 3가지 추천

텍스트:
{user_text}
"""
            )

        st.subheader("분석 결과")
        st.write(response.output_text)