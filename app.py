import os
import streamlit as st
import openai

st.markdown(
    """
    <head>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    """,
    unsafe_allow_html=True,
)

# 设置OpenAI API密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 检查是否设置了OpenAI API密钥
if openai.api_key:
    print("OpenAI API Key:", openai.api_key)
else:
    print("OpenAI API Key not found.")


def answer_question(model, prompt):
    """
    回答问题
    """
    # 向OpenAI请求回答
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=3072,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 获取OpenAI回答
    message = completions.choices[0].text
    print("OpenAI API Answer:", message)
    return message


def answer():
    """
    回答界面
    """
    # 设置页面标题
    st.title("Hi,I am ChatGPT. Please ask your questions, and I will do my best to provide you with a satisfactory answer.")

    # 设置使用的OpenAI模型
    model = "text-davinci-003"

    # 设置输入问题的文本框
    question = st.text_area("Your question:")

    # 如果用户点击提交按钮
    if st.button("Submit"):
        print("Your question is:", question)
        prompt = (f"{question}")

        # 获取ChatGPT的回答
        ChatGPT_Answer = answer_question(model, prompt)
        
        # 在页面上显示ChatGPT的回答
        st.write("ChatGPT Answer:")
        st.write("-" * 20)
        st.write(ChatGPT_Answer)

if __name__ == '__main__':

    answer()

