import streamlit as st
import os
import base64
import zipfile
import io
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
    page_title=f"{ALBUM_NAME} Album — {ARTIST}",
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

def build_zip(files):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in files:
            path = os.path.join(MUSIC_FOLDER, fname)
            if os.path.exists(path):
                zf.write(path, f"{song_title(fname)}.mp3")
    buf.seek(0)
    return buf.read()

# ══════════════════════════════════════════════════════════════════════════════
# STYLES
# ══════════════════════════════════════════════════════════════════════════════
bg_b64 = b64_image("BACKGROUND.png")
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

html, body, .stApp,
[data-testid="stAppViewContainer"] {{
    background-image:
        linear-gradient(rgba(0,0,0,0.80), rgba(0,0,0,0.90)),
        {bg_css} !important;
    background-size: cover, cover !important;
    background-position: center, center !important;
    background-repeat: no-repeat, no-repeat !important;
    background-attachment: fixed, fixed !important;
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
    text-align: left;
    margin-bottom: 10px;
}}
.hero-title {{
    font-size: 38px;
    font-weight: 900;
    color: #fff;
    line-height: 1.04;
    letter-spacing: -1.5px;
    text-shadow: 0 4px 28px rgba(0,0,0,0.8);
    margin-bottom: 10px;
}}
.hero-artist {{
    font-size: 15px;
    color: #aaa;
    font-weight: 400;
    letter-spacing: 1.5px;
    margin-bottom: 14px;
}}

/* ── Info pills ── */
.pill-row {{ margin-bottom: 4px; }}
.pill {{
    display: inline-block;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 12px;
    font-weight: 600;
    color: #ccc;
    margin: 3px 4px 3px 0;
}}

/* ── Cover frame ── */
.cover-frame {{
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 12px 55px rgba(0,0,0,0.75), 0 0 0 1px rgba(255,255,255,0.07);
    transition: transform 0.35s ease;
}}
.cover-frame:hover {{ transform: scale(1.025); }}

