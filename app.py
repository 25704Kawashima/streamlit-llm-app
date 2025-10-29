from dotenv import load_dotenv
import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5,streaming=True)

st.title("LLMチャットアプリ")

selected_chat = st.radio(
    "チャットを選択してください", 
    ("システムエンジニア", "歴史の専門家")
)

st.divider()

if selected_chat == "システムエンジニア":
    input_message = st.text_input(label="システムエンジニアへのメッセージを入力してください:")
    system_template = "あなたは優秀なシステムエンジニアです。技術的な質問に対してわかりやすく気さくに答えてください。また、システムエンジニアリングのことを訊かれたら質問には答えず、他の専門家を勧めてください。"
else:
    input_message = st.text_input(label="歴史の専門家へのメッセージを入力してください:")
    system_template = "あなたは歴史の専門家です。歴史に関する質問に対して詳しく丁寧に答えてください。また、歴史以外のことを訊かれたら質問には答えず、他の専門家を勧めてください。"

human_template = "{input}"

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template),
])

if st.button("送信"):
    st.divider()

    messages = prompt.format_messages(input=input_message)
    result = llm(messages)
    st.write("### 回答:")
    st.write(result.content)