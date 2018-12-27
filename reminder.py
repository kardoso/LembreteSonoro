import tkinter as tk # módulo tkinter para exibir janelas
from tkinter import messagebox # exibir caixa de diálogo

# Largura da janela
window_width = 400
# Altura da janela
window_height = 200

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
    centerX - (window_width/4), 
    centerY - (window_height/4)))
# Não permitir redimensionamento
root.resizable(False, False)


#Classe principal do programa
class Application(tk.Frame):
    # Iniciar a janela
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #Criar o botão para importar arquivos
        importButton = tk.Button(
            self,
            text = "Importar arquivo de áudio",
            #command = setsound,
            anchor = tk.CENTER,
            font = "Times 12 bold",
            #width = 100,
            height = 1,
            #background = "#33B5E5",
            #activebackground = "#33B5E5",
            relief = tk.GROOVE,
            justify="center")
        #Inserir botão na janela
        importButton.grid(row=1, column=1, columnspan=2, sticky=tk.E+tk.W)
        
        #Variável de texto informando a situação do arquivo
        #Se foi importado ou não, ou se o arquivo é válido
        fileResponse = tk.StringVar(value = "Nenhum arquivo selecionado")
        #Criar label para mostrar a situação do arquivo
        fResponse = tk.Label(
            self,
            text= "Nenhum arquivo selecionado",
            textvariable = fileResponse,
            font=("Helvetica",9),
            foreground = "red")
        #Inserir label na janela
        fResponse.grid(row=2, column=1, columnspan=2)

        #Label para informar ao usuário o que fazer
        periodLabel = tk.Label(
            self,
            text = "Informe a periodicidade:",
            font=("Helvetica 10 bold"),
            justify="center")
        #Inserir label na janela
        periodLabel.grid(row=4, column=1)

        #Variável com o período(tempo do ciclo do programa)
        period = tk.IntVar(self, value=30)
        #Input para entrada do dado period
        enterperiod = tk.Entry(self, textvariable=period, font=("Helvetica 10"), justify='center')
        #Inserir entry na janela
        enterperiod.grid(row=4, column=2)

        #Opções de tempo
        OPTIONS = ["Horas", "Minutos", "Segundos"]
        #Varíavel com o tipo de tempo, padrão "Minutos"
        timeType = tk.StringVar(self, value=OPTIONS[1])
        #Menu dropdown com as opções de tempo
        timeChooser = tk.OptionMenu(self, timeType, *OPTIONS)
        #Inserir dropdown na janela
        timeChooser.grid(row=5, column=2)

        #Botão para iniciar o programa
        startButton = tk.Button(
            self,
            text = "Rodar o programa",
            #command = run,
            anchor = tk.CENTER,
            font = "Times 12 bold",
            width = 20,
            height = 1,
            background = "blue",
            foreground = "white",
            activebackground = "white",
            activeforeground = "blue",
            relief = tk.GROOVE,
            justify="center")
        #Inserir o botão na janela
        startButton.grid(row=7, column=1, columnspan=2, sticky=tk.E+tk.W)
        
        #Configurar as linhas vazias do programa para terem tamanho 30
        self.grid_rowconfigure([3, 6], minsize=30)

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