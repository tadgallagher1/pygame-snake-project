#imports
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#start 
music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("1000x500")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

#play_list
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def volume_set():
    pygame.mixer.music.set_volume(0.05)
def volume_yummy():
    pygame.mixer.music.set_volume(1.0)


Button1 = tkr.Button(music_player, width=5, height=3, font = "Helvetica 12 bold", text="PLAY", command=play, bg="DodgerBlue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font = "Helvetica 12 bold", text="STOP", command=stop, bg="LightGray", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font = "Helvetica 12 bold", text="PAUSE", command=pause, bg="Tomato", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font = "Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="ForestGreen", fg="white")
Button5 = tkr.Button(music_player, width=5, height=3, font = "Helvetica 12 bold", text="Volume Small", command=volume_set, bg="Cyan", fg="white")
Button6 = tkr.Button(music_player, width=5, height=3, font = "Helvetica 12 bold", text="Volume Big", command=volume_yummy, bg="Brown", fg="white")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
Button6.pack(fill="x")

play_list.pack(fill="both", expand="yes")

music_player.mainloop()
