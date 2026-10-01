from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    input="한국어로 'OpenAI API 연결 성공!'이라고 답해줘."
)

print(response.output_text)
