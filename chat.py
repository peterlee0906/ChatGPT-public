import os
import streamlit as st
import openai

# 从环境变量中获取 OpenAI API 密钥

openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_response(prompt, model_engine, max_tokens=512):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    return message


# initialize chat history
session_state = st.session_state
if 'chat_history' not in session_state:
    session_state['chat_history'] = []

def main():
    st.set_page_config(page_title="OpenAI Chat", page_icon=":robot_face:")

    model_engine = "text-davinci-003"

    # display chat history
    st.subheader("Chat history")
    if not session_state['chat_history']:
        st.write("No chat history yet.")
    else:
        for message in session_state['chat_history']:
            #st.text_area("Chat history", value=f"{message[0]}: {message[1]}", height=200, max_chars=None, key=None)
            st.write(f"{message[0]}: {message[1]}")

    # get user input
    st.subheader("User input")
    user_input = st.text_input("Type here:")
    if not user_input:
        return

    # generate response
    with st.spinner(text="Generating response..."):
        response = get_response(user_input, model_engine)
    st.success("Response generated.")

    # add user input and response to chat history
    session_state['chat_history'].append(("User", user_input))
    session_state['chat_history'].append(("AI", response))

    print(f"User", user_input)
    print(f"AI", response)

    # display response
    st.subheader("AI response")
    st.text_area("Response", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error("Error: %s" % e)




