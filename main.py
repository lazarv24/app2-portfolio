import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo_of_me.jpg', width=600)

with col2:
    st.title('Lazar Voštić')
    content = '''
    Hello, I am Lazar. I am a Python programmer. For me coding is great way to show my skills and passion
    for programming and computers in general. I have solid experience with programming for a young guy like me in early
    twenties, when I was first started using Python, I decided to take a SoftUni course for programming basics and
    finished the course with maximum grade. After that I expanded my knowledge and experience on another level,
    listening to Udemy courses and many others, along with hard work I implement every day when I code to become better
    as much as I can. And for me there are no limits with that. Also have experience with making graphical user
    interface apps and web apps, web frameworks such as Streamlit, Heroku, Django and web development in general.
    '''

    st.info(content)

content2 = '''
Below you can find some of the apps I have built in Python. Feel free to contact me!
'''

st.write(content2)

