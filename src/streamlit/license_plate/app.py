import streamlit as st
from PIL import Image
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

@st.cache(allow_output_mutation=True)
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("DunnBC22/trocr-base-printed_license_plates_ocr")
    model = AutoModelForTokenClassification.from_pretrained("DunnBC22/trocr-base-printed_license_plates_ocr")
    return tokenizer, model

def recognize_license_plate(tokenizer, model, image):
    inputs = tokenizer(image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_ids = torch.argmax(outputs.logits, dim=-1)
    text_output = tokenizer.decode(predicted_ids[0], skip_special_tokens=True)
    return text_output

def main():
    st.title('License Plate OCR')
    tokenizer, model = load_model()

    st.sidebar.title('Input Options')
    choice = st.sidebar.radio('Choose Input Type', ('Upload Image', 'Use Webcam'))

    if choice == 'Upload Image':
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image', use_column_width=True)
                text_output = recognize_license_plate(tokenizer, model, image)
                st.write(f"Detected License Plate Text: {text_output}")
            except Exception as e:
                st.write("Error processing image:", e)

    elif choice == 'Use Webcam':
        st.warning("Webcam support is not implemented in this example.")

if __name__ == '__main__':
    main()
