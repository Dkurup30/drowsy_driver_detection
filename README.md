<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>Driver Drowsiness Detection System</h1>

  <p>This project is designed to monitor a driver's facial features and detect signs of drowsiness using computer vision techniques. When drowsiness is detected, the system alerts the driver to prevent potential accidents.</p>

  <h2>Features</h2>
  <ul>
    <li>Detects facial landmarks using Dlib’s pre-trained model.</li>
    <li>Calculates Eye Aspect Ratio (EAR) using Euclidean distance.</li>
    <li>Alerts the driver when drowsiness is detected.</li>
    <li>Real-time video processing using OpenCV.</li>
  </ul>

  <h2>Dataset / Model Used</h2>
  <p>
    Uses <a href="http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2" target="_blank">
    shape_predictor_68_face_landmarks.dat.bz2</a> — a pre-trained model that detects 68 facial landmarks.
    Download and extract the file in the project directory.
  </p>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>OpenCV (cv2)</li>
    <li>Dlib</li>
    <li>SciPy</li>
  </ul>
  <pre><code>pip install opencv-python dlib scipy</code></pre>

  <h2>How to Run</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
      </code></pre>
    </li>
    <li>Run the script:
      <pre><code>python Drowsiness-Detector-College-Project/myenv/src/code_1.py</code></pre>
    </li>
  </ol>

  <h2>Drowsiness Detection Logic</h2>
  <p>Calculates Eye Aspect Ratio (EAR) using Euclidean distance. If EAR stays below a threshold for a given number of frames, the system raises an alert.</p>



</body>
</html>
