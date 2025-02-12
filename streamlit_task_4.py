
import google.generativeai as genai
f=open(r"D:/Docu/pyjunb/API_keys/API_key_innomatics.txt")
key=f.read()
genai.configure(api_key=key)
import streamlit as st

sys_prompt = """
You are a Python code reviewer. Your task is to analyze the provided Python code for potential bugs, errors, and areas of improvement.
If the user submits code in languages other than Python, inform them that the review is only for Python code.
You will return suggestions for fixing issues in the code along with the corrected code
in structures first concise bug report ans then fixed code.
"""

model2 = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

st.title("AI Code Reviewer")
st.write("Submit your Python code below for review:")

user_code = st.text_area("Enter Python Code Here", height=300)

if st.button("Generate"):
    if user_code.strip():
        try:
            prompt = user_code
            res = model2.generate_content(prompt)
            st.subheader("Code Review")
            st.write(res.text)
        except Exception as e:
            st.error(f"An error occurred while reviewing the code: {e}")
    else:
        st.warning("Please enter Python code for review.")
