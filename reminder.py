import tkinter as tk # módulo tkinter para exibir janelas
from tkinter import messagebox # exibir caixa de diálogo

# Largura da janela
window_width = 400
# Altura da janela
window_height = 300

# Criar nova janela principal
root = tk.Tk()
# Definir título da janela
root.title("Reminder")
# Pontos do centro da tela
centerX = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
centerY = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
# Definir tamanho da janela
root.geometry("%dx%d" % (window_width, window_height))
# Centralizar janela
root.geometry("+%d+%d" % (
    centerX - (window_width/2), 
    centerY - (window_height/2)))
# Não permitir redimensionamento
root.resizable(False, False)


#Classe principal do programa
class Application(tk.Frame):
    # Iniciar a janela
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()


#Protocolo de saída
# Quando for fechar o programa executar essa função
# Essa função exibe uma caixa de diálogo
def on_closing():
        d = messagebox.askokcancel("Question","Do you want to quit?")
        if d == True:
            ## Destrói a janela
            ## Fecha o programa
            root.destroy()
        #else:
            #pass


# Definir o protoclo de saída
root.protocol("WM_DELETE_WINDOW", on_closing)


if __name__ == '__main__':
    # Definir classe que vai ser o programa
    # como parâmetro a janela principal
    app = Application(master=root)
    # Iniciar o programa
    app.mainloop()