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
        print("OpenAI API Key is OK")
    # 如果没有找到 OpenAI API 密钥，则输出错误消息
    else:
        print("OpenAI API Key not found.")
    


def answer_question(model, prompt):
    try:
        completions = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
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
    st.title("Hi,I am ChatGPT! \n")
             # ||("Please ask your questions, and I will do my best to provide you with a satisfactory answer.")

    model = "text-davinci-003"

    # 创建文本输入组件以获取用户的问题
    input_text = st.text_input("您有什么问题？")


    submit_button=st.button("Submit")

    # 创建文本区域组件以显示聊天历史记录
    history_text = st.text_area("Chat History:", "")

    

    if submit_button:
        if input_text :
            print("Your question is:", input_text)
            prompt = (f"{input_text}")

            ChatGPT_Answer  = answer_question(model, prompt)
            
            if ChatGPT_Answer:
                
                # 在 Streamlit 应用程序中显示生成的响应
                # st.text_output("AI: " + ChatGPT_Answer)
                # 将用户输入和 AI 响应追加到聊天历史记录中
                st.write("AI: " + ChatGPT_Answer)
                history_text += "User: " + input_text + "\n"
                history_text += "AI: " + ChatGPT_Answer + "\n"
            
            else:
                st.write("Error occurred while getting the answer from OpenAI API.")
            
            # with open('questions_answers.csv', mode='a', newline='', encoding='utf-8') as file:
            #   writer = csv.writer(file)
            #   writer.writerow([question, ChatGPT_Answer])

if __name__ == '__main__':

    answer()
