import streamlit as st
import qrcode
from PIL import Image
import os
import base64

# App configuration
st.set_page_config(
    page_title="Wakati Wa Bwana Album Launch by Imara Daima Youth Choir",
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

# Cache QR code generation
@st.cache_resource(hash_funcs={str: lambda x: x})
def generate_qr_code(url, output_filename="qr_code.png", fill_color="#1db954", back_color="white"):
    try:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(output_filename)
        return output_filename
    except Exception as e:
        st.warning(f"Failed to generate QR code for {url}: {e}")
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
            margin: 0 10px;
        }}
        .image-container {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 25px;
        }}
        .qr-frame {{
            background: #ffffff;
            padding: 8px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            display: inline-block;
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
            max-width: 150px;
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
st.markdown('<h3 class="title">Wakati Wa Bwana by Imara Daima Youth Choir</h3>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Scan or download the QR codes to access our music album or single song, launching June 1st!</p>', unsafe_allow_html=True)

# QR code URLs
album_url = "https://wakatiwabwana-GTEzbTvcTBKERjhrbgiyerAN-album.streamlit.app/?page=download"
single_url = "https://wakatiwabwana-sffrwvytuiytkqVYUWTVIWUBR-single.streamlit.app/?page=download"

# Generate QR codes
qr_code_path = generate_qr_code(album_url, output_filename="album_qr_code.png")
single_qr_code_path = generate_qr_code(single_url, output_filename="single_qr_code.png", fill_color="black")

# Load QR code images
album_qr_image = Image.open(qr_code_path) if qr_code_path and os.path.exists(qr_code_path) else None
single_qr_image = Image.open(single_qr_code_path) if single_qr_code_path and os.path.exists(single_qr_code_path) else None

# Display album cover and QR codes
st.markdown('<div class="image-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1], gap="small")
with col1:
    if os.path.exists("COVER.png"):
        st.markdown('<div class="album-cover">', unsafe_allow_html=True)
        st.image("COVER.png", caption="Album Cover", use_container_width=True, output_format="PNG")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Album cover not found at 'COVER.png'. Please upload the file.")
with col2:
    if album_qr_image:
        st.markdown('<div class="qr-frame">', unsafe_allow_html=True)
        st.image(album_qr_image, caption="Scan for Album", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        with open(qr_code_path, "rb") as file:
            st.download_button(
                label="Album QR Code",
                data=file,
                file_name="album_qr_code.png",
                mime="image/png",
                key="album_qr_download",
                help="Download the QR code for the album",
                type="primary"
            )
    else:
        st.warning("Album QR code could not be loaded.")
with col3:
    if single_qr_image:
        st.markdown('<div class="qr-frame">', unsafe_allow_html=True)
        st.image(single_qr_image, caption="Scan for Single Song", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        with open(single_qr_code_path, "rb") as file:
            st.download_button(
                label="Single QR Code",
                data=file,
                file_name="single_qr_code.png",
                mime="image/png",
                key="single_qr_download",
                help="Download the QR code for the single song",
                type="primary"
            )
    else:
        st.warning("Single song QR code could not be loaded.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)