import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import tkinter.font as tkFont
import subprocess
import sys
from tkinter import messagebox

def get_image(url, width, height):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

myyellow = "#FFD500"
score = 0

root = tk.Tk()
root.title("Matching Game")
root.geometry("1920x1080") 
root.attributes("-fullscreen", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

row1_height = int(0.2 * screen_height)
row2_height = int(0.2 * screen_height)
row3_height = int(0.2 * screen_height)
row4_height = int(0.4 * screen_height)

allurabig = tkFont.Font(family="Allura", size=48, weight="bold")

image_urls = [
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/c20b38030c6e463438ec0d0cf2195a1a/IMG_7448.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcDM9glIFgB6UIAKkBUo76RO8gwb5mejaq5CN-x5_4kf7H_3GW4ZHcn9qukAmi0jfp4pDasj0x8SJRSNIdEeZc06PNph2EH6oylEb49dfdRHKPUAoP5-ZO1FGev8AIxaW0ZJX_AXprwb38pruS_Vcrw",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/ec50a3a52ee8fed72c86a3c16c2cee43/IMG_7434.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzd5ipp8wJ0jQxjmOFcT-PFj9I90Dx-GQukF_y0LIin4-9RlADHsQ2TLNeFGkWyOoFEr5rSMK5bQsKxXMVCV6vi-bxwst_LnoQtYlamp-B_vqxrK9ZdZOk3vNYU8esJtlYgOGzAJbTpLJFssNLrEQ510",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/7bb4bbba23dc80037c0e844c467dce59/IMG_7435.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzebLajaIv9b92DI7GQgO4Rrg8kf3hU_3usE_ViVzO3cqNuWoTbPPvYwTrFQpmA0sQkguJFd9JAO56RiMg9PezXW77hYBaObGRy15yAfF11DleDRkp3vjOSLs0XNfP3y9xd3HKkSF-LxAHfS77K7rqh1",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/e379e5d9c02591c8e942411437ec4a7c/IMG_7436.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzd5ipp8wJ0jQxjmOFcT-PFjd5nfZmqLN-evMPBpVkERWCCETCVazJhz1trF5-ILr6iLIL6MiFUL-oFbn6i29TIAiKjagi4Kqe7Qt5g-viIfcT8FUKtaaQ7VkxZlxJ8CXE6QJlhM2C3QH0ypI2tfIJvb",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/069cfc00b7ca28e5639a14278fe5f319/IMG_7437.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvApQfKhtEvQP0kSPASO0wodsbx-GkH5fO5o13HbMy48O6ZBGXIw3LDKr6xOObpOcCMmncMmNAg0SbMsOzCHAeJ10EK7Juz2rUfXrpXmEo1eePMkqHX1WxufXgdf1o_1TF",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/637317b53e744f397323bdb32c394f53/IMG_7438.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOze6pA6LabDCC03MP4Ernxo5EyMBni9TJIYOPQiSp-8BWU1VAz0DZKc2LCzZbqnwdXdCQA08eKOQyYKmVFdFBzqdv8v38CIPBZiM0xGl00i_ISqlkX68rgWklfOG3-EZq0qN1BenKzJN7eMRS-fBTQKB",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/dc942371fbd3a96cb1fbf55a4fc7a21e/IMG_7439.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdqOyto4Kc4wWO-KPNTRwzNjNDQrnm_Za77ITf0Eq5SUIwpTXa4VJGf2QsRw432syJceFtEoG2zz4u7zvsKRXtnUTtiQb8QWzhvNPEynY7MyRo11xkZvBbVCr6Wc_bctsLAIUEfb9E1_wuzLP86zUmu",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/87c115697f968c8556be062448edaa27/IMG_7440.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfuu-rUBucKMsyHdudQh4mOgf3f-2GhZMs6as-OI3eXtctzuvghp57zCg4A-jAmiVTjdYuT4RkpqRzgqyEdcWZfqxVFQ161zpQ1GwW0O1ZZSFmr4rzS3uKK0PQA3Thp1WwzqkrNt08-mBu8FvV3xRIB",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/0bcc713745ba890dcf6177bfff37519f/IMG_7446.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvDOQEe0JUCaOxxhstFLgmot-iglUFhpXzbBrtuuTKsKGXUxFURTzoZhr4nc461CGs4rx1965oy3-3HjqYL7aGyylw0oBh5AH2cJe_o62RKrm7RG63fN5enOQiZnb72ern",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/d6529afe554ae20a872f63ae519301a0/IMG_7447.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdqOyto4Kc4wWO-KPNTRwzNTLSIUcw6vX636aDIWq2eUU-4jHk2t6w9o7ay9RJc6Bx9g5U7Z7daQcqOLcHXcOBRvFOFNqnxfvFkPdk3AuCsvKzkcFA6ShWQVoX4QKou98vDUmFjSEa0d-mysopPhrmh",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/3e256b2f57b053b9851c6134f6a1505c/IMG_7014.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzeG68HmhjCTPeEAkFH88KonbS8lvuYIOELulpuTfqy4NBEB5lGv5Qf5cQQJDgawuo_hO_zsuKSImTaSH4I-3F02Ig15fp5Cx1gSJ14bfztHz9k52ZUzTzjW61YLN4_jBo5xQoqUXBBbQP8TReWwzjrs",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/3431bcaf175ddb51628a927f5ba970f1/IMG_7013.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzeG68HmhjCTPeEAkFH88KonJAvftsqNH27ibNkglESV8PKapFPC973975wL2rQYCyiQFiB-8T7HVXi0jWC2vyImc50KN0NKR87IJHMJ2xVHUypK0Pp-wwEh1v5Nruk8BjQAhyYm98XLUyUlD6OAg0qA",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/dc0b3ea1f3f38d05a870fc4f94ffb278/IMG_7012.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdqOyto4Kc4wWO-KPNTRwzNwR4LPG6FVPncTAQx8_lPX_J_Ia0sKshRKvnN0RHxUnccjUZ-l8lHPhBx4rA9YbizD-0q1CpdhyWzTqkmU7wXsKxYcKfGTE4TCQ-9Hk0ZT0wgdYzkECSucz9t-hjnjwyM",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/3fc9761ce087e752fe353aeac559d506/IMG_7011.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzeG68HmhjCTPeEAkFH88Kon8yCELZO7iex9GswXQS46VNJlanKEKI0ZL9qvP3Qi5c35_KHLUguuEAl-ISaYQJdz-v3PHVivwVSW2Z_798JyQ8ndIJFRY4K7aFzZSiRyGUriJFHy0KcLe8u7iQ51uMcd",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/12259b52dd0261221f20d26ae809486c/IMG_7010.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxvy3UQHPwxtzT0ukNhvQDKGbUD9SZuwW8tpdkk-QQ798lMbTBwnG6bsJV-MAX5xPwelsgE5wIiEKyh7btcgW-pfsa_b_RM80nosp3Mswx5GwqtY3I4e49tQzauIUlb0Q6ffCTfL_8i1wmoJd6xuSD",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/0972b289c46c8474033cd67625ae91ee/IMG_7009.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvVTrUSO4RZLgmINooqfVGzDZkd7DjtVEx-E0Fe5pBrjaJ1E0-l8EvIIybgKhh-scUlFkmrY2OMMGhm7p58rFC9fa2309ApwErCkEMoj2smSPfzWJMNKbReZIUYpRlx5Hx",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/f121376eff4a0de4d2e56bfce1d97117/IMG_7007.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdrfw102NKhCFdQ4eCHKtNvQ2q4X8RLN3RK3umJsgsuGdmu1pshvdSy-EYcajiM5tfh-Vwm054XHfvzZ2psOrSftUe7F6O_X1oq579Ki1MI4I3VAZZV5baKjP3TrxebPu1S5YruW_J6qaFl8-GF919M",
]

Matches = {
    "Robe": "Dress",
    "Pantalon": "Pants",
    "Chaussettes": "Socks",
    "Manteau": "Coat",
    "Chemise": "Shirt",
    "Chapeau": "Hat",
    "Jupe": "Skirt"
}
NEW_IMAGE_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/5997200ec1ddcc97dddcb08d00900bb8/IMG_7452.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfhUhZTA5OeWcEGM3iGX6ZoWO2aO1wwNoMPu33hCqE8ITrhAlRm3_7usO0A8Tu0a_5Zh3542SQwKghrFk2u5ffKOYwF4GWLk23LFWqb_3TxzdXCznNh9urrtlRqkv6gmP6XH19pakU8q8s8A0NRL4oo"
button_images = [None]
button_refs = [None]
buttons = [None]
Commands = ["Robe", "Manteau", "Chemise", "Chapeau", "Chaussettes", "Pantalon", "Jupe", "Dress", "Skirt", "Pants", "Socks", "Hat", "Shirt", "Coat"]
status = False
first = None
pair = None
finished = 0
firstheight = 0
firstwidth = 0

def goBack():
    messagebox.showinfo("Game Over", "Game Over: You have successfully completed this mission")
    try:
        subprocess.Popen([sys.executable, "NextGames.py", str(remaining)])
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.")

def open_fullscreen_window():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.mainloop()

def update_button_image(button_index, button_index2, width, height, width2, height2):
    new_img = get_image(NEW_IMAGE_URL, width2, height2)  
    btn = buttons[button_index-2]  
    btn.config(image=new_img) 
    btn.image = new_img  
    new_img = get_image(NEW_IMAGE_URL, width, height)  
    btn2 = buttons[button_index2] 
    btn2.config(image=new_img) 
    btn2.image = new_img 


def get_match(name, urlno, width, height):
    global status, first, pair, score, status_label, finished, firstheight, firstwidth
    if status == False:
        pair = find_pair(name)
        status = True
        print("First term received", name)
        first = urlno
        firstheight = height
        firstwidth = width
        #status_label.config(text=f"First term received: {name}")
    elif status == True and pair == name:
        status = False
        print("Correct match received", pair, first)
        score += 2
        finished += 1
        print("Score: ", score)
        status_label.config(text=f"Score: {score}")
        #image_urls[urlno - 1] = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/5997200ec1ddcc97dddcb08d00900bb8/IMG_7452.jpeg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ_YVCo7R8EhlM18GLZ0eMdtwPShJZEE6IHnkcfbTKc4ixaFILWKPKpJMKaCmtDUOcD0O1NC2jWx-NySksr-NpLKvvH0Qwozmo3x59d9mqZRgA-2ds9O4B5aNdhsjJcbNYw=="
        #update_image(image_widgets[urlno - 1], image_urls[urlno - 1], image_width, image_height)
        #update_image(image_widgets[first], image_urls[first], image_width, image_height)
        update_button_image(urlno, first, firstwidth, firstheight, width, height)
        print ("URLs at {} and {} changed".format(urlno, first))
        print (i)
        if finished == 7:
            print("Game Over")
            goBack()
        return True
    else:
        status = False
        print("Incorrect match received", name, first)
        score -= 1
        status_label.config(text=f"Score: {score}")
        return False
    

def find_pair(value):
    for key, val in Matches.items():
        if val == value:
            return key
        elif key == value:
            return val
    return None  

if len(sys.argv) > 1:
    time_left = sys.argv[1]
    print(f"Received variable: {time_left}")
else:
    print("No variable received.")
    time_left = 2700

def open_script():
    try:
        subprocess.Popen([sys.executable, "Break.py", str(remaining)])
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.") 

def countdown(time_left):
    global remaining
    time_left = int(time_left)
    minutes, seconds = divmod(time_left, 60)
    if time_left > 0:
        remaining = time_left
        root.after(1000, countdown, time_left - 1)
        print(f"Time Left: {minutes:02}:{seconds:02}")
        print(remaining)
    else:
        open_script()

parent_canvas = tk.Canvas(root, bg=myyellow, width=screen_width, height=row1_height, highlightthickness=0)
parent_canvas.pack(fill="x")
child_canvas1 = tk.Canvas(parent_canvas, bg=myyellow, width=screen_width // 3, height=row1_height, highlightthickness=0)
child_canvas1.place(x=0, y=0)
child_canvas1.pack(side="left", fill="both", expand=True)
status_label = tk.Label(child_canvas1, text="Score: 0", font=allurabig, bg=myyellow)
status_label.pack(expand=True)
child_canvas2 = tk.Canvas(parent_canvas, bg=myyellow, width=screen_width // 3, height=row1_height, highlightthickness=0)
child_canvas2.place(x=screen_width // 3, y=0)
child_canvas2.pack(side="left", fill="both", expand=True)
heading1 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/c20b38030c6e463438ec0d0cf2195a1a/IMG_7448.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcDM9glIFgB6UIAKkBUo76RO8gwb5mejaq5CN-x5_4kf7H_3GW4ZHcn9qukAmi0jfp4pDasj0x8SJRSNIdEeZc06PNph2EH6oylEb49dfdRHKPUAoP5-ZO1FGev8AIxaW0ZJX_AXprwb38pruS_Vcrw", screen_width // 3, row1_height//2)
child_canvas2.create_image(200, row1_height // 4, anchor="nw", image=heading1)
child_canvas3 = tk.Canvas(parent_canvas, bg=myyellow, width=screen_width // 3, height=row1_height, highlightthickness=0)
child_canvas3.place(x=(2 * screen_width) // 3, y=0)
child_canvas3.pack(side="left", fill="both", expand=True)
heading2 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/0867e5d40bb8de5cbd59f26bbd9ea7ff/IMG_7449.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvA7uB9PNdqlYNr_U6i2gvsJJNvMRAqkS0DHvejuzdSiMx3tPpy2s9fMDL9sFJ7INYkwJl6TeeVAZ6-WWeczAgYkN9ty4_I9XCSQhHM5EKwwmBPIwWL1xRekIiOfEQHmFC", screen_width // 4, row1_height//2)
child_canvas3.create_image(200, row1_height // 4, anchor="nw", image=heading2)

row2_frame = tk.Frame(root, height=row2_height)
row2_frame.pack(fill="x")
canvas2_width = screen_width // 4

for i in range(4):
    canvas = tk.Canvas(row2_frame, bg=myyellow, width=canvas2_width, height=row2_height, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    img = get_image(image_urls[i + 1], canvas2_width, row2_height)
    
    btn = tk.Button(canvas, image=img, command=lambda i=i: get_match(Commands[i], i + 1, canvas2_width, row2_height))
    btn.image = img  
    btn.note = i + 1
    btn.pack(fill="both", expand=True)
    
    buttons.append(btn)


# Row 3: Three canvases
row3_frame = tk.Frame(root, height=row3_height)
row3_frame.pack(fill="x")
canvas3_width = screen_width // 3

for i in range(3):
    canvas = tk.Canvas(row3_frame, bg=myyellow, width=canvas3_width, height=row3_height, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    img = get_image(image_urls[i + 5], canvas3_width, row3_height)
    btn = tk.Button(canvas, image=img, command=lambda i=i: get_match(Commands[i + 4], i+5, canvas3_width, row3_height))
    btn.image = img  
    btn.note = i + 5
    btn.pack(fill="both", expand=True)
    buttons.append(btn)

# Row 4: Three canvases with special dimensions
row4_frame = tk.Frame(root, height=row4_height)
row4_frame.pack(fill="x")

canvas4_1 = tk.Canvas(row4_frame, bg=myyellow, width=int(0.1 * screen_width), height=row4_height, highlightthickness=0)
canvas4_1.pack(side="left", fill="both", expand=True)
img4_1 = get_image(image_urls[8], int(0.2 * screen_width), row4_height)
canvas4_1.create_image(0, 0, anchor="nw", image=img4_1)

canvas4_x = tk.Canvas(row4_frame, bg=myyellow, width=int(0.6 * screen_width), height=row4_height, highlightthickness=0)
canvas4_x.pack(side="left", fill="both", expand=True)

canvas4_3 = tk.Canvas(row4_frame, bg=myyellow, width=int(0.1 * screen_width), height=row4_height, highlightthickness=0)
canvas4_3.pack(side="left", fill="both", expand=True)
img4_3 = get_image(image_urls[9], int(0.2 * screen_width), row4_height)
canvas4_3.create_image(0, 0, anchor="nw", image=img4_3)

# Inside Canvas X: Two canvases
canvas_y = tk.Canvas(canvas4_x, bg=myyellow, width=int(0.6 * screen_width), height=int(float(row4_height) // 2.5), highlightthickness=0)
canvas_y.pack(fill="x")
canvas_z = tk.Canvas(canvas4_x, bg=myyellow, width=int(0.6 * screen_width), height=row4_height // 2, highlightthickness=0)
canvas_z.pack(fill="x")

# Inside Canvas Y
for i in range(4):
    inner_canvas = tk.Canvas(canvas_y, bg=myyellow, width=int(0.15 * screen_width), height=row4_height // 2, highlightthickness=0)
    inner_canvas.pack(side="left", fill="both", expand=True)
    img = get_image(image_urls[i + 10], int(0.15 * screen_width), int(float(row4_height) // 2.5))
    btn = tk.Button(inner_canvas, image=img, width=int(float(row4_height) // 2.5), height = int(float(row4_height) // 2.5), command=lambda i=i: get_match(Commands[i + 7], i+10, int(0.15*screen_width), int(float(row4_height) // 2.5)))
    btn.image = img  
    btn.note = i + 10
    btn.pack(fill="both", expand=True)
    buttons.append(btn)

# Inside Canvas Z
for i in range(3):
    inner_canvas = tk.Canvas(canvas_z, bg=myyellow, width=screen_width // 3, height=row4_height // 2, highlightthickness=0)
    inner_canvas.pack(side="left", fill="both", expand=True)
    img = get_image(image_urls[i + 14], row4_height // 2, row4_height // 2)
    btn = tk.Button(inner_canvas, image=img, width=(row4_height // 2)-8, height=(row4_height // 2)-8, command=lambda i=i: get_match(Commands[i + 11], i+14, row4_height // 2, row4_height // 2))
    btn.image = img  
    btn.note = i + 14
    btn.pack()
    buttons.append(btn)

countdown(time_left)
root.mainloop()
