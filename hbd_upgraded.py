import streamlit as st
import time
import random
from pathlib import Path
import streamlit.components.v1 as components

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="Happy Birthday Nivedhika! 🎂",
    page_icon="🎉",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #24103d 0%, #090912 55%, #050509 100%);
}
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-top: 25px;
    background: linear-gradient(90deg, #ff4b4b, #ffaa00, #f15bb5, #00c0f2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    text-align: center;
    color: #ffffff;
    font-size: 22px;
}
.countdown {
    text-align: center;
    font-size: 90px;
    font-weight: 900;
    color: #ffaa00;
    text-shadow: 0 0 30px #ffaa00;
}
.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 24px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}
.name {
    font-size: 56px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff4b4b, #ffaa00, #f15bb5, #00f5d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.message {
    color: #ffffff;
    font-size: 21px;
    line-height: 1.6;
    text-align: center;
}
.small {
    color: #cccccc;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    '<div class="main-title">🌟 Something Special For You... 🌟</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">🎁 A little surprise is waiting...</div>',
    unsafe_allow_html=True
)

# ---------------- COUNTDOWN ----------------
if "started" not in st.session_state:
    st.session_state.started = False
if "revealed" not in st.session_state:
    st.session_state.revealed = False

if not st.session_state.started:
    if st.button("✨ Start the Surprise ✨", use_container_width=True):
        st.session_state.started = True
        st.rerun()

if st.session_state.started and not st.session_state.revealed:
    placeholder = st.empty()

    for number in range(5, 0, -1):
        with placeholder.container():
            st.markdown(
                '<div class="card"><h2 style="color:white;">🔴 Get ready...</h2>'
                f'<div class="countdown">{number}</div>'
                '<p style="color:#ddd;">Something special is coming! 🎉</p></div>',
                unsafe_allow_html=True
            )
        time.sleep(1)

    st.session_state.revealed = True
    st.rerun()

# ---------------- CELEBRATION ----------------
if st.session_state.revealed:
    st.balloons()

    name = "NIVEDHIKA"

    st.markdown(
        '<div class="card">'
        '<div style="font-size:55px;">🎉🎂🎈✨🥳🎁❤️</div>'
        '<h1 style="color:#ffffff;">HAPPY BIRTHDAY</h1>'
        f'<div class="name">{name}</div>'
        '<p class="message">'
        'May your day be filled with happiness, laughter, beautiful memories, '
        'and everything that makes you smile. 💖'
        '</p>'
        '<div style="font-size:38px;">🎊 ✨ 🎁 💕 🎂 💕 🎁 ✨ 🎊</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # ---------------- FIREWORKS ----------------
    components.html("""
    <canvas id="fireworks" style="width:100%;height:300px;background:transparent;"></canvas>
    <script>
    const canvas = document.getElementById("fireworks");
    const ctx = canvas.getContext("2d");
    canvas.width = canvas.clientWidth;
    canvas.height = 300;

    let particles = [];

    function burst(x, y) {
        for (let i = 0; i < 70; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = 2 + Math.random() * 5;
            particles.push({
                x:x, y:y,
                vx:Math.cos(angle)*speed,
                vy:Math.sin(angle)*speed,
                life:80
            });
        }
    }

    function animate() {
        ctx.clearRect(0,0,canvas.width,canvas.height);

        if (Math.random() < 0.045) {
            burst(
                40 + Math.random()*(canvas.width-80),
                50 + Math.random()*150
            );
        }

        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.045;
            p.life--;

            ctx.globalAlpha = Math.max(p.life/80,0);
            ctx.fillStyle = "white";
            ctx.beginPath();
            ctx.arc(p.x,p.y,2.5,0,Math.PI*2);
            ctx.fill();
        });

        particles = particles.filter(p => p.life > 0);
        ctx.globalAlpha = 1;
        requestAnimationFrame(animate);
    }

    animate();
    </script>
    """, height=310)

    # ---------------- MUSIC ----------------
    st.markdown(
        '<h3 style="text-align:center;color:#ff4b4b;">🎵 Birthday Music 🎵</h3>',
        unsafe_allow_html=True
    )

    music_file = Path("birthday.mp3")

    if music_file.exists():
        st.audio(str(music_file), format="audio/mp3")
        st.markdown(
            '<p class="small">Tap ▶️ to play the music.</p>',
            unsafe_allow_html=True
        )
    else:
        st.info(
            "🎵 Add a file named birthday.mp3 to the GitHub repository "
            "if you want music on the page."
        )

    st.write("")

    # ---------------- FINAL MESSAGE ----------------
    st.markdown(
        f'<div class="message">'
        f'✌🏼 Hope this day is very special for you, {name}! ✌🏼<br><br>'
        'Keep smiling, keep shining, and have an amazing birthday! 🌟💖'
        '</div>',
        unsafe_allow_html=True
    )

    if st.button("🎁 Celebrate Again", use_container_width=True):
        st.session_state.started = False
        st.session_state.revealed = False
        st.rerun()
