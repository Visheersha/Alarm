import tkinter as tk
from tkinter import messagebox
import winsound
from datetime import datetime, timedelta
import threading
import time

# Function to add alarms from entry box

def add_alarm():
    times = alarm_entry.get().split(",")
    for t in times:
        try:
            # Normalize input to HH:MM format
            time_obj = datetime.strptime(t.strip(), "%H:%M")
            formatted_time = time_obj.strftime("%H:%M")
            if formatted_time not in alarm_list:
                alarm_list.append(formatted_time)
                alarm_listbox.insert(tk.END, formatted_time)
        except ValueError:
            messagebox.showerror("Invalid Time", f"'{t.strip()}' is not a valid time")
    alarm_entry.delete(0, tk.END)

# Function to check alarms in background

def check_alarms():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        for alarm_time in alarm_list.copy():  # copy to avoid modifying list while looping
            if current_time == alarm_time:
                # Play alarm sound
                winsound.PlaySound("alarm.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
                
                # Popup message for the alarm
                response = messagebox.askyesno("Alarm", f"Alarm ringing at {current_time}\nSnooze for 5 minutes?")
                
                # If snooze pressed
                if response:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    snooze_time = (datetime.strptime(current_time, "%H:%M") + timedelta(minutes=5)).strftime("%H:%M")
                    alarm_list.append(snooze_time)
                    alarm_listbox.insert(tk.END, snooze_time)
                    messagebox.showinfo("Snoozed", f"Alarm snoozed to {snooze_time}")
                
                # Stop current alarm
                winsound.PlaySound(None, winsound.SND_PURGE)
                
                # Remove triggered alarm
                alarm_list.remove(alarm_time)
                alarm_listbox.delete(0, tk.END)
                for a in alarm_list:
                    alarm_listbox.insert(tk.END, a)
                
        time.sleep(5)  # Check every 5 seconds


# Tkinter GUI 

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x300")

tk.Label(root, text="Enter alarm times (HH:MM, comma separated):").pack(pady=10)

alarm_entry = tk.Entry(root, width=30)
alarm_entry.pack(pady=5)

tk.Button(root, text="Add Alarm", command=add_alarm).pack(pady=5)

alarm_listbox = tk.Listbox(root)
alarm_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Initialize alarm list
alarm_list = []

# Start the background thread
thread = threading.Thread(target=check_alarms, daemon=True)
thread.start()

root.mainloop()
