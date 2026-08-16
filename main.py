import streamlit as st
import datetime
from pytz import timezone

slider = st.slider("Current day", 1, 31)

trip_start = datetime.datetime(2026, 10, 2);
trip_end = datetime.datetime(2026, 10, 27);
current = datetime.datetime.now();
current = datetime.datetime(2026, 10, slider.real);
messages = open("assets/quotes.txt").read().splitlines()

if current < trip_start:
    st.header(f"Days until Saas-Fee: {(trip_start - current).days}")
    exit(0)

st.header(f"♥️ From Saas-Fee - October {current.day}")
st.divider()

left1, right1 = st.columns(2, border=True);
left2, right2 = st.columns(2, border=True);

left1.write("Message of the day")
left1.write(f"**{messages[current.day - 1]}**")
right1.metric("Days until return", f"{(trip_end - current).days}")

left2.metric("Saas-Fee Elevation", "13,123 ft.", icon=":material/altitude:")
right2.metric("Current time in Saas-Fee", f"{datetime.datetime.now(timezone("Europe/Zurich")).strftime("%I:%M %p")}", icon=":material/chronic:")

st.subheader("A glimpse of where we are...")
st.iframe('<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d40644.18874283654!2d7.860087375578062!3d46.08571498084126!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x478f45a2f68360a7%3A0xe58089a57a3d1ace!2s3906%20Saas-Fee%2C%20Switzerland!5e1!3m2!1sen!2sus!4v1786837906444!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>')
