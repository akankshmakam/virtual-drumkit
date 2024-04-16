# import cv2
# import mediapipe as mp
# import pygame
# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
#
# # Initialize pygame
# pygame.init()
# drum_sound = pygame.mixer.Sound('bass_drum.wav')
# snare_sound = pygame.mixer.Sound('snaredrum.wav')
# cymbal = pygame.mixer.Sound('cymbal.wav')
# fingerclap = pygame.mixer.Sound('fingerclap.wav')
#
# mpHands = mp.solutions.hands
# hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)
# mpDraw = mp.solutions.drawing_utils
#
# cap = None
# is_running = False
#
# def start_webcam():
#     global cap, is_running
#     if not is_running:
#         cap = cv2.VideoCapture(0)
#         cap.set(3,1080)
#         cap.set(4,720)
#         cap.set(10,1000000)
#         is_running = True
#         update_webcam()
#
# def stop_webcam():
#     global cap, is_running
#     if is_running:
#         cap.release()
#         is_running = False
# def update_webcam():
#     global cap, is_running
#     if is_running:
#         ret, frame = cap.read()
#         x, y, c = frame.shape
#
#         frame = cv2.flip(frame, 1)
#
#         # Convert BGR to RGB
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#         result = hands.process(frame_rgb)
#
#         if result.multi_hand_landmarks:
#             for handslms in result.multi_hand_landmarks:
#                 landmarks = []
#                 for lm in handslms.landmark:
#                     lmx = int(lm.x * 640)
#                     lmy = int(lm.y * 480)
#                     landmarks.append([lmx, lmy])
#                 mpDraw.draw_landmarks(frame_rgb, handslms, mpHands.HAND_CONNECTIONS)  # Draw landmarks on RGB image
#
#                 thumb = landmarks[4]
#                 fore_finger = landmarks[8]
#                 middle_finger = landmarks[12]
#                 ring_finger = landmarks[16]
#                 little_finger = landmarks[20]
#                 thumb_x, thumb_y = thumb
#                 fore_finger_x, fore_finger_y = fore_finger
#                 middle_finger_x, middle_finger_y = middle_finger
#                 ring_finger_x, ring_finger_y = ring_finger
#                 little_finger_x, little_finger_y = little_finger
#
#                 thumb_fore_distance = ((thumb_x - fore_finger_x) ** 2 + (thumb_y - fore_finger_y) ** 2) ** 0.5
#                 thumb_middle_distance = ((thumb_x - middle_finger_x) ** 2 + (thumb_y - middle_finger_y) ** 2) ** 0.5
#                 thumb_ring_distance = ((thumb_x - ring_finger_x) ** 2 + (thumb_y - ring_finger_y) ** 2) ** 0.5
#                 thumb_little_distance = ((thumb_x - little_finger_x) ** 2 + (thumb_y - little_finger_y) ** 2) ** 0.5
#
#                 if thumb_fore_distance < 20:  # Adjust the threshold as needed
#                     drum_sound.play()
#                 elif thumb_middle_distance < 20:  # Adjust the threshold as needed
#                     snare_sound.play()
#                 elif thumb_ring_distance < 20:  # Adjust the threshold as needed
#                     cymbal.play()
#                 elif thumb_little_distance < 20:  # Adjust the threshold as needed
#                     fingerclap.play()
#
#         # Convert the frame to tkinter format
#         img = Image.fromarray(frame_rgb)
#         imgtk = ImageTk.PhotoImage(image=img)
#
#         # Update the label with the new frame
#         label.imgtk = imgtk
#         label.configure(image=imgtk)
#
#         if cv2.waitKey(1) == ord('q'):
#             stop_webcam()
#         else:
#             root.after(10, update_webcam)
#     else:
#         cv2.destroyAllWindows()
#
# root = tk.Tk()
# root.title("Hand Gesture Drum Kit")
# root.geometry("1080x720")
#
# start_button = tk.Button(root, text="Start Webcam", command=start_webcam)
# start_button.pack()
#
# stop_button = tk.Button(root, text="Stop Webcam", command=stop_webcam)
# stop_button.pack()
#
# def show_guidelines():
#     messagebox.showinfo("Guidelines", "Show guidelines here")
#
# guidelines_button = tk.Button(root, text="Guidelines", command=show_guidelines)
# guidelines_button.pack()
#
# # Create a label to display the webcam feed
# label = tk.Label(root)
# label.pack()
#
# root.mainloop()

