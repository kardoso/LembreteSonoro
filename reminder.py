import os # usado para pegar diretório em que o programa está
import tkinter as tk # módulo tkinter para exibir janelas
from tkinter import messagebox # para exibir caixa de diálogo
from tkinter import filedialog # para procurar/selecionar arquivo
import winsound # para reproduzir o som (no windows)
from datetime import timedelta # para converter segundos para o formato HH:MM:SS

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

    # Adicionar campos ao programa
    def create_widgets(self):
        #Remover todos os campos presentes no programa
        for slave in self.grid_slaves():
            slave.grid_remove()
            slave.grid_forget()
            slave.destroy()
        #Criar o botão para importar arquivos
        self.importButton = tk.Button(
            self,
            text = "Importar arquivo de áudio",
            command = self.setsound,
            anchor = tk.CENTER,
            font = "Times 12 bold",
            #width = 100,
            height = 1,
            #background = "#33B5E5",
            #activebackground = "#33B5E5",
            relief = tk.GROOVE,
            justify="center")
        #Inserir botão na janela
        self.importButton.grid(row=1, column=1, columnspan=2, sticky=tk.E+tk.W)
        
        #O path do arquivo a ser carregador
        self.soundpath = ""
        #Variável de texto informando a situação do arquivo
        #Se foi importado ou não, ou se o arquivo é válido
        self.fileResponse = tk.StringVar(value = "Nenhum arquivo selecionado")
        #Criar label para mostrar a situação do arquivo
        self.fResponse = tk.Label(
            self,
            text= "Nenhum arquivo selecionado",
            textvariable = self.fileResponse,
            font=("Helvetica",9),
            foreground = "red")
        #Inserir label na janela
        self.fResponse.grid(row=2, column=1, columnspan=2)

        #Label para informar ao usuário o que fazer
        self.periodLabel = tk.Label(
            self,
            text = "Informe a periodicidade:",
            font=("Helvetica 10 bold"),
            justify="center")
        #Inserir label na janela
        self.periodLabel.grid(row=4, column=1)

        #Variável com o período(tempo do ciclo do programa)
        self.period = tk.IntVar(self, value=30)
        #Input para entrada do dado period
        self.enterperiod = tk.Entry(self, textvariable=self.period, font=("Helvetica 10"), justify='center')
        #Inserir entry na janela
        self.enterperiod.grid(row=4, column=2)

        #Opções de tempo
        self.OPTIONS = ["Horas", "Minutos", "Segundos"]
        #Varíavel com o tipo de tempo, padrão "Minutos"
        self.timeType = tk.StringVar(self, self.OPTIONS[1])
        #Menu dropdown com as opções de tempo
        self.timeChooser = tk.OptionMenu(self,self.timeType, *self.OPTIONS)
        #Inserir dropdown na janela
        self.timeChooser.grid(row=5, column=2, sticky="ew")

        #Botão para iniciar o programa
        self.startButton = tk.Button(
            self,
            text = "Iniciar",
            state = tk.DISABLED,
            command = self.run,
            anchor = tk.CENTER,
            font = "Times 12 bold",
            background = "blue",
            foreground = "white",
            activebackground = "white",
            activeforeground = "blue",
            relief = tk.GROOVE,
            justify="center")
        #Inserir o botão na janela
        self.startButton.grid(row=7, column=1, columnspan=2, sticky=tk.E+tk.W)
        
        #Configurar altura das linhas do programa
        self.grid_rowconfigure([1,2,3,4,5,6,7], minsize=26)

    # Definir o som que será reproduzido
    def setsound(self):
        #Pedir para o usuário selecionar o arquivo WAV
        fpath = filedialog.askopenfile(
            #Iniciar o diretório em que o programa está
            initialdir = os.path.dirname(os.path.abspath(__file__)),
            title="Selecione o áudio",
            filetypes=(("Arquivos .wav","*.wav"),
                ("all files","*.*"))
            )
        #Se o arquivo de áudio foi selecionado
        if fpath is not None:
            #Se o nome terminar com '.wav'
            #winsound reproduz apenas arquivos .wav
            if fpath.name.endswith('.wav'):
                self.soundpath = fpath.name
                self.fileResponse.set("Aquivo selecionado: "+str(fpath.name))
                self.fResponse.config(fg="green")
                self.startButton.config(state=tk.ACTIVE)
            else:
                self.fileResponse.set("Selecione um arquivo válido")
                self.fResponse.config(fg="orange")
                self.startButton.config(state=tk.DISABLED)
        #Se não foi selecionado nenhum arquivo
        else:
            self.fileResponse.set("Nenhum arquivo selecionado")
            self.fResponse.config(fg="red")
            self.startButton.config(state=tk.DISABLED)

    # Reproduzir som
    def playsound(self):
        #SND_LOOP - Reproduz com loop o usuário tomar alguma ação que pare o loop
        #SND_ASYNC - Reproduz de forma assíncrona, sem travar o programa
        winsound.PlaySound(self.soundpath, winsound.SND_LOOP | winsound.SND_ASYNC)
    
    # Parar de reproduzir som
    def stopsound(self):
        winsound.PlaySound(None, winsound.SND_ALIAS)

    # Iniciar ciclo do programa
    def run(self):
        #Parar de raproduzir som se estiver reproduzindo
        self.stopsound()
        #Remover todos os campos presentes programa
        for slave in self.grid_slaves():
            slave.grid_remove()
            slave.grid_forget()
            slave.destroy()

        #Label com a mensagem ao concluir a contagem
        messageLabel = tk.Label(
            self,
            text="Se lembre de ...",
            font=("Helvetica 12 bold"),
            fg="red")
        
        #Criar uma label apenas para mostrar o texto
        visualTimer = tk.Label(
            self,
            text="00:00:00",
            font=("Helvetica 24 bold"),
            fg="black")
        #Incluir label no grid
        visualTimer.grid(row=3, column=1, columnspan=2, sticky=tk.E+tk.W)
        
        #Recebe a variável que o usuário digitou convertida em segundos
        timeinseconds = 0
        if(self.timeType.get() == self.OPTIONS[0]):
            #Horas
            timeinseconds = (self.period.get() * 60) * 60
        elif(self.timeType.get() == self.OPTIONS[1]):
            #Minutos
            timeinseconds = self.period.get() * 60
        elif(self.timeType.get() == self.OPTIONS[2]):
            #Segundos
            timeinseconds = self.period.get()
        
        #Atualizar a label 'visualTimer'
        #e quando o tempo chegar a zero reproduz o som
        #mostra opções e mensagem de lembrete
        def update_timer(t):
            if(t >= 0):
                #Atualizar o texto da label visualTimer no formato de horas
                visualTimer.configure(text=str(timedelta(seconds=t)))
                #Decrementar dos segundos
                t -= 1
                #Esperar 1 segundo e fazer a recursão
                self.master.after(1000, update_timer, t)
            else:
                #Fazer a janela ficar na frente de tudo
                self.master.attributes('-topmost', 'true')
                #Restaurar/mostrar a janela
                self.master.deiconify()
                #Reproduzir o som
                self.playsound()
                #Alterar a cor do visualTimer(cronometro) para vermelho
                visualTimer.config(fg="red")
                #Incluir mensagem no grid no grid
                messageLabel.grid(row=2, column=1, columnspan=2, sticky=tk.E+tk.W)
                #Criar um botão para resetar "cronometro"
                self.resetButton = tk.Button(
                    self,
                    text = "Me avise novamente",
                    command = self.run,
                    anchor = tk.CENTER,
                    font = "Times 12 bold",
                    height = 1,
                    relief = tk.GROOVE,
                    justify="center")
                #Inserir botão na janela
                self.resetButton.grid(row=5, column=1, sticky=tk.E+tk.W)
                #Criar um botão para sair do programa
                self.exitButton = tk.Button(
                    self,
                    text = "Para com isso!",
                    command = on_closing,
                    anchor = tk.CENTER,
                    font = "Times 12 bold",
                    height = 1,
                    relief = tk.GROOVE,
                    justify="center")
                #Inserir botão na janela
                self.exitButton.grid(row=5, column=2, sticky=tk.E+tk.W)

        #Iniciar "cronometro"
        update_timer(timeinseconds)

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