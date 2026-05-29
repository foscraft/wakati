import streamlit as st
import qrcode
import os
import base64
import io

ALBUM_NAME   = "Kisa Cha Ajabu"
ARTIST       = "Adventist Imara Daima Youth Choir"
SINGLE_KEY   = "Kisa Cha Ajabu"
YEAR         = "2026"
TRACK_COUNT  = 8
ALBUM_URL    = "https://kisachaajabu-p64aw4idjxs5amwsbt02rjewm-album.streamlit.app"
SINGLE_URL   = "https://kisachaajabu-vmzqlyj8ijna9dykpqhkozi-single.streamlit.app"

st.set_page_config(
    page_title=f"{ALBUM_NAME} — {ARTIST}",
    page_icon="COVER.png" if os.path.exists("COVER.png") else "🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"Get Help": None, "Report a bug": None, "About": None},
)

@st.cache_resource
def b64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def make_qr(url, fill="#1db954"):
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

bg_b64 = b64_image("BACKGROUND.png")
bg_css = (
    f"url(data:image/png;base64,{bg_b64})" if bg_b64
    else "linear-gradient(160deg,#060606,#0b160c)"
)

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;900&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

html, body, .stApp, [data-testid="stAppViewContainer"] {{
    background-image:
        linear-gradient(rgba(0,0,0,0.84), rgba(0,0,0,0.94)),
        {bg_css} !important;
    background-size: cover, cover !important;
    background-position: center, center !important;
    background-repeat: no-repeat, no-repeat !important;
    background-attachment: fixed, fixed !important;
    font-family: 'Montserrat', sans-serif !important;
    color: #fff !important;
}}

#MainMenu, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stFooter"],
[data-testid="stSidebar"],
header[data-testid="stHeader"] {{ display: none !important; }}

.block-container {{
    max-width: 800px !important;
    padding: 3.5rem 2rem 6rem !important;
}}

/* ── Eyebrow ── */
.eyebrow {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: #1db954;
    text-align: center;
    margin: 0 0 22px;
}}

/* ── Hero ── */
.hero-title {{
    font-size: 60px;
    font-weight: 900;
    text-align: center;
    color: #fff;
    line-height: 1.0;
    letter-spacing: -2.5px;
    text-shadow: 0 6px 50px rgba(0,0,0,0.95);
    margin: 18px 0 10px;
}}
.hero-artist {{
    font-size: 11px;
    color: #666;
    text-align: center;
    font-weight: 500;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    margin-bottom: 22px;
}}

/* ── Pills ── */
.pill-row {{ text-align: center; margin-bottom: 42px; }}
.pill {{
    display: inline-block;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 50px;
    padding: 5px 16px;
    font-size: 11px;
    font-weight: 600;
    color: #888;
    margin: 3px 4px;
    letter-spacing: 0.3px;
}}
.pill.green {{
    background: rgba(29,185,84,0.11);
    border-color: rgba(29,185,84,0.28);
    color: #1db954;
}}
.pill.gold {{
    background: rgba(255,215,0,0.09);
    border-color: rgba(255,215,0,0.26);
    color: #d4a800;
}}

/* ── Cover ── */
.cover-wrap {{
    border-radius: 18px;
    overflow: hidden;
    box-shadow:
        0 32px 100px rgba(0,0,0,0.90),
        0 0 0 1px rgba(255,255,255,0.06);
    transition: transform 0.45s ease, box-shadow 0.45s ease;
}}
.cover-wrap:hover {{
    transform: translateY(-8px) scale(1.01);
    box-shadow:
        0 48px 120px rgba(0,0,0,0.95),
        0 0 0 1px rgba(255,255,255,0.11);
}}

/* ── Divider ── */
.divider {{
    width: 100%;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(255,255,255,0.09) 25%,
        rgba(255,255,255,0.09) 75%,
        transparent 100%
    );
    margin: 44px 0;
    border: none;
    display: block;
}}

/* ── Section label ── */
.section-label {{
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.30);
    text-align: center;
    margin-bottom: 26px;
}}

