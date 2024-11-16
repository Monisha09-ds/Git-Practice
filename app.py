import streamlit as st

# Streamlit App
st.title("Simple Email Writer")

# Input Fields
recipient = st.text_input("Recipient's Email Address", placeholder="e.g., example@example.com")
subject = st.text_input("Email Subject", placeholder="Enter the subject of the email")
context = st.text_area("Email Content", placeholder="Write the body of the email")

# Generate Button
if st.button("Generate Email"):
    if recipient and subject and context:
        # Format the email
        email_template = f"""
        To: {recipient}
        Subject: {subject}

        Dear {recipient.split('@')[0].capitalize()},

        {context}

        Best regards,
        [Your Name]
        """
        st.success("Email Generated Successfully!")
        st.text_area("Generated Email", email_template, height=250)
    else:
        st.warning("Please fill out all fields!")
