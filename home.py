import streamlit as st
import qrcode
import os
import base64
import io


# CONFIGURATION — update both URLs after deploying album.py and single.py

ALBUM_NAME     = "Kisa Cha Ajabu"
ARTIST         = "Adventist Imara Daima Youth Choir"
SINGLE_KEY     = "Kisa Cha Ajabu"
YEAR           = "2026"

ALBUM_APP_URL  = "https://kisachaajabu-p64aw4idjxs5amwsbt02rjewm-album.streamlit.app"
SINGLE_APP_URL = "https://kisachaajabu-vmzqlyj8ijna9dykpqhkozi-single.streamlit.app"


# PAGE CONFIG
st.set_page_config(
    page_title=f"{ALBUM_NAME} — {ARTIST}",
    page_icon="COVER.png" if os.path.exists("COVER.png") else "🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"Get Help": None, "Report a bug": None, "About": None},
)


# HELPERS

@st.cache_resource
def b64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def make_qr(url, fill="#0e632c"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


# STYLES

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
    max-width: 860px !important;
    padding: 2rem 1.5rem 5rem !important;
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
    margin-bottom: 30px;
    animation: pulse-glow 2.2s ease-in-out infinite;
}}
@keyframes pulse-glow {{
    0%,100% {{ box-shadow: 0 0 18px rgba(29,185,84,0.45); }}
    50%      {{ box-shadow: 0 0 40px rgba(29,185,84,0.9), 0 0 70px rgba(29,185,84,0.25); }}
}}

/* ── Hero typography ── */
.hero-tag {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: #1db954;
    text-align: center;
    margin-bottom: 10px;
}}
.hero-title {{
    font-size: 54px;
    font-weight: 900;
    text-align: center;
    color: #fff;
    line-height: 1.04;
    letter-spacing: -2px;
    text-shadow: 0 4px 28px rgba(0,0,0,0.8);
    margin-bottom: 12px;
}}
.hero-artist {{
    font-size: 17px;
    color: #aaa;
    text-align: center;
    font-weight: 400;
    letter-spacing: 2px;
    margin-bottom: 26px;
}}

/* ── Info pills ── */
.pill-row {{ text-align: center; margin-bottom: 28px; }}
.pill {{
    display: inline-block;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 12px;
    font-weight: 600;
    color: #ccc;
    margin: 3px 4px;
}}

/* ── Album cover frame ── */
.cover-frame {{
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 12px 55px rgba(0,0,0,0.75), 0 0 0 1px rgba(255,255,255,0.07);
    transition: transform 0.35s ease;
}}
.cover-frame:hover {{ transform: scale(1.025); }}

/* ── QR code card ── */
.qr-card {{
    background: #fff;
    border-radius: 14px;
    padding: 10px 10px 5px;
    box-shadow: 0 8px 35px rgba(0,0,0,0.55);
    text-align: center;
}}
.qr-label {{
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #333;
    margin-top: 5px;
    padding-bottom: 2px;
}}

/* ── Scan instruction ── */
.scan-hint {{
    font-size: 12px;
    color: rgba(255,255,255,0.45);
    text-align: center;
    letter-spacing: 1px;
    margin-top: 8px;
    font-weight: 400;
}}

/* ── Buttons ── */
.stDownloadButton > button {{
    background: linear-gradient(135deg, #1db954, #159a41) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 10px 22px !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 3px 14px rgba(29,185,84,0.38) !important;
    transition: all 0.22s ease !important;
    cursor: pointer !important;
    white-space: nowrap !important;
    width: 100% !important;
}}
.stDownloadButton > button:hover {{
    background: linear-gradient(135deg, #22e060, #1db954) !important;
    box-shadow: 0 6px 24px rgba(29,185,84,0.65) !important;
    transform: translateY(-1px) !important;
}}

/* ── Footer ── */
.page-footer {{
    text-align: center;
    color: rgba(255,255,255,0.32);
    font-size: 12px;
    font-weight: 300;
    letter-spacing: 1.2px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.07);
}}

@media (max-width: 640px) {{
    .hero-title  {{ font-size: 34px; letter-spacing: -1px; }}
    .hero-tag    {{ font-size: 10px; }}
    .block-container {{ padding: 1.2rem 1rem 4rem !important; }}
}}
</style>
""",
    unsafe_allow_html=True,
)


# HOME PAGE

st.markdown(
    f'<div class="launch-banner">'
    f"🎉&nbsp; New Album Out Now &nbsp;·&nbsp; {ALBUM_NAME} &nbsp;·&nbsp; {ARTIST}"
    f"</div>",
    unsafe_allow_html=True,
)

st.markdown(f'<p class="hero-tag">New Release &nbsp;·&nbsp; {YEAR}</p>', unsafe_allow_html=True)
st.markdown(f'<h1 class="hero-title">{ALBUM_NAME}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-artist">{ARTIST}</p>', unsafe_allow_html=True)

st.markdown(
    f'<div class="pill-row">'
    f'<span class="pill">🎶 7 Tracks</span>'
    f'<span class="pill">⭐ Single: {SINGLE_KEY}</span>'
    f'<span class="pill">📅 {YEAR}</span>'
    f"</div>",
    unsafe_allow_html=True,
)

# Generate both QR codes
album_qr  = make_qr(ALBUM_APP_URL,  fill="#1db954")
single_qr = make_qr(SINGLE_APP_URL, fill="#000000")

_, col_aqr, col_sqr, _ = st.columns([0.5, 1, 1, 0.5])

with col_aqr:
    st.markdown('<div class="qr-card">', unsafe_allow_html=True)
    st.image(album_qr, use_container_width=True)
    st.markdown('<p class="qr-label">Full Album</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<p class="scan-hint">Scan to download album</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        "⬇ Save Album QR",
        data=album_qr,
        file_name="kisa-cha-ajabu-album-qr.png",
        mime="image/png",
        key="dl_album_qr",
    )

with col_sqr:
    st.markdown('<div class="qr-card">', unsafe_allow_html=True)
    st.image(single_qr, use_container_width=True)
    st.markdown('<p class="qr-label">Single</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<p class="scan-hint">Scan to download single</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        "⬇ Save Single QR",
        data=single_qr,
        file_name="kisa-cha-ajabu-single-qr.png",
        mime="image/png",
        key="dl_single_qr",
    )

st.markdown(
    f'<p class="page-footer">© {YEAR} Adventist Imara Daima Youth Choir &nbsp;·&nbsp; {ALBUM_NAME} Album<br>'
    f"Scan the QR codes to listen &amp; download</p>",
    unsafe_allow_html=True,
)
