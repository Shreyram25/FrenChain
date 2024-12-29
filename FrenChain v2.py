import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO

# Define the color variables
myyellow = "#FFD500"
mybrown = "#B27530"

# Initialize the root window
parent = tk.Tk()
parent.title("Login Form")

# Set screen size to 1920x1080
parent.geometry("1920x1080")

# Set background color
parent.configure(bg=myyellow)

# Create font styles
allurabig = tkFont.Font(family="Allura", size=48, weight="bold")
large_font = tkFont.Font(family="Helvetica", size=18)
button_font = tkFont.Font(family="Helvetica", size=32, weight="bold")

# Load the main image
main_url = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/acf1cf423d2f579d1bf2a52fa90aad5a/IMG_6999.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcttbWblVBcrtjzlrLfyvWfASmvLY8uiiXnM-TM_QHw4C26QJbqF1fpPy2OetH4EEGSv76uFczN2rWs1FjiRuKCSSBgnrQ58QITkb7yRB8mH2dKPpTdySMJJQD01USZLwIXElRoylnQcV-jTCZ0cKU3"
overlay_url = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/633e668c64f6bf13757f0e291c7f01f2/image.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOze6pA6LabDCC03MP4Ernxo5anUIQQrGYJUXVE27ttqtdnjyw1b9M9SXjEJyjxgsJMl7yTKeC97neUDH34KPl-02Vqrs3KB3aevxA0VBDCHINZZu2tnV6mBi11xe0uLxZDI="

try:
    main_response = requests.get(main_url)
    main_response.raise_for_status()
    main_image_data = main_response.content
    main_image = Image.open(BytesIO(main_image_data))

    # Resize the main image
    window_width = 1920
    window_height = 1080
    max_width = window_width // 1.5
    max_height = window_height // 1.5
    main_image.thumbnail((max_width, max_height), Image.LANCZOS)
    main_photo = ImageTk.PhotoImage(main_image)

    overlay_response = requests.get(overlay_url)
    overlay_response.raise_for_status()
    overlay_image_data = overlay_response.content
    overlay_image = Image.open(BytesIO(overlay_image_data))
    overlay_image.thumbnail((max_width // 2.5, max_height // 1.25), Image.LANCZOS)
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    # Create a canvas to hold the images
    canvas = tk.Canvas(parent, width=main_photo.width() + overlay_photo.width() + 200, height=main_photo.height(), bg=myyellow, highlightthickness=0)
    canvas.pack(side="left", padx=50, pady=10)

    # Add the overlay and main images to the canvas
    canvas.create_image(0, 150, anchor="nw", image=overlay_photo)
    canvas.create_image(overlay_photo.width() + 200, 0, anchor="nw", image=main_photo)

except (requests.RequestException, UnidentifiedImageError) as e:
    print(f"Error loading image: {e}")
    image_label = tk.Label(parent, text="Image not available", bg=myyellow)
    image_label.pack(side="left", padx=50, pady=10)

# Create a frame for the form elements
form_frame = tk.Frame(parent, bg=myyellow)
form_frame.pack(side="right", expand=True, fill="both", padx=(0, 50))

# Add a centered inner frame
inner_frame = tk.Frame(form_frame, bg=myyellow)
inner_frame.pack(expand=True)

# Add title label
title_label = tk.Label(inner_frame, text="FrenChain", font=allurabig, bg=myyellow)
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 50), padx=(0, 80))

# Custom buttons
start_button = tk.Button(inner_frame, text="Start! / Commencez!", font=button_font, fg="white", bg=mybrown, borderwidth=0, activebackground=mybrown)
start_button.grid(row=5, column=0, pady=(50, 25), padx=(0, 80), columnspan=2, sticky="")

achievements_button = tk.Button(inner_frame, text="Achievements / Realisations", font=button_font, fg=mybrown, bg="white", borderwidth=0, activebackground="white")
achievements_button.grid(row=6, column=0, pady=(25, 25), padx=(0, 80), columnspan=2, sticky="")

games_button = tk.Button(inner_frame, text="Games / Jeux", font=button_font, fg="yellow", bg="black", borderwidth=0, activebackground="black")
games_button.grid(row=7, column=0, pady=(25, 25), padx=(0, 80), columnspan=2, sticky="")

parent.mainloop()