/* ── QR cards ── */
.qr-card {{
    background: #fff;
    border-radius: 14px;
    padding: 14px 14px 8px;
    box-shadow:
        0 16px 60px rgba(0,0,0,0.70),
        0 4px 16px rgba(0,0,0,0.40);
    text-align: center;
}}
.qr-label {{
    font-size: 8px;
    font-weight: 900;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #1a1a1a;
    margin-top: 8px;
    padding-bottom: 3px;
}}
.qr-hint {{
    font-size: 11px;
    color: rgba(255,255,255,0.32);
    text-align: center;
    letter-spacing: 0.2px;
    margin: 10px 0 12px;
    font-weight: 400;
    line-height: 1.5;
}}

/* ── Buttons ── */
.stDownloadButton > button {{
    background: rgba(255,255,255,0.06) !important;
    color: #aaa !important;
    border: 1px solid rgba(255,255,255,0.13) !important;
    border-radius: 50px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600 !important;
    font-size: 11px !important;
    padding: 9px 20px !important;
    letter-spacing: 0.5px !important;
    transition: all 0.22s ease !important;
    cursor: pointer !important;
    width: 100% !important;
}}
.stDownloadButton > button:hover {{
    background: rgba(29,185,84,0.14) !important;
    border-color: rgba(29,185,84,0.38) !important;
    color: #1db954 !important;
    transform: translateY(-1px) !important;
}}

/* ── Footer ── */
.page-footer {{
    text-align: center;
    color: rgba(255,255,255,0.22);
    font-size: 11px;
    font-weight: 300;
    letter-spacing: 1.8px;
    margin-top: 60px;
    padding-top: 22px;
    border-top: 1px solid rgba(255,255,255,0.05);
    line-height: 1.8;
}}

@media (max-width: 640px) {{
    .hero-title {{ font-size: 38px; letter-spacing: -1.5px; }}
    .block-container {{ padding: 2rem 1.2rem 4rem !important; }}
}}
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────

st.markdown(f'<p class="eyebrow">New Release &nbsp;·&nbsp; {YEAR}</p>', unsafe_allow_html=True)

_, col_cover, _ = st.columns([0.7, 2, 0.7])
with col_cover:
    if os.path.exists("COVER.png"):
        st.markdown('<div class="cover-wrap">', unsafe_allow_html=True)
        st.image("COVER.png", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown(f'<h1 class="hero-title">{ALBUM_NAME}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-artist">{ARTIST}</p>', unsafe_allow_html=True)
st.markdown(
    f'<div class="pill-row">'
    f'<span class="pill green">🎶 {TRACK_COUNT} Songs</span>'
    f'<span class="pill">📅 {YEAR}</span>'
    f'<span class="pill gold">⭐ {SINGLE_KEY}</span>'
    f"</div>",
    unsafe_allow_html=True,
)

# ── QR Section ───────────────────────────────────────────────────────────────

st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<p class="section-label">Scan to Access</p>', unsafe_allow_html=True)

album_qr  = make_qr(ALBUM_URL,  fill="#1db954")
single_qr = make_qr(SINGLE_URL, fill="#111111")

_, col_aqr, _, col_sqr, _ = st.columns([0.25, 1, 0.12, 1, 0.25])

with col_aqr:
    st.markdown('<div class="qr-card">', unsafe_allow_html=True)
    st.image(album_qr, use_container_width=True)
    st.markdown('<p class="qr-label">Full Album</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<p class="qr-hint">Scan to browse &amp; download<br>all tracks</p>', unsafe_allow_html=True)
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
    st.markdown('<p class="qr-label">Featured Single</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<p class="qr-hint">Scan to download<br>the featured single</p>', unsafe_allow_html=True)
    st.download_button(
        "⬇ Save Single QR",
        data=single_qr,
        file_name="kisa-cha-ajabu-single-qr.png",
        mime="image/png",
        key="dl_single_qr",
    )

st.markdown(
    f'<p class="page-footer">'
    f'© {YEAR} Adventist Imara Daima Youth Choir &nbsp;·&nbsp; {ALBUM_NAME}<br>'
    f'Scan the QR codes above to listen &amp; download'
    f'</p>',
    unsafe_allow_html=True,
)
