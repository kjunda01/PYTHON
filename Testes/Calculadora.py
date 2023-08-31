import customtkinter as ctk

########## OPÇOES DA JANELA ##########
window = ctk.CTk()
window.geometry("305x370")
window.title("Calculadora")
ctk.set_appearance_mode("System")

########## FUNÇÕES ##########




num = "0"


########## CRIAÇÃO DOS BOTÕES ##########
# Tela
font_resposta = ctk.CTkFont(family="Helvetica", size=40)
font_operations = ctk.CTkFont(family="Helvetica", size=30)
font_numbers = ctk.CTkFont(family="Helvetica", size=24)
screen = ctk.CTkLabel(window, width=295, height=60, text=num, font=font_resposta)

# primeira linha
btn_percent = ctk.CTkButton(window, width=70, height=40, text="%", font=font_operations)
btn_ce = ctk.CTkButton(window, width=70, height=40, text="CE", font=font_operations)
btn_c = ctk.CTkButton(window, width=70, height=40, text="C", font=font_operations)
btn_delete = ctk.CTkButton(window, width=70, height=40, text="Del", font=font_operations)

# Segunda linha
btn_num_divide = ctk.CTkButton(window, width=70, height=40, text="¹/x", font=font_operations)
btn_elevate = ctk.CTkButton(window, width=70, height=40, text="x²", font=font_operations)
btn_square = ctk.CTkButton(window, width=70, height=40, text="²√x", font=font_operations)
btn_divided = ctk.CTkButton(window, width=70, height=40, text="÷", font=font_operations)

# Terceira linha
btn_7 = ctk.CTkButton(window, width=70, height=40, text="7", font=font_numbers)
btn_8 = ctk.CTkButton(window, width=70, height=40, text="8", font=font_numbers)
btn_9 = ctk.CTkButton(window, width=70, height=40, text="9", font=font_numbers)
btn_times = ctk.CTkButton(window, width=70, height=40, text="*", font=font_operations)

# Quarta linha
btn_4 = ctk.CTkButton(window, width=70, height=40, text="4", font=font_numbers)
btn_5 = ctk.CTkButton(window, width=70, height=40, text="5", font=font_numbers)
btn_6 = ctk.CTkButton(window, width=70, height=40, text="6", font=font_numbers)
btn_minus = ctk.CTkButton(window, width=70, height=40, text="-", font=font_operations)

# Quinta linha
btn_1 = ctk.CTkButton(window, width=70, height=40, text="1", font=font_numbers)
btn_2 = ctk.CTkButton(window, width=70, height=40, text="2", font=font_numbers)
btn_3 = ctk.CTkButton(window, width=70, height=40, text="3", font=font_numbers)
btn_plus = ctk.CTkButton(window, width=70, height=40, text="+", font=font_operations)

# Sexta linha
btn_invert = ctk.CTkButton(window, width=70, height=40, text="+/-", font=font_operations)
btn_0 = ctk.CTkButton(window, width=70, height=40, text="0", font=font_numbers)
btn_virg = ctk.CTkButton(window, width=70, height=40, text=",", font=font_numbers)
btn_equal = ctk.CTkButton(window, width=70, height=40, text="=", font=font_operations)

########## COLOCANDO OS BOTÕES NA TELA ########## 
# Screen
r0 = 45
screen.place(x=120, y=15)

# Botões primeira linha
# btn_percent.grid(row=1, column=0, padx=2, pady=5, sticky="ew")
# btn_ce.grid(row=1, column=1, padx=2, pady=5, sticky="ew")
# btn_c.grid(row=1, column=2, padx=2, pady=5, sticky="ew")
# btn_delete.grid(row=1, column=3, padx=2, pady=5, sticky="ew")
btn_percent.place(x=5, y=2*r0)
btn_ce.place(x=80, y=2*r0)
btn_c.place(x=155, y=2*r0)
btn_delete.place(x=230, y=2*r0)

# Botões segunda linha
# btn_num_divide.grid(row=2, column=0, padx=2, pady=5, sticky="ew")
# btn_elevate.grid(row=2, column=1, padx=2, pady=5, sticky="ew")
# btn_square.grid(row=2, column=2, padx=2, pady=5, sticky="ew")
# btn_divided.grid(row=2, column=3, padx=2, pady=5, sticky="ew")
btn_num_divide.place(x=5, y=3*r0)
btn_elevate.place(x=80, y=3*r0)
btn_square.place(x=155, y=3*r0)
btn_divided.place(x=230, y=3*r0)

# Botões tereceira linha
# btn_7.grid(row=3, column=0, padx=2, pady=5, sticky="ew")
# btn_8.grid(row=3, column=1, padx=2, pady=5, sticky="ew")
# btn_9.grid(row=3, column=2, padx=2, pady=5, sticky="ew")
# btn_times.grid(row=3, column=3, padx=2, pady=5, sticky="ew")
btn_7.place(x=5, y=4*r0)
btn_8.place(x=80, y=4*r0)
btn_9.place(x=155, y=4*r0)
btn_times.place(x=230, y=4*r0)

# Botões quarta linha
# btn_4.grid(row=4, column=0, padx=2, pady=5, sticky="ew")
# btn_5.grid(row=4, column=1, padx=2, pady=5, sticky="ew")
# btn_6.grid(row=4, column=2, padx=2, pady=5, sticky="ew")
# btn_minus.grid(row=4, column=3, padx=2, pady=5, sticky="ew")
btn_4.place(x=5, y=5*r0)
btn_5.place(x=80, y=5*r0)
btn_6.place(x=155, y=5*r0)
btn_minus.place(x=230, y=5*r0)


# Botões quinta linha
# btn_1.grid(row=5, column=0, padx=2, pady=5, sticky="ew")
# btn_2.grid(row=5, column=1, padx=2, pady=5, sticky="ew")
# btn_3.grid(row=5, column=2, padx=2, pady=5, sticky="ew")
# btn_plus.grid(row=5, column=3, padx=2, pady=5, sticky="ew")
btn_1.place(x=5, y=6*r0)
btn_2.place(x=80, y=6*r0)
btn_3.place(x=155, y=6*r0)
btn_plus.place(x=230, y=6*r0)


# Botões sexta linha
# btn_invert.grid(row=6, column=0, padx=2, pady=5, sticky="ew")
# btn_0.grid(row=6, column=1, padx=2, pady=5, sticky="ew")
# btn_virg.grid(row=6, column=2, padx=2, pady=5, sticky="ew")
# btn_equal.grid(row=6, column=3, padx=2, pady=5, sticky="ew",)
btn_invert.place(x=5, y=7*r0)
btn_0.place(x=80, y=7*r0)
btn_virg.place(x=155, y=7*r0)
btn_equal.place(x=230, y=7*r0)

window.mainloop()
