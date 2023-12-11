import tkinter as tk
from tkinter import ttk  # ttk is tkinter's themed widget library
import os
import random
import pygame
from helper import GetTitlesAndAuthors, GetMusicByIdPath
from tkinter.font import Font


# Function to play music
def play_music():
    global upper_limit, lower_limit, file_index, current_track_pos

    current_track_pos = 0
    randId = -1
    if upper_limit-lower_limit==0:
        randId = lower_limit
    else:
        while (True):
            randId = lower_limit+random.choice(range(upper_limit-lower_limit))
            if(randId !=file_index):
                break
    file_index = randId
    file_path = GetMusicByIdPath(file_index)
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    title_label.config(text="")
    composer_label.config(text="")
    

# Function to stop music and display title and composer
def stop_music():
    global file_index, titles, composers

    title = titles[file_index]
    composer = composers[file_index]
    title_label.config(text=f"{title}", font=bold_font)
    composer_label.config(text=f"{composer}", font=bold_font)

# Function to update file index and slider value labels
def update_file_index_lower(value):
    global lower_limit, upper_limit, slider_label_lower
    lower_limit = int(float(value))
    
    if(upper_limit<lower_limit):
        upper_limit=lower_limit
        slider_label_upper.config(text=f"Do utworu: {upper_limit}") 
        limitId_slider_upper.set(upper_limit)
        
    
    slider_label_lower.config(text=f"Od utworu: {lower_limit}")

def update_file_index_upper(value):
    global lower_limit, upper_limit, slider_label_upper
    upper_limit = int(float(value))
    
    if(upper_limit<lower_limit):
        lower_limit=upper_limit
        slider_label_lower.config(text=f"Od utworu: {lower_limit}")
        limitId_slider_lower.set(lower_limit)
    
    slider_label_upper.config(text=f"Do utworu: {upper_limit}")

# Function to skip ahead 30 seconds in the music
def skip_ahead():
    global current_track_pos  # Use the global variable to keep track of position

    if pygame.mixer.music.get_busy():  # Check if music is playing
        elapsed_time = pygame.mixer.music.get_pos() / 1000  # Time elapsed since last play in seconds
        current_track_pos += elapsed_time  # Update the absolute position
        new_pos = current_track_pos + 30  # Calculate new position
        pygame.mixer.music.play(0, new_pos)  # Start playing at the new position

        current_track_pos = new_pos  # Update current position for next skip
        
# Function to go back 30 seconds in the music
def go_back():
    global current_track_pos  # Use the global variable to keep track of position

    if pygame.mixer.music.get_busy():  # Check if music is playing
        elapsed_time = pygame.mixer.music.get_pos() / 1000  # Time elapsed since last play in seconds
        current_track_pos += elapsed_time  # Update the absolute position
        new_pos = current_track_pos - 30  # Calculate new position
        pygame.mixer.music.play(0, new_pos)  # Start playing at the new position

        current_track_pos = new_pos  # Update current position for next skip
        

# Initialize data
titles, composers = GetTitlesAndAuthors()
lower_limit = 0
upper_limit = 10
file_index = lower_limit+random.choice(range(upper_limit-lower_limit))

# Initialize a variable to keep track of the absolute position
current_track_pos = 0

# Creating main window
root = tk.Tk()
root.title("Jaka to Melodia")
root.geometry("500x250")  # Width: 500px, Height: 300px
root.resizable(False, False)  # Disable resizing of the window

# Styling
style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme for a modern look

# Frame for the controls
control_frame = ttk.Frame(root, padding="10 10 10 10")
control_frame.pack(pady=10, fill='x', expand=True)

# Lower limit slider
slider_label_lower = ttk.Label(control_frame, text="Od utworu: ", font=("Helvetica", 10))
slider_label_lower.grid(row=0, column=0, padx=10, sticky="W")
limitId_slider_lower = ttk.Scale(control_frame, from_=0, to=42, orient='horizontal', command=update_file_index_lower, length=200)
limitId_slider_lower.set(lower_limit)
limitId_slider_lower.grid(row=1, column=0, padx=10, sticky="EW")

# Upper limit slider
slider_label_upper = ttk.Label(control_frame, text="Do utworu: ", font=("Helvetica", 10))
slider_label_upper.grid(row=2, column=0, padx=10, sticky="W")
limitId_slider_upper = ttk.Scale(control_frame, from_=0, to=42, orient='horizontal', command=update_file_index_upper, length=200)
limitId_slider_upper.set(upper_limit)
limitId_slider_upper.grid(row=3, column=0, padx=10, sticky="EW")

# Play and Stop buttons
play_button = ttk.Button(control_frame, text="Następny", command=play_music)
play_button.grid(row=1, column=1, padx=10)
stop_button = ttk.Button(control_frame, text="Sprawdź", command=stop_music)
stop_button.grid(row=1, column=2, padx=10)

# Add the skip button to your interface
skip_button = ttk.Button(control_frame, text="<< 30s", command=go_back)
skip_button.grid(row=3, column=1, padx=10)

# Add the skip button to your interface
skip_button = ttk.Button(control_frame, text=">> 30s", command=skip_ahead)
skip_button.grid(row=3, column=2, padx=10)

# Frame for the music information
info_frame = ttk.Frame(root, padding="10 10 10 10")
info_frame.pack(pady=10, fill='x', expand=True)

# Inside your main GUI setup code, define the fonts
bold_font = Font(family="Helvetica", size=10, weight="bold")

# The static part of the labels remain unchanged and with the default font
title_prefix_label = ttk.Label(info_frame, text="Tytuł: ")
title_prefix_label.grid(row=0, column=0, sticky="W")
composer_prefix_label = ttk.Label(info_frame, text="Kompozytor: ")
composer_prefix_label.grid(row=1, column=0, sticky="W")

# The dynamic part of the labels where you'll set the bold font
title_label = ttk.Label(info_frame, font=bold_font)
title_label.grid(row=0, column=1, sticky="W")
composer_label = ttk.Label(info_frame, font=bold_font)
composer_label.grid(row=1, column=1, sticky="W")

# Start the GUI loop
root.mainloop()
