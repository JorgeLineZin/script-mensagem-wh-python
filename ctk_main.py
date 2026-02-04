import customtkinter as ctk
import pywhatkit as kit


# Criação da Classe da Aplicação(CTK)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("WhatsApp Message Sender")
        self.geometry("400x300")
        self.resizable(False, False)

        # Widgets
        self.label_title = ctk.CTkLabel(
            self,
            text="Envio de Mensagem pelo WhatsApp",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.label_title.pack(pady=10)

        self.label_num = ctk.CTkLabel(
            self, text="Número de telefone (Ex: +5511999999999):"
        )
        self.label_num.pack(pady=5)

        self.entry_num = ctk.CTkEntry(
            self, placeholder_text="Digite o número aqui...", width=200, height=30
        )
        self.entry_num.pack(pady=5)

        self.label_text = ctk.CTkLabel(self, text="Mensagem:")
        self.label_text.pack(pady=5)

        self.entry_text = ctk.CTkEntry(
            self, placeholder_text="Digite a mensagem aqui...", width=200, height=30
        )
        self.entry_text.pack(pady=5)

        self.send_button = ctk.CTkButton(
            self, text="Enviar Mensagem", command=self.send_message
        )
        self.send_button.pack(pady=10)

    # Funções
    def send_message(self):
        msg_num = self.entry_num.get()
        msg_text = self.entry_text.get()
        kit.sendwhatmsg_instantly(
            f"{msg_num}", f"{msg_text}", tab_close=True, close_time=4
        )
        print("Mensagem enviada!")


app = App()
app.mainloop()
