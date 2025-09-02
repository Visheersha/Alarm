# Alarm
A Python Tkinter Alarm Clock with multiple alarm, sound alert, snooze.
This is a Python-based Alarm Clock application built with Tkinter (GUI).
It allows users to set one or multiple alarms, handles invalid time inputs, and provides a snooze feature. When an alarm rings, the user can choose to stop it or snooze it for 5 minutes.
The app runs in the background, continuously checking for alarm times, and plays a looping sound when an alarm is triggered.

# Features
- Multiple Alarms: Add more than one alarm at a time
- Error Handling: Invalid inputs are skipped 
- Snooze Option: Snooze alarm for 5 minutes
- Sound Alert: Play a sound (audio.wav) when the alarm rings
- GUI TKinter: Provide  interface with input box and alarm list
- Background Threading: Keeps checking the alarms without freezing the GUI

# Technologies Used
- Python 3
- Tkinter (GUI framework)
- winsound (for sound playback on Windows)
- datetime and timedelta (for time handling)
- threading (for background alarm checking)
