import datetime
import csv
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import subprocess

now = datetime.datetime.now()
current_date = now.strftime('%Y-%m-%d')

def read_attendance_data():
    attendance_data = []
    with open(f'/home/thesis/Face-Recognition-with-YOLO-and-FaceNet/{current_date}.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            attendance_data.append(row)
    return attendance_data

def display_attendance(data):
    index = 1
    for row in data:
        name_label = tk.Label(window, text=row['Name'], bg='#EEEEEE', padx=10, pady=5)
        type_label = tk.Label(window, text=row['Type'], bg='#EEEEEE', padx=10, pady=5)
        date_label = tk.Label(window, text=row['Date'], bg='#EEEEEE', padx=10, pady=5)
        time_label = tk.Label(window, text=row['Time'], bg='#EEEEEE', padx=10, pady=5)
        name_label.grid(row=index, column=0, sticky='nsew')
        type_label.grid(row=index, column=1, sticky='nsew')
        date_label.grid(row=index, column=2, sticky='nsew')
        time_label.grid(row=index, column=3, sticky='nsew')
        index += 1

    name_header = tk.Label(window, text='Name', bg='#151515', fg='#EEEEEE', padx=10, pady=5)
    type_header = tk.Label(window, text='Type', bg='#151515', fg='#EEEEEE', padx=10, pady=5)
    date_header = tk.Label(window, text='Date', bg='#151515', fg='#EEEEEE', padx=10, pady=5)
    time_header = tk.Label(window, text='Time', bg='#151515', fg='#EEEEEE', padx=10, pady=5)
    name_header.grid(row=0, column=0, sticky='nsew')
    type_header.grid(row=0, column=1, sticky='nsew')
    date_header.grid(row=0, column=2, sticky='nsew')
    time_header.grid(row=0, column=3, sticky='nsew')

    # Add grid lines
    for i in range(index):
        window.grid_rowconfigure(i, minsize=1)
        window.grid_columnconfigure(i, minsize=1)

def open_script():
    script_directory = '/path/to/your/script_directory'
    script_filepath = os.path.join(script_directory, 'your_script.py')
    subprocess.Popen(['python', script_filepath])

def capture_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('OpenCV Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

window = tk.Tk()
window.minsize(640, 480)
window.title(f'Attendance Logs for {current_date}')

# Configure grid row and column weights for resizing
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
window.grid_rowconfigure(0, weight=1)

attendance_data = read_attendance_data()

display_attendance(attendance_data)

# Add a button overlaying the upper right part of the screen
open_script_button = tk.Button(window, text="Open Script", command=open_script, bg='#C73659', fg='#EEEEEE')
open_script_button.place(relx=1, rely=0, anchor='ne', x=-10, y=10)

# Add a button to start capturing video using OpenCV
capture_video_button = tk.Button(window, text="Capture Video", command=capture_video, bg='#A91D3A', fg='#EEEEEE')
capture_video_button.place(relx=0.5, rely=1, anchor='s', y=-10)

window.mainloop()
