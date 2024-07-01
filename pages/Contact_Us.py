import streamlit as st
from function import email_sender

st.title("Contact Us")

with st.form(key="contact_form"):
    user_email = st.text_input("Email:")
    topic = st.selectbox("topic", ("Primary", "Secondary", "Tertiary"))
    message_ = st.text_area("message")
    message = f"""\
    Subject: New message
    
    From:{user_email}
    
    {message_}
    """
    submit = st.form_submit_button("Submit")

    if submit:
        email_sender(message)
        st.info("Your message has been sent")