/* ── Featured single card ── */
.single-card {{
    background: linear-gradient(135deg, rgba(255,215,0,0.11), rgba(255,165,0,0.04));
    border: 1px solid rgba(255,215,0,0.32);
    border-radius: 16px;
    padding: 26px 28px;
    margin: 24px 0 26px;
    text-align: center;
}}
.sc-tag    {{ font-size: 10px; font-weight: 800; letter-spacing: 3px; text-transform: uppercase; color: #FFD700; opacity: 0.75; margin-bottom: 8px; }}
.sc-title  {{ font-size: 36px; font-weight: 900; color: #FFD700; text-shadow: 0 2px 14px rgba(255,215,0,0.3); margin-bottom: 6px; line-height: 1.1; letter-spacing: -1px; }}
.sc-artist {{ font-size: 14px; color: #bbb; font-weight: 400; }}

/* ── Section heading ── */
.section-head {{
    font-size: 19px;
    font-weight: 700;
    color: #fff;
    margin: 32px 0 14px;
    padding-bottom: 10px;
    border-bottom: 2px solid #1db954;
}}

/* ── Track list header bar ── */
.track-list-header {{
    display: flex;
    align-items: center;
    padding: 10px 14px;
    background: #1db954;
    border-radius: 10px 10px 0 0;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #fff;
    gap: 12px;
}}
.tlh-num   {{ width: 28px; text-align: center; flex-shrink: 0; }}
.tlh-title {{ flex: 1; }}
.tlh-dl    {{ width: 100px; text-align: right; flex-shrink: 0; }}

/* ── Track rows ── */
.track-item {{
    padding: 13px 14px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    background: rgba(255,255,255,0.025);
    transition: background 0.2s;
}}
.track-item:hover {{ background: rgba(29,185,84,0.12); }}
.track-item.is-single {{
    background: rgba(255,215,0,0.07);
    border-left: 3px solid #FFD700;
}}
.track-item.is-single:hover {{ background: rgba(255,215,0,0.15); }}
.t-num   {{ font-size: 13px; color: #777; font-weight: 600; }}
.t-title {{ font-size: 15px; color: #fff; font-weight: 500; line-height: 1.3; }}
.t-title.gold {{ color: #FFD700; font-weight: 700; }}
.single-badge {{
    display: inline-block;
    background: #FFD700;
    color: #000;
    font-size: 8px;
    font-weight: 900;
    padding: 2px 7px;
    border-radius: 4px;
    margin-left: 8px;
    letter-spacing: 1px;
    text-transform: uppercase;
    vertical-align: middle;
}}

/* ── Buttons ── */
.stDownloadButton > button,
.stButton > button {{
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
}}
.stDownloadButton > button:hover,
.stButton > button:hover {{
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
    .hero-title  {{ font-size: 28px; letter-spacing: -0.5px; }}
    .sc-title    {{ font-size: 26px; }}
    .block-container {{ padding: 1.2rem 1rem 4rem !important; }}
    .tlh-dl      {{ display: none; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

# ══════════════════════════════════════════════════════════════════════════════
# CONTENT
# ══════════════════════════════════════════════════════════════════════════════
music_files = list_music()

st.markdown(
    f'<div class="launch-banner">'
    f"🎉&nbsp; New Album Out Now &nbsp;·&nbsp; {ALBUM_NAME} &nbsp;·&nbsp; {ARTIST}"
    f"</div>",
    unsafe_allow_html=True,
)

# ── Album header ─────────────────────────────────────────────────────────────
hcol1, hcol2 = st.columns([1, 1.9])
with hcol1:
    if os.path.exists("COVER.png"):
        st.markdown('<div class="cover-frame">', unsafe_allow_html=True)
        st.image("COVER.png", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    if os.path.exists("LOGO.png"):
        st.markdown("<br>", unsafe_allow_html=True)
        st.image("LOGO.png", use_container_width=True)

with hcol2:
    n = len(music_files)
    st.markdown(
        f'<p class="hero-tag">Album &nbsp;·&nbsp; {YEAR}</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<h1 class="hero-title">{ALBUM_NAME}</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<p class="hero-artist">{ARTIST}</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="pill-row">'
        f'<span class="pill">🎶 {n} Songs</span>'
        f'<span class="pill">⭐ {SINGLE_KEY}</span>'
        f"</div>",
        unsafe_allow_html=True,
    )

# ── Featured single ───────────────────────────────────────────────────────────
single_file = next((f for f in music_files if song_title(f) == SINGLE_KEY), None)
if single_file:
    st.markdown(
        f'<div class="single-card">'
        f'<p class="sc-tag">⭐ Featured Single</p>'
        f'<p class="sc-title">{SINGLE_KEY}</p>'
        f'<p class="sc-artist">{ARTIST} &nbsp;·&nbsp; {YEAR}</p>'
        f"</div>",
        unsafe_allow_html=True,
    )
    audio = read_audio(single_file)
    if audio:
        scol1, scol2 = st.columns([1.8, 1])
        with scol1:
            st.audio(audio, format="audio/mpeg")
        with scol2:
            st.download_button(
                "⬇ Download Single",
                data=audio,
                file_name=f"{SINGLE_KEY}.mp3",
                mime="audio/mpeg",
                key="single_featured_dl",
            )

# ── Download entire album as ZIP ──────────────────────────────────────────────
if music_files:
    st.markdown('<p class="section-head">📦 Download Entire Album</p>', unsafe_allow_html=True)
    zcol1, zcol2 = st.columns([2, 1])
    with zcol1:
        st.markdown(
            f'<p style="color:#bbb;font-size:13px;margin:0;">'
            f"Get all {n} songs in a single ZIP file.</p>",
            unsafe_allow_html=True,
        )
    with zcol2:
        if st.button("📦 Pack Album ZIP", key="build_zip_btn"):
            with st.spinner("Packing all songs…"):
                zip_data = build_zip(music_files)
            st.download_button(
                "⬇ Download All Songs (.zip)",
                data=zip_data,
                file_name=f"{ALBUM_NAME} — {ARTIST}.zip",
                mime="application/zip",
                key="album_zip_dl",
            )

# ── Track list ────────────────────────────────────────────────────────────────
st.markdown('<p class="section-head">🎵 All Tracks</p>', unsafe_allow_html=True)

st.markdown(
    '<div class="track-list-header">'
    '<span class="tlh-num">#</span>'
    '<span class="tlh-title">Title</span>'
    '<span class="tlh-dl">Download</span>'
    "</div>",
    unsafe_allow_html=True,
)

for i, fname in enumerate(music_files):
    title     = song_title(fname)
    is_single = title == SINGLE_KEY
    row_cls   = "track-item is-single" if is_single else "track-item"
    audio     = read_audio(fname)

    st.markdown(f'<div class="{row_cls}">', unsafe_allow_html=True)
    tc1, tc2, tc3 = st.columns([0.45, 2.8, 1.4])

    with tc1:
        marker = "⭐" if is_single else str(i + 1)
        st.markdown(f'<p class="t-num">{marker}</p>', unsafe_allow_html=True)

    with tc2:
        badge = '<span class="single-badge">Single</span>' if is_single else ""
        cls   = "t-title gold" if is_single else "t-title"
        st.markdown(f'<p class="{cls}">{title}{badge}</p>', unsafe_allow_html=True)

    with tc3:
        if audio:
            st.download_button(
                "⬇ Download",
                data=audio,
                file_name=f"{title}.mp3",
                mime="audio/mpeg",
                key=f"dl_track_{i}",
            )

    st.markdown("</div>", unsafe_allow_html=True)

    if audio:
        with st.expander(f"▶  Preview — {title}"):
            st.audio(audio, format="audio/mpeg")

st.markdown(
    f'<p class="page-footer">© {YEAR} Adventist Imara Daima Youth Choir &nbsp;·&nbsp; {ALBUM_NAME}</p>',
    unsafe_allow_html=True,
)
