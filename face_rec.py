import cv2
import face_recognition
import serial
import time

# Set up serial communication with Arduino
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with the correct port for your Arduino
time.sleep(2)  # Wait for the serial connection to initialize

# Load the saved authorized face image and encode it
authorized_image = face_recognition.load_image_file("authorized_face.jpg")
authorized_encoding = face_recognition.face_encodings(authorized_image)[0]

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame from BGR (OpenCV format) to RGB (face_recognition format)
    rgb_frame = frame[:, :, ::-1]

    # Find all faces and their encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Check each detected face
    for face_encoding in face_encodings:
        # Compare the detected face encoding with the authorized encoding
        match = face_recognition.compare_faces([authorized_encoding], face_encoding, tolerance=0.6)

        if match[0]:  # If there is a match
            print("Authorized face detected!")
            arduino.write(b'1')  # Send '1' to Arduino to unlock the door
            time.sleep(5)  # Keep the door unlocked for 5 seconds
            arduino.write(b'0')  # Send '0' to Arduino to lock the door
            break
        else:
            print("Unauthorized face.")

    # Display the video feed with a bounding box around detected faces
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()

