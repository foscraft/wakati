import streamlit as st
import os
import base64

# App configuration
st.set_page_config(
    page_title="Wakati Wa Bwana Single by Imara Daima Youth Choir",
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
        .album-cover {{
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            border: 2px solid #ffffff;
            display: block;
            margin: 0 auto;
        }}
        .image-container {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 25px;
        }}
        button.download-button {{
            background: linear-gradient(45deg, #1db954, #17a34a) !important;
            color: white !important;
            padding: 8px 10px;
            border-radius: 20px;
            border: none;
            font-size: 12px;
            cursor: pointer;
            width: 100%;
            max-width: 200px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transition: background 0.3s ease;
        }}
        button.download-button:hover {{
            background: linear-gradient(45deg, #17a34a, #1db954) !important;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
        }}
        [data-testid="stSidebar"] {{display: none;}}
        @media (max-width: 600px) {{
            .main {{padding: 20px;}}
            .title {{font-size: 32px;}}
            .subtitle {{font-size: 16px;}}
            .image-container {{flex-direction: column; align-items: center; gap: 10px;}}
            .album-cover {{margin: 5px 0; width: 150px;}}
            button.download-button {{font-size: 12px; padding: 8px 10px;}}
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
st.markdown("#### `Wakati Wa Bwana by Imara Daima Youth Choir`", unsafe_allow_html=True)
st.markdown("##### `Download Wakati Wa Bwana Single Below`", unsafe_allow_html=True)


# Display album cover
st.markdown('<div class="image-container">', unsafe_allow_html=True)
if os.path.exists("COVER.png"):
    st.markdown('<div class="album-cover">', unsafe_allow_html=True)
    st.image("COVER.png", caption="Wakati Wa Bwana Cover", width=370, output_format="PNG")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("Album cover not found at 'COVER.png'. Please upload the file.")
st.markdown('</div>', unsafe_allow_html=True)

# Download button for single song
song_file = "Wakati Wa Bwana.mp3"
if os.path.exists(song_file):
    with open(song_file, "rb") as f:
        st.download_button(
            label="Download Wakati Wa Bwana",
            data=f,
            file_name="Wakati Wa Bwana.mp3",
            mime="audio/mpeg",
            key="single_song_download",
            help="Download Wakati Wa Bwana",
            type="primary"
        )
else:
    st.warning("Song 'Wakati Wa Bwana.mp3' not found. Please ensure the file exists.")

st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)