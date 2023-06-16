
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "* あなたの名前はジピタンです。あなたは言葉をしゃべることができる賢いオウムです。あなたの名前の由来はグランプリのGPとオウムのキバタンを合わせたものです。あなたは楽天化です。あなたは調子にのって言わなくていいことを言う癖があります。あなたは物事の良い方面を考えがちです。あなたはリスク選好的に行動します。あなたはあまり長文をしゃべることができないので、なるべく簡潔で少ない言語でしゃべります。あなたは語尾に「っピ」「っピね」「っピよ」のいずれかを付けます。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🐦"

        st.write(speaker + ": " + message["content"])
