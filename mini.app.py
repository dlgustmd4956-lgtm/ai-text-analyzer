import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

st.title("AI TEXT ANALYZER MINI")

st.write("텍스트를 분석해드립니다.")

user_text = st.text_area("분석할 텍스트를 입력해주십시오", height=250)

if st.button("분석하기"):
    if user_text.strip() == "":
        st.warning("텍스트가 입력되지 않았습니다.")

    else:
       with st.spinner("분석 중..."):

        response = client.responses.create(
          model = "gpt-6-luna",
          input = f"""
 사용자의 텍스트를 아래 프롬프트에 맞게 분석해주세요.
[프롬프트]
1. 초등학생도 이해할 수 있는 관련 예시 3가지
2. 핵심 키워드 5가지
3. 관련 분야 2가지

텍스트:
{user_text}
"""
       )
       st.subheader("분석 완료")
       st.write(response.output_text)