import face_recognition
import cv2
import pickle

# Capture the authorized face
cap = cv2.VideoCapture(0)
print("Press 's' to save the authorized face and 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Authorized Face", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        # Save and encode the authorized face
        face_encoding = face_recognition.face_encodings(frame)[0]
        with open("authorized_face.pkl", "wb") as f:
            pickle.dump(face_encoding, f)
        print("Authorized face saved and encoded!")
        break
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
