import os
import streamlit as st
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

if openai.api_key:
    print("OpenAI API Key:", openai.api_key)
else:
    print("OpenAI API Key not found.")



def answer_question(model, prompt):
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



def answer():
    st.title("Hi,I am ChatGPT. Please ask your questions, and I will do my best to provide you with a satisfactory answer.")

    model = "text-davinci-003"

    question = st.text_area("Your question:")

    if st.button("Submit"):
        print("Your question is:", question)
        prompt = (f"{question}")

        ChatGPT_Answer = answer_question(model, prompt)
        
        st.write("ChatGPT Answer:")
        st.write("-" * 20)
        st.write(ChatGPT_Answer)

if __name__ == '__main__':

    answer()
