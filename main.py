import datetime

import streamlit as st
from pytz import timezone

trip_start = datetime.datetime(2026, 10, 2)
trip_end = datetime.datetime(2026, 10, 27)
current = datetime.datetime.now()
messages = open("assets/quotes.txt").read().splitlines()
facts = open("assets/facts.txt").read().splitlines()

if current < trip_start:
    st.header(f"Days until Saas-Fee: {(trip_start - current).days}")
    exit(0)

st.header(f"♥️ From Saas-Fee - October {current.day}")
st.write(f"**Did you know?** *{facts[current.day - 1]}*")
st.divider()

left1, right1 = st.columns(2, border=True)
left2, right2 = st.columns(2, border=True)
left1.write("Message of the day")
left1.write(f"**{messages[current.day - 1]}**")
right1.metric("Days until return", f"{(trip_end - current).days}")

left2.metric("Saas-Fee Elevation", "13,123 ft.", icon=":material/altitude:")
right2.metric(
    "Current time in Saas-Fee",
    f"{datetime.datetime.now(timezone('Europe/Zurich')).strftime('%I:%M %p')}",
    icon=":material/chronic:",
)

st.subheader("Photo of the day")
st.image(f"assets/photos/{current.day}.jpg")
