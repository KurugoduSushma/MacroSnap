import streamlit as st
from twilio.rest import Client


account_sid = st.secrets["TWILIO_ACCOUNT_SID"]
auth_token = st.secrets["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)


message = client.messages.create(
    from_=st.secrets["TWILIO_WHATSAPP_FROM"],
    to="whatsapp:+918328410944",
    body="🥗 MacroSnap test message!\n\nTwilio connection is working."
)

print("Message SID:", message.sid)