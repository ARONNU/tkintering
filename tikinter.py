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
        name_label = tk.Label(attendance_frame, text=row['Name'], bg='#EEEEEE', padx=20, pady=10)
        type_label = tk.Label(attendance_frame, text=row['Type'], bg='#EEEEEE', padx=20, pady=10)
        date_label = tk.Label(attendance_frame, text=row['Date'], bg='#EEEEEE', padx=20, pady=10)
        time_label = tk.Label(attendance_frame, text=row['Time'], bg='#EEEEEE', padx=20, pady=10)
        name_label.grid(row=index, column=0, sticky='nsew')
        type_label.grid(row=index, column=1, sticky='nsew')
        date_label.grid(row=index, column=2, sticky='nsew')
        time_label.grid(row=index, column=3, sticky='nsew')

    # Create a pie chart for attendance types
    types = [row['Type'] for row in data]
    type_counts = {t: types.count(t) for t in set(types)}
    plt.figure(figsize=(5, 5))
    plt.pie(type_counts.values(), labels=type_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Attendance Types', fontsize=12, fontweight='bold')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()

    # Embed the Matplotlib plot in the GUI
    graph_canvas = FigureCanvasTkAgg(plt.gcf(), graph_frame)
    graph_canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    # Add labels for current date and time with designs
    date_label = tk.Label(date_time_frame, text=f'Current Date: {current_date}', font=('Arial', 14, 'bold'), bg='#EEEEEE', padx=20, pady=10)
    time_label = tk.Label(date_time_frame, text=f'Current Time: {current_time}', font=('Arial', 14, 'bold'), bg='#EEEEEE', padx=20, pady=10)
    date_label.pack(side='left')
    time_label.pack(side='right')

window = tk.Tk()
window.minsize(800, 600)
window.title(f'Attendance Logs for {current_date}')

# Create frames for attendance display, graph, and date/time
attendance_frame = tk.Frame(window, bg='#FFFFFF')
attendance_frame.pack(side='left', fill='both', expand=True)

graph_frame = tk.Frame(window, bg='#FFFFFF')
graph_frame.pack(side='right', fill='both', expand=True)

date_time_frame = tk.Frame(window, bg='#EEEEEE', pady=10)
date_time_frame.pack(side='bottom', fill='x')

attendance_data = read_attendance_data()
display_attendance(attendance_data)

window.mainloop()