import cv2
import mediapipe as mp
import pygame
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize pygame
pygame.init()
drum_sound = pygame.mixer.Sound('bass_drum.wav')
snare_sound = pygame.mixer.Sound('snaredrum.wav')
cymbal = pygame.mixer.Sound('cymbal.wav')
fingerclap = pygame.mixer.Sound('fingerclap.wav')

mpHands = mp.solutions.hands

hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

cap = None
is_running = False

def start_webcam():
    global cap, is_running
    if not is_running:
        cap = cv2.VideoCapture(0)
        cap.set(3,1080)
        cap.set(4,720)
        cap.set(10,1000000)
        is_running = True
        update_webcam()

def stop_webcam():
    global cap, is_running
    if is_running:
        cap.release()
        is_running = False

def update_webcam():
    global cap, is_running
    if is_running:
        ret, frame = cap.read()
        x, y, c = frame.shape

        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for handslms in result.multi_hand_landmarks:
                landmarks = []
                for lm in handslms.landmark:
                    lmx = int(lm.x * 640)
                    lmy = int(lm.y * 480)
                    landmarks.append([lmx, lmy])
                mpDraw.draw_landmarks(frame_rgb, handslms, mpHands.HAND_CONNECTIONS)

                thumb = landmarks[4]
                fore_finger = landmarks[8]
                middle_finger = landmarks[12]
                ring_finger = landmarks[16]
                little_finger = landmarks[20]
                thumb_x, thumb_y = thumb
                fore_finger_x, fore_finger_y = fore_finger
                middle_finger_x, middle_finger_y = middle_finger
                ring_finger_x, ring_finger_y = ring_finger
                little_finger_x, little_finger_y = little_finger

                thumb_fore_distance = ((thumb_x - fore_finger_x) ** 2 + (thumb_y - fore_finger_y) ** 2) ** 0.5
                thumb_middle_distance = ((thumb_x - middle_finger_x) ** 2 + (thumb_y - middle_finger_y) ** 2) ** 0.5
                thumb_ring_distance = ((thumb_x - ring_finger_x) ** 2 + (thumb_y - ring_finger_y) ** 2) ** 0.5
                thumb_little_distance = ((thumb_x - little_finger_x) ** 2 + (thumb_y - little_finger_y) ** 2) ** 0.5

                if thumb_fore_distance < 20:
                    drum_sound.play()
                elif thumb_middle_distance < 20:
                    snare_sound.play()
                elif thumb_ring_distance < 20:
                    cymbal.play()
                elif thumb_little_distance < 20:
                    fingerclap.play()

        # Convert the frame to tkinter format
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the label with the new frame
        label.imgtk = imgtk
        label.configure(image=imgtk)

        if cv2.waitKey(1) == ord('q'):
            stop_webcam()
        else:
            root.after(10, update_webcam)
    else:
        cv2.destroyAllWindows()

def show_guidelines():
    guidelines = """
    1. Click "Start Webcam" to activate the webcam.
    2. Show your hand to trigger drum sounds based on gestures.
    3. Use fist for bass drum, index finger for snare drum, etc.
    4. Click "Stop Webcam" to deactivate the webcam and stop sounds.
    5. Adjust webcam position and lighting for better detection.
    6. Have fun experimenting with different gestures to create music!
    """
    messagebox.showinfo("Guidelines", guidelines)

root = tk.Tk()
root.title("Hand Gesture Drum Kit")
root.geometry("1080x720")

start_button = tk.Button(root, text="Start Webcam", command=start_webcam)
start_button.pack()

stop_button = tk.Button(root, text="Stop Webcam", command=stop_webcam)
stop_button.pack()

guidelines_button = tk.Button(root, text="Guidelines", command=show_guidelines)
guidelines_button.pack()


label = tk.Label(root)
label.pack()

root.mainloop()
