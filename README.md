# Suspect-Detection-using-facial-recognition


The Suspect Recognition System is a Python-based application designed to identify a suspect from existing image files and real-time feeds. If a suspect is recognized, the system automatically sends an email notification to the admin using SMTP.

Features
Image-Based Recognition:
Compares a given image with the database of suspect images.

Real-Time Recognition:
Uses live video feeds to detect suspects and trigger alerts.

Email Notifications:
Sends an automated email to the admin with details and optionally attaches the detected image.

User-Friendly Visualization:
Utilizes Matplotlib to visualize image comparisons and recognition results.

Technologies Used
Programming Language: Python
Image Processing: OpenCV
Visualization: Matplotlib
Email Service: smtplib
Face Recognition: face_recognition library (or OpenCV's DNN module)
