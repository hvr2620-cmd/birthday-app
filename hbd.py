import streamlit as st  # type: ignore[import-not-found]
import time
import random

# Set up the web page title and a cute icon
st.set_page_config(page_title="Happy Birthday Nivedhika!", page_icon="🎉")

# Title styling
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🌟 Something Special For You... 🌟</h1>", unsafe_allow_html=True)

# Step 1: Initialize custom session state to handle the app steps
if "step" not in st.session_state:
    st.session_state.step = "countdown"
    st.session_state.countdown_val = 5

# Create a clean placeholder container for the animation frame updates
placeholder = st.empty()

# --- STEP A: THE COUNTDOWN ---
if st.session_state.step == "countdown":
    with placeholder.container():
        st.markdown(f"<h2 style='text-align: center;'>🔴 Preparing something special...</h2>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; font-size: 80px; color: #FFAA00;'>[ {st.session_state.countdown_val} ]</h1>", unsafe_allow_html=True)
    
    # Wait 1 second, then lower countdown
    time.sleep(1)
    st.session_state.countdown_val -= 1
    
    # Transition to the main celebration once countdown hits 0
    if st.session_state.countdown_val < 1:
        st.session_state.step = "celebrate"
    st.rerun()

# --- STEP B: THE CELEBRATION ---
elif st.session_state.step == "celebrate":
    # Trigger a massive burst of web balloons!
    st.balloons()
    
    # Setup name and simple color rotations
    name = "NIVEDHIKA"
    colors = ["#FF4B4B", "#00C0F2", "#FFAA00", "#9B5DE5", "#F15BB5", "#00F5D4"]
    c1, c2, c3 = random.sample(colors, 3)
    
    # Render the gorgeous, color-shifting ASCII Cake using web-safe HTML formatting
    cake_html = f"""
    <div style="text-align: center; font-family: monospace; font-size: 18px; line-height: 1.2; white-space: pre; background-color: #1E1E1E; padding: 20px; border-radius: 10px; color: #FFFFFF;">
<span style="color: #FFAA00;">       |||||||||||   ("stay happy, beautiful, always!")</span>
<span style="color: #FFAA00;">       |||||||||||</span>
<span style="color: {c1};">    =================</span>
<span style="color: {c1};">    |   H A P P Y   |</span>
<span style="color: {c2};"> =====================</span>
<span style="color: {c2};"> |  B I R T H D A Y  |</span>
<span style="color: {c3};">=======================</span>
<span style="color: {c3};">|  {name.center(19)}  |</span>
=======================
    </div>
    """
    
    with placeholder.container():
        st.markdown("<h3 style='text-align: center; color: #FF4B4B;'>🎵 MUSIC PLAYING: Happy Birthday to You! 🎵</h3>", unsafe_allow_html=True)
        st.markdown(cake_html, unsafe_allow_html=True)
        
        # Add a random pool of confetti emojis beneath the cake
        confetti_pool = ["🎉", "✨", "🥳", "🎁", "❤️", "⭐"]
        random_confetti = "  ".join(random.choices(confetti_pool, k=10))
        st.markdown(f"<h2 style='text-align: center;'>{random_confetti}</h2>", unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='text-align: center; color: #77DD77;'>✌🏼 hope this day is very special for you {name}! ✌🏼</h3>", unsafe_allow_html=True)

    # Automatically refresh every 0.6 seconds to keep the cake changing colors dynamically
    time.sleep(0.6)
    st.rerun()
