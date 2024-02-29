import streamlit as st
from PIL import Image

st.title("Image to Grayscale Convertor")
st.write("Upload your image and see what happen😊")
uploaded_image = st.file_uploader("Upload Image")
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)


def main():
    st.title("Camera App with Grayscale Conversion")

    with st.expander("Camera Settings"):
        # Option to start the camera
        start_camera = st.checkbox("Start Camera")

        if start_camera:
            # Camera input
            image = st.camera_input("Capture Image", key="camera_input")

            if image:
                # Convert the captured image to grayscale
                grayscale_image = convert_to_grayscale(image)
                st.image(grayscale_image, caption="Grayscale Snapshot", use_column_width=True)

    st.markdown("---")

    st.header("Instructions:")
    st.write("1. Click 'camera setting' to show Start Camera.")
    st.write("2. Check 'Start Camera' to activate the camera input.")
    st.write("3. Use the 'Take Photo' button to capture a grayscale image.")


# Your existing code ...

# Footer styling
footer_style = """
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f1f1f1;
    }
</style>
"""

# Display the footer
st.markdown(footer_style, unsafe_allow_html=True)
st.markdown("<div class='footer'>&copy; 2024 @dan-kingo.</div>", unsafe_allow_html=True)


def convert_to_grayscale(image):
    # Create a pillow image instance
    imgs = Image.open(image)
    # Convert the image to grayscale
    grayscale_image = imgs.convert("L")
    return grayscale_image


if __name__ == "__main__":
    main()
