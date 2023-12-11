import streamlit as st

st.set_page_config(layout='wide')

st.title('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Your email address')
    message = st.text_area('Your message')
    button = st.form_submit_button('Submit')
    print(button)
    if button:
        print(button)
        print('I was pressed!')