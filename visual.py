# Author: Raphael Campos Squilaro
# Project Name: FP - Visual Interface Example

# instalar o pacote do customtkinter
# pip install customtkinter

# importação da biblioteca
import customtkinter as ctk

# Configurações Visuais
# Modos : "dark", "light" ou "system" (padrão do sistema)
ctk.set_appearance_mode('dark')
# Temas : "blue" (padrão), "dark-blue", "green"
ctk.set_default_color_theme('blue')


janela = ctk.CTk()
janela.geometry('800x600')
janela.title('Conversor de Temperatura')

# Criação de elementos da tela
entrada = ctk.CTKEntry(janela, placeholder_text='Digite a temperatura em Celsius')
entrada.pack(pady=20)

janela.mainloop()
