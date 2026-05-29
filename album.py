import streamlit as st
import os
import base64
import zipfile
import io
import re

ALBUM_NAME   = "Kisa Cha Ajabu"
ARTIST       = "Adventist Imara Daima Youth Choir"
SINGLE_KEY   = "Kisa Cha Ajabu"
MUSIC_FOLDER = "music"
YEAR         = "2026"

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

@st.cache_data
def get_album_zip():
    files = list_music()
    return build_zip(files) if files else None

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
        linear-gradient(rgba(0,0,0,0.83), rgba(0,0,0,0.93)),
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
    max-width: 880px !important;
    padding: 2.5rem 2rem 6rem !important;
}}

/* ── Launch banner ── */
.launch-banner {{
    background: linear-gradient(135deg, #1db954, #0c6830);
    border-radius: 12px;
    padding: 14px 24px;
    text-align: center;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #fff;
    margin-bottom: 34px;
    animation: pulse-glow 2.6s ease-in-out infinite;
}}
@keyframes pulse-glow {{
    0%,100% {{ box-shadow: 0 0 16px rgba(29,185,84,0.38); }}
    50%      {{ box-shadow: 0 0 36px rgba(29,185,84,0.80), 0 0 60px rgba(29,185,84,0.18); }}
}}

/* ── Cover ── */
.cover-wrap {{
    border-radius: 14px;
    overflow: hidden;
    box-shadow:
        0 20px 70px rgba(0,0,0,0.85),
        0 0 0 1px rgba(255,255,255,0.06);
    transition: transform 0.38s ease;
}}
.cover-wrap:hover {{ transform: scale(1.02); }}

/* ── Hero meta ── */
.hero-tag {{
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: #1db954;
    margin-bottom: 14px;
}}
.hero-title {{
    font-size: 42px;
    font-weight: 900;
    color: #fff;
    line-height: 1.03;
    letter-spacing: -1.5px;
    text-shadow: 0 4px 30px rgba(0,0,0,0.85);
    margin-bottom: 12px;
}}
.hero-artist {{
    font-size: 12px;
    color: #666;
    font-weight: 400;
    letter-spacing: 1.5px;
    margin-bottom: 18px;
    line-height: 1.5;
}}

/* ── Pills ── */
.pill-row {{ margin-bottom: 6px; }}
.pill {{
    display: inline-block;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 50px;
    padding: 5px 14px;
    font-size: 11px;
    font-weight: 600;
    color: #888;
    margin: 3px 4px 3px 0;
    letter-spacing: 0.3px;
}}

/* ── Section head ── */
.section-head {{
    display: flex;
    align-items: center;
    gap: 14px;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 4.5px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.38);
    margin: 38px 0 18px;
}}
.section-head::after {{
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.07);
}}

