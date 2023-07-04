import tkinter as tk
from tkinter import messagebox
from plyer import notification

def show_notification():
    notification_title = "Hora de beber água!"
    notification_message = "Lembre-se de se hidratar."
    notification_icon = 'water.ico'
    notification.notify(title=notification_title, message=notification_message, app_icon=notification_icon)

def set_reminder():
    interval = int(interval_entry.get())  # Obter o intervalo do campo de entrada
    interval_in_minutes = interval * 60  # Converter o intervalo para minutos
    show_notification()  # Exibir uma notificação imediatamente

    # Configurar um lembrete periódico
    window.after(interval_in_minutes * 1000, set_reminder)

# Configuração da janela principal
window = tk.Tk()
window.title("Lembrete de Água")
window.geometry("300x150")

# Rótulo e campo de entrada para o intervalo
interval_label = tk.Label(window, text="Intervalo (minutos):")
interval_label.pack()
interval_entry = tk.Entry(window)
interval_entry.pack()

# Botão para iniciar o lembrete
start_button = tk.Button(window, text="Iniciar", command=set_reminder)
start_button.pack()

# Executar a janela principal
window.mainloop()
