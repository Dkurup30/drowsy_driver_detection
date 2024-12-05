import cv2
import dlib
from scipy.spatial import distance

#to calculate Eye Aspect Ratio(EAR)
def calculate_EAR(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear_aspect_ratio = (A+B)/(2.0*C)
	return ear_aspect_ratio

#initialize camera and models
cap = cv2.VideoCapture(0)               
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("Drowsiness-Detector-College-Project\shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat")

#detect drowsiness
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          #convert to grayscale

    faces = hog_face_detector(gray)
    for face in faces:                                      #detecting faces

        face_landmarks = dlib_facelandmark(gray, face)      #detecting landmarks for EAR
        leftEye = []
        rightEye = []

        for n in range(36,42):                              #left-eye landmarks
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x,y))
            next_point = n+1
            if n == 41:
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        for n in range(42,48):                              #right eye landmarks
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x,y))
            next_point = n+1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        #calculating EAR
        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)

        EAR = (left_ear+right_ear)/2
        EAR = round(EAR,2)

        #alert messages based on EAR
        if EAR<0.19: 
            cv2.putText(frame,"DROWSY",(20,100),
                        cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
            cv2.putText(frame,"Are you Sleepy?",(20,400),
                        cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
            print("Drowsy")
        print(EAR)

    cv2.imshow("Are you Sleepy?", frame)

    #press Esc key or close(X) button to exit
    key = cv2.waitKey(3)
    if key == 27 or cv2.getWindowProperty("Are you Sleepy?", cv2.WND_PROP_VISIBLE) < 1:
        break

#releasing resources
cap.release()
cv2.destroyAllWindows()