/* ── Featured single card ── */
.single-card {{
    background: linear-gradient(135deg, rgba(255,215,0,0.08), rgba(255,165,0,0.03));
    border: 1px solid rgba(255,215,0,0.25);
    border-radius: 16px;
    padding: 28px 30px;
    margin-bottom: 6px;
    text-align: center;
}}
.sc-tag    {{
    font-size: 9px; font-weight: 800; letter-spacing: 3.5px;
    text-transform: uppercase; color: rgba(255,215,0,0.60); margin-bottom: 12px;
}}
.sc-title  {{
    font-size: 40px; font-weight: 900; color: #FFD700;
    text-shadow: 0 2px 18px rgba(255,215,0,0.22); margin-bottom: 8px;
    line-height: 1.08; letter-spacing: -1.2px;
}}
.sc-artist {{ font-size: 13px; color: #666; font-weight: 400; }}

/* ── Preview label ── */
.preview-label {{
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.28);
    margin: 20px 0 8px;
    display: block;
}}

/* ── ZIP card ── */
.zip-card {{
    background: rgba(29,185,84,0.05);
    border: 1px solid rgba(29,185,84,0.18);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 12px;
}}
.zip-title {{ font-size: 15px; font-weight: 700; color: #e0e0e0; margin-bottom: 5px; }}
.zip-sub   {{ font-size: 12px; color: #555; margin: 0; }}

/* ── Track list header ── */
.track-header {{
    display: flex;
    align-items: center;
    padding: 10px 16px;
    background: rgba(29,185,84,0.12);
    border: 1px solid rgba(29,185,84,0.20);
    border-bottom: none;
    border-radius: 10px 10px 0 0;
    font-size: 8px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.50);
    gap: 12px;
}}
.th-num   {{ width: 30px; text-align: center; flex-shrink: 0; }}
.th-title {{ flex: 1; }}
.th-dl    {{ width: 90px; text-align: right; flex-shrink: 0; }}

/* ── Track number & title (inside columns) ── */
.t-num {{
    font-size: 12px;
    color: #444;
    font-weight: 600;
    text-align: center;
    margin: 0;
    padding: 14px 0;
    font-variant-numeric: tabular-nums;
}}
.t-title {{
    font-size: 14px;
    color: #ccc;
    font-weight: 500;
    margin: 0;
    padding: 14px 0 14px 4px;
    line-height: 1.3;
}}
.t-title.gold {{ color: #FFD700; font-weight: 700; }}
.single-badge {{
    display: inline-block;
    background: rgba(255,215,0,0.12);
    color: #c9a000;
    font-size: 7px;
    font-weight: 900;
    padding: 2px 7px;
    border-radius: 4px;
    margin-left: 8px;
    letter-spacing: 1px;
    text-transform: uppercase;
    vertical-align: middle;
    border: 1px solid rgba(255,215,0,0.25);
}}

/* ── Track rows container ── */
.track-border {{
    border: 1px solid rgba(255,255,255,0.06);
    border-top: none;
    border-radius: 0 0 10px 10px;
    overflow: hidden;
    margin-bottom: 2px;
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
    font-size: 12px !important;
    padding: 10px 22px !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 3px 16px rgba(29,185,84,0.32) !important;
    transition: all 0.22s ease !important;
    cursor: pointer !important;
    white-space: nowrap !important;
}}
.stDownloadButton > button:hover,
.stButton > button:hover {{
    background: linear-gradient(135deg, #22e060, #1db954) !important;
    box-shadow: 0 6px 24px rgba(29,185,84,0.58) !important;
    transform: translateY(-1px) !important;
}}

/* ── Expanders ── */
[data-testid="stExpander"] {{
    background: rgba(255,255,255,0.015) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 8px !important;
    margin-top: 2px !important;
    margin-bottom: 6px !important;
}}
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p {{
    font-size: 11px !important;
    color: #555 !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
}}

/* ── Footer ── */
.page-footer {{
    text-align: center;
    color: rgba(255,255,255,0.20);
    font-size: 11px;
    font-weight: 300;
    letter-spacing: 1.8px;
    margin-top: 60px;
    padding-top: 22px;
    border-top: 1px solid rgba(255,255,255,0.05);
}}

@media (max-width: 640px) {{
    .hero-title {{ font-size: 28px; letter-spacing: -0.8px; }}
    .sc-title   {{ font-size: 28px; }}
    .block-container {{ padding: 1.5rem 1rem 4rem !important; }}
    .th-dl {{ display: none; }}
}}
</style>
""", unsafe_allow_html=True)

# ── Content ────────

music_files = list_music()

st.markdown(
    f'<div class="launch-banner">'
    f"🎉 New Album Out Now &nbsp;·&nbsp; {ALBUM_NAME} &nbsp;·&nbsp; {ARTIST}"
    f"</div>",
    unsafe_allow_html=True,
)

# ── Hero ───────────

hcol1, hcol2 = st.columns([1, 1.75])

with hcol1:
    if os.path.exists("COVER.png"):
        st.markdown('<div class="cover-wrap">', unsafe_allow_html=True)
        st.image("COVER.png", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

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
        f'<span class="pill">📅 {YEAR}</span>'
        f'<span class="pill">⭐ {SINGLE_KEY}</span>'
        f"</div>",
        unsafe_allow_html=True,
    )

# # ── Featured single 

# single_file = next((f for f in music_files if song_title(f) == SINGLE_KEY), None)
# if single_file:
#     st.markdown('<p class="section-head">⭐ Featured Single</p>', unsafe_allow_html=True)
#     st.markdown(
#         f'<div class="single-card">'
#         f'<p class="sc-tag">⭐ Featured Single</p>'
#         f'<p class="sc-title">{SINGLE_KEY}</p>'
#         f'<p class="sc-artist">{ARTIST} &nbsp;·&nbsp; {YEAR}</p>'
#         f"</div>",
#         unsafe_allow_html=True,
#     )
#     audio_single = read_audio(single_file)
#     if audio_single:
#         st.markdown('<span class="preview-label">▶ Preview</span>', unsafe_allow_html=True)
#         scol1, scol2 = st.columns([1.8, 1])
#         with scol1:
#             st.audio(audio_single, format="audio/mpeg")
#         with scol2:
#             st.download_button(
#                 "⬇ Download Single",
#                 data=audio_single,
#                 file_name=f"{SINGLE_KEY}.mp3",
#                 mime="audio/mpeg",
#                 key="single_featured_dl",
#             )

# ── Download full album ───────────────────────────────────────────────────────

if music_files:
    st.markdown('<p class="section-head">📦 Download Full Album</p>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="zip-card">'
        f'<p class="zip-title">{ALBUM_NAME} — Complete Album</p>'
        f'<p class="zip-sub">{n} tracks &nbsp;·&nbsp; Download all in one ZIP file</p>'
        f"</div>",
        unsafe_allow_html=True,
    )
    zip_data = get_album_zip()
    if zip_data:
        _, zcol, _ = st.columns([1, 2, 1])
        with zcol:
            st.download_button(
                "⬇ Download All Songs (.zip)",
                data=zip_data,
                file_name=f"{ALBUM_NAME} — {ARTIST}.zip",
                mime="application/zip",
                key="album_zip_dl",
            )

# ── Track list ─────

st.markdown('<p class="section-head">🎵 All Tracks</p>', unsafe_allow_html=True)

st.markdown(
    '<div class="track-header">'
    '<span class="th-num">#</span>'
    '<span class="th-title">Title</span>'
    '<span class="th-dl">Download</span>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown('<div class="track-border">', unsafe_allow_html=True)

for i, fname in enumerate(music_files):
    title     = song_title(fname)
    is_single = title == SINGLE_KEY
    audio     = read_audio(fname)

    badge = '<span class="single-badge">Single</span>' if is_single else ""
    t_cls = "t-title gold" if is_single else "t-title"
    num   = "⭐" if is_single else str(i + 1)

    tc1, tc2, tc3 = st.columns([0.4, 3, 1.4])

    with tc1:
        st.markdown(f'<p class="t-num">{num}</p>', unsafe_allow_html=True)
    with tc2:
        st.markdown(f'<p class="{t_cls}">{title}{badge}</p>', unsafe_allow_html=True)
    with tc3:
        if audio:
            st.download_button(
                "⬇ Download",
                data=audio,
                file_name=f"{title}.mp3",
                mime="audio/mpeg",
                key=f"dl_track_{i}",
            )

    if audio:
        with st.expander(f"▶  Preview — {title}"):
            st.audio(audio, format="audio/mpeg")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f'<p class="page-footer">'
    f'© {YEAR} Adventist Imara Daima Youth Choir &nbsp;·&nbsp; {ALBUM_NAME}'
    f'</p>',
    unsafe_allow_html=True,
)
