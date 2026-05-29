import streamlit as st
import os
import base64
import re

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════
ALBUM_NAME   = "Kisa Cha Ajabu"
ARTIST       = "Adventist Imara Daima Youth Choir"
SINGLE_KEY   = "Kisa Cha Ajabu"
MUSIC_FOLDER = "music"
YEAR         = "2026"

# ══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title=f"{SINGLE_KEY} — {ARTIST}",
    page_icon="COVER.png" if os.path.exists("COVER.png") else "🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"Get Help": None, "Report a bug": None, "About": None},
)

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_resource
def b64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def song_title(filename):
    return re.sub(r"\.mp3(\.mpeg)?$", "", filename, flags=re.IGNORECASE).strip()

def list_music():
    if not os.path.exists(MUSIC_FOLDER):
        return []
    return sorted(
        f for f in os.listdir(MUSIC_FOLDER)
        if re.search(r"\.mp3(\.mpeg)?$", f, re.IGNORECASE)
    )

def read_audio(filename):
    path = os.path.join(MUSIC_FOLDER, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    return None

# ══════════════════════════════════════════════════════════════════════════════
# STYLES
# ══════════════════════════════════════════════════════════════════════════════
bg_b64 = b64_image("COVER.png")
bg_css = (
    f"url(data:image/png;base64,{bg_b64})"
    if bg_b64
    else "linear-gradient(135deg,#0a0a0a,#1a1a2e)"
)

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;900&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

html, body, .stApp {{
    background:
        linear-gradient(rgba(0,0,0,0.80), rgba(0,0,0,0.90)),
        {bg_css} !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    font-family: 'Montserrat', sans-serif !important;
    color: #fff !important;
}}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stFooter"],
[data-testid="stSidebar"],
header[data-testid="stHeader"] {{ display: none !important; }}

.block-container {{
    max-width: 760px !important;
    padding: 2.5rem 1.5rem 5rem !important;
}}

/* ── Animated launch banner ── */
.launch-banner {{
    background: linear-gradient(135deg, #1db954, #0d6e31);
    border-radius: 12px;
    padding: 15px 24px;
    text-align: center;
    font-weight: 700;
    font-size: 13px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #fff;
    margin-bottom: 32px;
    animation: pulse-glow 2.2s ease-in-out infinite;
}}
@keyframes pulse-glow {{
    0%,100% {{ box-shadow: 0 0 18px rgba(29,185,84,0.45); }}
    50%      {{ box-shadow: 0 0 40px rgba(29,185,84,0.9), 0 0 70px rgba(29,185,84,0.25); }}
}}

/* ── Cover frame ── */
.cover-frame {{
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 16px 60px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.07);
    transition: transform 0.35s ease;
}}
.cover-frame:hover {{ transform: scale(1.02); }}

/* ── Featured single card ── */
.single-card {{
    background: linear-gradient(135deg, rgba(255,215,0,0.12), rgba(255,165,0,0.04));
    border: 1px solid rgba(255,215,0,0.35);
    border-radius: 18px;
    padding: 30px 28px;
    margin: 28px 0 24px;
    text-align: center;
}}
.sc-tag {{
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    color: #FFD700;
    opacity: 0.75;
    margin-bottom: 10px;
}}
.sc-title {{
    font-size: 42px;
    font-weight: 900;
    color: #FFD700;
    text-shadow: 0 2px 16px rgba(255,215,0,0.3);
    margin-bottom: 8px;
    line-height: 1.1;
    letter-spacing: -1px;
}}
.sc-artist {{
    font-size: 15px;
    color: #bbb;
    font-weight: 400;
    letter-spacing: 0.5px;
}}

/* ── Preview label ── */
.preview-label {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #1db954;
    margin-bottom: 10px;
    margin-top: 28px;
}}

/* ── Buttons ── */
.stDownloadButton > button,
.stButton > button {{
    background: linear-gradient(135deg, #1db954, #159a41) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    padding: 16px 36px !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 4px 20px rgba(29,185,84,0.45) !important;
    transition: all 0.22s ease !important;
    cursor: pointer !important;
    width: 100% !important;
}}
.stDownloadButton > button:hover,
.stButton > button:hover {{
    background: linear-gradient(135deg, #22e060, #1db954) !important;
    box-shadow: 0 8px 30px rgba(29,185,84,0.7) !important;
    transform: translateY(-2px) !important;
}}

/* ── Footer ── */
.page-footer {{
    text-align: center;
    color: rgba(255,255,255,0.30);
    font-size: 12px;
    font-weight: 300;
    letter-spacing: 1.2px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.07);
}}

/* ── Divider ── */
.divider {{
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 28px 0;
}}

@media (max-width: 640px) {{
    .sc-title       {{ font-size: 30px; }}
    .block-container {{ padding: 1.5rem 1rem 4rem !important; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

# ══════════════════════════════════════════════════════════════════════════════
# CONTENT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f'<div class="launch-banner">⭐ Featured Single &nbsp;·&nbsp; {SINGLE_KEY} &nbsp;·&nbsp; {ARTIST}</div>',
    unsafe_allow_html=True,
)

# Centered album cover
_, col_img, _ = st.columns([1, 2, 1])
with col_img:
    if os.path.exists("COVER.png"):
        st.markdown('<div class="cover-frame">', unsafe_allow_html=True)
        st.image("COVER.png", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Featured single card
st.markdown(
    f'<div class="single-card">'
    f'<p class="sc-tag">⭐ Featured Single</p>'
    f'<p class="sc-title">{SINGLE_KEY}</p>'
    f'<p class="sc-artist">{ARTIST} &nbsp;·&nbsp; {YEAR}</p>'
    f"</div>",
    unsafe_allow_html=True,
)

# Find the single file
music_files = list_music()
single_file = next((f for f in music_files if song_title(f) == SINGLE_KEY), None)
audio = read_audio(single_file) if single_file else None

if audio:
    # Preview player
    st.markdown('<p class="preview-label">▶ Preview</p>', unsafe_allow_html=True)
    st.audio(audio, format="audio/mpeg")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Big centered download button
    _, dl_col, _ = st.columns([0.5, 2, 0.5])
    with dl_col:
        st.download_button(
            f"⬇  Download {SINGLE_KEY}",
            data=audio,
            file_name=f"{SINGLE_KEY}.mp3",
            mime="audio/mpeg",
            key="single_dl",
        )
else:
    st.error(f"Track '{SINGLE_KEY}' was not found in the '{MUSIC_FOLDER}' folder.")

st.markdown(
    f'<p class="page-footer">© {YEAR} Adventist Imara Daima Youth Choir &nbsp;·&nbsp; {ALBUM_NAME} Album</p>',
    unsafe_allow_html=True,
)
