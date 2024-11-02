import cv2
from playsound import playsound

# Initialize the webcam
cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

distracted_counter = 0
distracted_threshold = 30

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        distracted_counter = 0  # Reset counter if a face is detected
    else:
        distracted_counter += 1  # Increment counter if no face is detected
        if distracted_counter > distracted_threshold:
            print("You seem to be distracted!")
            playsound('Motivation_Quickie.mp3')

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Check if the frame was captured correctly
    if not ret:
        print("Failed to grab frame")
        break

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture object and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()