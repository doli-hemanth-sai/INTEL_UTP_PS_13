import streamlit as st
import cv2
from PIL import Image
import numpy as np
from ultralytics import YOLO
import pytesseract
import tempfile

# Function for license plate detection using YOLOv8
def detect_license_plate(image, model):
    results = model(image)
    detected_plates = []
    coordinates = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extract the bounding box coordinates
            plate_image = image[y1:y2, x1:x2]  # Crop the license plate from the image
            detected_plates.append(plate_image)
            coordinates.append((x1, y1, x2, y2))

    return detected_plates, coordinates

# Function for OCR using Tesseract
def recognize_license_plate(plate_image):
    result = pytesseract.image_to_string(plate_image, config='--oem 3 --psm 7')
    text_output = "".join(result.split()).replace(":", "").replace("-", "")
    return text_output.strip()

# Streamlit app
def main():
    st.title('License Plate Recognition')
    st.sidebar.title('Input Options')
    choice = st.sidebar.radio('Choose Input Type', ('Image', 'Video'))

    model_path = 'best100.pt'  # Update with your model path
    model = YOLO(model_path)

    if choice == 'Image':
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # Read image
            image = Image.open(uploaded_file)
            image_np = np.array(image)

            # Perform license plate detection
            detected_plates, coordinates = detect_license_plate(image_np, model)

            # Display detected plates and recognized text
            st.image(image, caption='Uploaded Image', use_column_width=True)
            for i, plate_image in enumerate(detected_plates):
                st.image(plate_image, caption=f'Detected Plate {i+1}', use_column_width=True)
                text_output = recognize_license_plate(plate_image)
                st.write(f"Detected License Plate Text {i+1}: {text_output}")

    elif choice == 'Video':
        uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
        if uploaded_video is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_video.read())

            # Open the video file
            cap = cv2.VideoCapture(tfile.name)
            stframe = st.empty()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Perform license plate detection on the frame
                detected_plates, coordinates = detect_license_plate(frame, model)

                # Draw bounding boxes on the frame
                for (x1, y1, x2, y2), plate_image in zip(coordinates, detected_plates):
                    text_output = recognize_license_plate(plate_image)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, text_output, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Convert frame to RGB format
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                stframe.image(frame_rgb, channels="RGB")

            cap.release()

if __name__ == '__main__':
    main()
