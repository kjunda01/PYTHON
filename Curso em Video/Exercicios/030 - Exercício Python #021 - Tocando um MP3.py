from tkinter import PhotoImage, filedialog
import pygame
from pygame import *
import customtkinter as ctk
from time import sleep



pygame.mixer.init()
pygame.mixer.music.rewind()

def iniciar_musica():
    escolher_musica = filedialog.askopenfilename(
        title = "Escolha um arquivo",
        filetypes = (("Music Files","*.mp3"),))
    
    pygame.mixer.music.load(escolher_musica)
    pygame.mixer.music.play()

condition = True
def duracao():
   while condition:
        pygame.mixer.music.get_pos() / 1000

def pausar_musica():
    pygame.mixer.music.pause()

def resumir_musica():
    pygame.mixer.music.unpause()

def parar_musica():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

def volume_geral(value):
    pygame.mixer.music.set_volume(value)


# Propriedades da janela principal
window = ctk.CTk()
window.title("MP3 Player")
window.geometry("230x200")


# criação dos botoes
botao_pausa = ctk.CTkButton(window,
                            text="Pausar",
                            command=pausar_musica,
                            corner_radius=45,
                            border_width=1,
                            )

botao_selecionar = ctk.CTkButton(window,
                              text="Selecionar\nMP3",
                              command=iniciar_musica,
                              corner_radius=45,
                              border_width=1,
                              )

botao_parar = ctk.CTkButton(window,
                            text="Parar",
                            command=parar_musica,
                            corner_radius=45,
                            border_width=1,
                            )

botao_resumir = ctk.CTkButton(window,
                              text="Resumir",
                              command=resumir_musica,
                              corner_radius=45,
                              border_width=1,
                              )

volume_bar = ctk.CTkSlider(master=window,
                           command=volume_geral,
                           orientation='vertical',
                           height=140,
                           )

volume = ctk.CTkLabel(window,
                     text="Volume",
                     width=1,
                     height=1,)


#botoes na tela - grid
botao_selecionar.place(x=15, y=10)
botao_pausa.place(x=15, y=60)
botao_resumir.place(x=15, y=110)
botao_parar.place(x=15, y=160)
volume_bar.place(x=175, y=15)
volume.place(x=160, y=155)


window.mainloop()
