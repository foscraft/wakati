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
    initial_sidebar_state="collapsed",  # Sidebar collapsed by default
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Encode image as base64 for background
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# CSS for styling, hiding sidebar, and styling download buttons
background_image = get_base64_image("COVER.png")
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
        width: 120px; /* Wider for longer buttons */
        text-align: right;
    }}
    .download-button button {{
        background: linear-gradient(45deg, #1db954, #17a34a) !important;
        color: white !important;
        padding: 12px 20px; /* Increased padding */
        border-radius: 25px;
        border: none;
        font-size: 14px; /* Larger font size */
        cursor: pointer;
        width: 120px; /* Wider button */
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: background 0.3s ease;
    }}
    .qr-download-button button {{
        background: linear-gradient(45deg, #1db954, #17a34a) !important;
        color: white !important;
        padding: 12px 20px; /* Increased padding */
        border-radius: 25px;
        border: none;
        font-size: 14px; /* Larger font size */
        cursor: pointer;
        width: 100%; /* Full-width for QR buttons */
        max-width: 200px; /* Limit max width */
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: background 0.3s ease;
    }}
    .download-button button:hover, .qr-download-button button:hover {{
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
    .qr-frame {{
        background: #ffffff;
        padding: 8px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        display: inline-block;
    }}
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {{
        display: none;
    }}
    @media (max-width: 600px) {{
        .main {{
            padding: 20px;
        }}
        .title {{
            font-size: 32px;
        }}
        .subtitle {{
            font-size: 16px;
        }}
        .image-container {{
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }}
        .album-cover {{
            margin: 5px 0;
            width: 150px;
        }}
        .spotify-header {{
            font-size: 13px;
            padding: 10px;
        }}
        .spotify-row {{
            flex-direction: column;
            align-items: flex-start;
            padding: 10px;
            font-size: 13px;
        }}
        .title-column, .button-column {{
            width: 100%;
            text-align: left;
            margin-bottom: 8px;
        }}
        .download-button button {{
            width: 100%;
            font-size: 13px;
            padding: 10px 15px;
        }}
        .qr-download-button button {{
            width: 100%;
            font-size: 13px;
            padding: 10px 15px;
        }}
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

# Helper to generate QR code for full album (green)
def generate_qr_code(url, fill_color="#1db954", back_color="white", output_filename="qr_code.png"):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_filename)
    return output_filename

# Helper to generate black QR code for single song
def generate_single_song_qr_code(song_url, output_filename="wakati_wa_bwana_qr_code.png"):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(song_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)
    return output_filename

# Determine page based on URL path and query
query_params = st.query_params
path = query_params.get("page", None)
query = query_params.get("query", None)

# Map paths to pages, only if query=download
if path == "wakati-wa-bwana-full-album-access-2025" and query == "download":
    page = "Download Wakati Wa Bwana"
elif path == "wakati-wa-bwana-single-track-access-2025" and query == "download":
    page = "Download Single Song"
else:
    page = "Home"

# Pages
if page == "Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h3 class="title">Wakati Wa Bwana by Imara Daima Youth Choir</h3>', unsafe_allow_html=True)
    st.markdown("#### `Scan or download the QR codes to access our music content, launching June 1st!`", unsafe_allow_html=True)

    # Generate and show both QR codes with long URLs ending in ?query=download
    download_page_url = "https://wakatiwabwana-album.streamlit.app/wakati-wa-bwana-full-album-access-2025/?page=wakati-wa-bwana-full-album-access-2025&query=download"
    single_song_url = "https://wakatiwabwana-album.streamlit.app/wakati-wa-bwana-single-track-access-2025/?page=wakati-wa-bwana-single-track-access-2025&query=download"
    qr_code_path = generate_qr_code(download_page_url, fill_color="#1db954", output_filename="qr_code.png")
    single_qr_code_path = generate_single_song_qr_code(single_song_url, output_filename="wakati_wa_bwana_qr_code.png")
    qr_image = Image.open(qr_code_path)
    single_qr_image = Image.open(single_qr_code_path)

    # Show album cover and both QR codes
    col1, col2, col3 = st.columns(3)
    with col1:
        if os.path.exists("COVER.png"):
            st.markdown('<div class="album-cover">', unsafe_allow_html=True)
            st.image("COVER.png", caption="Album Cover", use_container_width=True, output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("Album cover not found at 'COVER.png'. Please upload the file.")
    with col2:
        st.markdown('<div class="qr-frame">', unsafe_allow_html=True)
        st.image(qr_image, caption="Scan for Music Content", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="qr-download-button">', unsafe_allow_html=True)
        st.download_button(
            label="Album QR Code",
            data=open(qr_code_path, "rb"),
            file_name="music_content_qr_code.png",
            mime="image/png",
            key="qr_download",
            help="Download the QR code for music content",
            type="primary"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="qr-frame">', unsafe_allow_html=True)
        st.image(single_qr_image, caption="Scan for Special Track", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="qr-download-button">', unsafe_allow_html=True)
        st.download_button(
            label="Single QR Code",
            data=open(single_qr_code_path, "rb"),
            file_name="special_track_qr_code.png",
            mime="image/png",
            key="single_song_qr_download",
            help="Download the QR code for the special track",
            type="primary"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Download Wakati Wa Bwana":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown("## `Download Wakati Wa Bwana`", unsafe_allow_html=True)
    st.markdown("#### `Wakati Wa Bwana Album by Imara Daima Youth Choir`", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Explore and download individual songs or the full album.</p>', unsafe_allow_html=True)

    # Center the album cover and logo side by side
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    if os.path.exists("COVER.png") and os.path.exists("LOGO.png"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="album-cover">', unsafe_allow_html=True)
            st.image("COVER.png", caption="Wakati Wa Bwana Cover", width=200, output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="album-cover">', unsafe_allow_html=True)
            st.image("LOGO.png", caption="Imara Daima Youth Choir Logo", width=200, output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        if not os.path.exists("COVER.png"):
            st.error("Album cover not found at 'COVER.png'. Please upload the file.")
        if not os.path.exists("LOGO.png"):
            st.error("Logo not found at 'LOGO.png'. Please upload the file.")
    st.markdown('</div>', unsafe_allow_html=True)

    # List songs in a table-like layout
    st.markdown("### `Song List`", unsafe_allow_html=True)
    song_folder = "."
    mp3_files = [f for f in os.listdir(song_folder) if f.endswith(".mp3")] if os.path.exists(song_folder) else []

    if mp3_files:
        # Header
        st.markdown(
            '<div class="spotify-header">'
            '<div class="title-column">Song Title</div>'
            '<div class="button-column">Download</div>'
            '</div>',
            unsafe_allow_html=True
        )
        # Rows
        for index, file in enumerate(sorted(mp3_files)):
            title = os.path.splitext(file)[0].replace("_", " ").title()
            full_path = os.path.join(song_folder, file)
            if os.path.exists(full_path):
                with open(full_path, "rb") as f:
                    st.markdown('<div class="spotify-row">', unsafe_allow_html=True)
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f'<div class="title-column">{title}</div>', unsafe_allow_html=True)
                    with col2:
                        st.markdown('<div class="download-button">', unsafe_allow_html=True)
                        st.download_button(
                            label="Download Song",
                            data=f,
                            file_name=file,
                            mime="audio/mpeg",
                            key=f"song_{index}",
                            help=f"Download {title}",
                            type="primary"
                        )
                        st.markdown('</div>', unsafe_allow_html=True)
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
        st.error("No songs found in the current folder. Please ensure the folder exists and contains MP3 files.")

    st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Download Single Song":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown("## `Download Wakati Wa Bwana Single`", unsafe_allow_html=True)
    st.markdown("#### `Wakati Wa Bwana by Imara Daima Youth Choir`", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Download the single song "Wakati Wa Bwana".</p>', unsafe_allow_html=True)

    # Center the album cover
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    if os.path.exists("COVER.png"):
        st.markdown('<div class="album-cover">', unsafe_allow_html=True)
        st.image("COVER.png", caption="Wakati Wa Bwana Cover", width=200, output_format="PNG")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Album cover not found at 'COVER.png'. Please upload the file.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Download button for the single song
    song_file = "Wakati Wa Bwana.mp3"
    if os.path.exists(song_file):
        st.markdown('<div class="download-button">', unsafe_allow_html=True)
        st.download_button(
            label="Download Wakati Wa Bwana",
            data=open(song_file, "rb"),
            file_name="Wakati Wa Bwana.mp3",
            mime="audio/mpeg",
            key="single_song_download",
            help="Download Wakati Wa Bwana",
            type="primary"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Song 'Wakati Wa Bwana.mp3' not found. Please ensure the file exists.")

    st.markdown('<p class="footer">Presented by Imara Daima Youth Choir © 2025</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)