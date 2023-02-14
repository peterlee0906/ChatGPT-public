import os
import csv
import streamlit as st
import openai

# 在 Streamlit 中添加自定义 CSS 样式
st.markdown(
    """
    <head>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    """,
    unsafe_allow_html=True,
)

# 从环境变量中获取 OpenAI API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 如果找到了 OpenAI API 密钥，则输出密钥
if openai.api_key:
    print("OpenAI API Key:", openai.api_key)
# 如果没有找到 OpenAI API 密钥，则输出错误消息
else:
    print("OpenAI API Key not found.")


def answer_question(model, prompt):
    try:
        completions = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=3072,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        print("OpenAI API Answer:", message)
        return message
    except Exception as e:
        print("Error occurred:", str(e))
        return None


def answer():
    st.title("Hi,I am ChatGPT. Please ask your questions, and I will do my best to provide you with a satisfactory answer.")

    model = "text-davinci-003"

    question = st.text_area("Your question:")

    if st.button("Submit"):
        print("Your question is:", question)
        prompt = (f"{question}")

        ChatGPT_Answer = answer_question(model, prompt)
        
        if ChatGPT_Answer:
            # st.write("ChatGPT Answer:")
            st.write("-" * 20)
            st.write(ChatGPT_Answer)
        else:
            st.write("Error occurred while getting the answer from OpenAI API.")
        
        # with open('questions_answers.csv', mode='a', newline='', encoding='utf-8') as file:
        #   writer = csv.writer(file)
        #   writer.writerow([question, ChatGPT_Answer])

if __name__ == '__main__':

    answer()
