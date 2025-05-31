import streamlit as st
import os
import base64

# App configuration
st.set_page_config(
    page_title="Wakati Wa Bwana Album by Imara Daima Youth Choir",
    page_icon="COVER.png" if os.path.exists("COVER.png") else "🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

# Cache base64 image encoding
@st.cache_resource
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# Cache MP3 file listing
@st.cache_data
def get_mp3_files(song_folder="."):
    try:
        return sorted([f for f in os.listdir(song_folder) if f.endswith(".mp3")])
    except FileNotFoundError:
        return []

# CSS styling
background_image = get_base64_image("COVER.png")
if background_image:
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
        .main {{
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(data:image/png;base64,{background_image});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            padding: 30px;
            border-radius: 15px;
            max-width: 900px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            color: #ffffff;
            font-family: 'Montserrat', sans-serif;
        }}
        .title {{
            font-size: 40px;
            color: #ffffff;
            text-align: center;
            font-weight: 700;
            margin-bottom: 12px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}
        .subtitle {{
            font-size: 18px;
            color: #e0e0e0;
            text-align: center;
            margin-bottom: 25px;
            font-weight: 300;
        }}
        .footer {{
            font-size: 12px;
            color: #b0b0b0;
            text-align: center;
            margin-top: 30px;
            font-weight: 300;
        }}
        .spotify-header {{
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            padding: 12px;
            background: #1db954;
            font-weight: 600;
            font-size: 14px;
            color: #ffffff;
            border-radius: 8px 8px 0 0;
            border-bottom: 2px solid #17a34a;
        }}
        .spotify-row {{
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            padding: 12px;
            border-bottom: 1px solid #e0e0e0;
            font-size: 14px;
            color: #333333;
            background: #f9f9f9;
            transition: background 0.3s ease;
        }}
        .spotify-row:hover {{
            background: #e6f3eb;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}
        .title-column {{
            flex: 1;
            text-align: left;
            color: #333333;
        }}
        .button-column {{
            width: 80px;
            text-align: right;
        }}
        button.download-button {{
            background: linear-gradient(45deg, #1db954, #17a34a) !important;
            color: white !important;
            padding: 8px 10px;
            border-radius: 20px;
            border: none;
            font-size: 12px;
            cursor: pointer;
            width: 60px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transition: background 0.3s ease;
        }}
        button.download-button:hover {{
            background: linear-gradient(45deg, #17a34a, #1db954) !important;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
        }}
        .album-cover {{
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            border: 2px solid #ffffff;
            display: block;
            margin: 0 10px;
        }}
        .image-container {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 25px;
        }}
        [data-testid="stSidebar"] {{display: none;}}
        @media (max-width: 600px) {{
            .main {{padding: 20px;}}
            .title {{font-size: 32px;}}
            .subtitle {{font-size: 16px;}}
            .image-container {{flex-direction: column; align-items: center; gap: 10px;}}
            .album-cover {{margin: 5px 0; width: 150px;}}
            .spotify-header {{font-size: 13px; padding: 10px;}}
            .spotify-row {{flex-direction: column; align-items: flex-start; padding: 10px; font-size: 13px;}}
            .title-column, .button-column {{width: 100%; text-align: left; margin-bottom: 8px;}}
            button.download-button {{width: 100%; font-size: 12px; padding: 8px 10px;}}
        }}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        [data-testid="stToolbar"] {{visibility: hidden;}}
        [data-testid="stDecoration"] {{visibility: hidden;}}
        [data-testid="stFooter"] {{display: none;}}
        .streamlit-footer {{display: none;}}
        .css-1v3fvcr {{display: none;}}
        .css-1v0mbdj img {{display: none;}}
        .css-1v0mbdj {{display: none;}}
        </style>
        """,
        unsafe_allow_html=True
    )

# Main content
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">Asante na ubarikiwe!</h1>', unsafe_allow_html=True)
st.markdown("#### Wakati Wa Bwana Album by Imara Daima Youth Choir", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Download Wakati Wa Bwana Album Songs Below</p>', unsafe_allow_html=True)

# Display album cover and logo
st.markdown('<div class="image-container">', unsafe_allow_html=True)
if os.path.exists("COVER.png") and os.path.exists("LOGO.png"):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="album-cover">', unsafe_allow_html=True)
        st.image("COVER.png", width=370, output_format="PNG")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="album-cover">', unsafe_allow_html=True)
        st.image("LOGO.png", width=370, output_format="PNG")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    if not os.path.exists("COVER.png"):
        st.warning("Album cover not found at 'COVER.png'. Please upload the file.")
    if not os.path.exists("LOGO.png"):
        st.warning("Logo not found at 'LOGO.png'. Please upload the file.")
st.markdown('</div>', unsafe_allow_html=True)

# List songs
st.markdown("### Song List", unsafe_allow_html=True)
mp3_files = get_mp3_files(".")
if mp3_files:
    st.markdown(
        '<div class="spotify-header">'
        '<div class="title-column">Song Title</div>'
        '<div class="button-column">Download</div>'
        '</div>',
        unsafe_allow_html=True
    )
    for index, file in enumerate(mp3_files):
        title = os.path.splitext(file)[0].replace("_", " ").title()
        full_path = os.path.join(".", file)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                st.markdown('<div class="spotify-row">', unsafe_allow_html=True)
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f'<div class="title-column">{title}</div>', unsafe_allow_html=True)
                with col2:
                    st.download_button(
                        label="Download",
                        data=f,
                        file_name=file,
                        mime="audio/mpeg",
                        key=f"song_{index}",
                        help=f"Download {title}",
                        type="primary"
                    )
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="spotify-row">'
                f'<div class="title-column">{title}</div>'
                f'<div class="button-column">Not found</div>'
                f'</div>',
                unsafe_allow_html=True
            )
else:
    st.warning("No songs found in the current directory. Please ensure MP3 files are present.")

st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)