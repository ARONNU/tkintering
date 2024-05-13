import datetime
import csv
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

now = datetime.datetime.now()
current_date = now.strftime('%Y-%m-%d')
current_time = now.strftime('%H:%M:%S')

def read_attendance_data():
    attendance_data = []
    with open(f'/home/thesis/Face-Recognition-with-YOLO-and-FaceNet/{current_date}.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            attendance_data.append(row)
    return attendance_data

def display_attendance(data):
    for index, row in enumerate(data, start=1):
        name_label = tk.Label(canvas_frame, text=row['Name'], bg='#EEEEEE', padx=40, pady=20)
        type_label = tk.Label(canvas_frame, text=row['Type'], bg='#EEEEEE', padx=40, pady=20)
        date_label = tk.Label(canvas_frame, text=row['Date'], bg='#EEEEEE', padx=40, pady=20)
        time_label = tk.Label(canvas_frame, text=row['Time'], bg='#EEEEEE', padx=40, pady=20)
        name_label.grid(row=index, column=0, sticky='nsew')
        type_label.grid(row=index, column=1, sticky='nsew')
        date_label.grid(row=index, column=2, sticky='nsew')
        time_label.grid(row=index, column=3, sticky='nsew')

    canvas_frame.update_idletasks()  # Update the canvas to compute the scrollable region
    canvas.config(scrollregion=canvas.bbox("all"))  # Set the scroll region

    # Create a bar chart for attendance types
    types = [row['Type'] for row in data]
    type_counts = {t: types.count(t) for t in set(types)}
    plt.figure(figsize=(6, 4))
    plt.bar(type_counts.keys(), type_counts.values())
    plt.xlabel('Attendance Type')
    plt.ylabel('Count')
    plt.title('Attendance Types')
    plt.tight_layout()

    # Embed the Matplotlib plot in the GUI
    graph_canvas = FigureCanvasTkAgg(plt.gcf(), window)
    graph_canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True)

    # Add labels for current date and time at the bottom
    date_time_frame = tk.Frame(window)
    date_label = tk.Label(date_time_frame, text=f'Current Date: {current_date}')
    time_label = tk.Label(date_time_frame, text=f'Current Time: {current_time}')
    date_label.pack(side='left')
    time_label.pack(side='right')
    date_time_frame.pack(side='bottom')

window = tk.Tk()
window.minsize(640, 480)
window.title(f'Attendance Logs for {current_date}')

# Create a canvas widget with a vertical scrollbar
canvas = tk.Canvas(window)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas for the scrollable content
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

attendance_data = read_attendance_data()
display_attendance(attendance_data)

window.mainloop()
