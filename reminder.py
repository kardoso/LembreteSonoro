#!/usr/bin/python3

# usado para pegar diretório em que o programa está
import os
# módulo tkinter para exibir janelas
import tkinter as tk
# para exibir caixa de diálogo
from tkinter import messagebox
# para procurar/selecionar arquivo
from tkinter import filedialog
# para reproduzir o som (no windows)
import winsound
# para converter segundos para o formato HH:MM:SS
from datetime import timedelta

# Variáveis das strings no programa
# Botão para importar áudio
import_audio = "Importar arquivo de áudio"
# Título da janela que abre para selecionar arquivo de audio
dialog_audio = "Selecione o áudio"
# Label quando nada é selecionado
none_selected = "Nenhum arquivo selecionado"
# Label quando um arquivo inválido é selecionado
invalid_file = "Selecione um arquivo válido"
# Label quando um arquivo válido é selecionado
# + é contatenado com a path do arquivo
selected_file = "Aquivo selecionado: "
# Label perdindo para informar o tempo do ciclo
ask_period = "Informe a periodicidade: "
# Botão para iniciar o programa
start_string = "Iniciar"
# label para pedir para o usuário digitar o que deseja lembrar
remember_ask = "Quero lembrar de "
# Label para informar o usuário de lembrar...
# Vai ser concatenado com a ação que o usuário deseja lembrar
remember_to = "Se lembre de "
# Botão para recomeçar o temporizador
remind_again = "Me avise novamente"
# Botão para fechar o programa
stop_reminding = "Para com isso!"
# Label do diálogo ao encerrar o programa
dialog_question = "Já vai?"
# Confirmar o encerramento do programa
dialog_confirm = "Sim (Enter)"
# Negar o encerramento do programa
dialog_cancel = "NÃO (Esc)"

# Largura da janela
window_width = 400
# Altura da janela
window_height = 200

# Variável com o path do icone do programa
program_icon = "res/reminder.ico"

# Criar nova janela principal
root = tk.Tk()
# Definir título da janela
root.title("Lembrete Sonoro")
# Pontos do centro da tela
centerX = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
centerY = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
# Definir tamanho da janela
root.geometry("%dx%d" % (window_width, window_height))
# Centralizar janela
root.geometry(
    "+%d+%d" % (
        centerX - (window_width/4),
        centerY - (window_height/4)))
# Não permitir redimensionamento
root.resizable(False, False)
# Definir icone do programa no windows
if os.name == 'nt':
    root.iconbitmap(bitmap=program_icon)


# Classe principal do programa
class Application(tk.Frame):
    # Iniciar a janela
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # Adicionar campos ao programa
    def create_widgets(self):
        # Remover todos os campos presentes no programa
        for slave in self.grid_slaves():
            slave.grid_remove()
            slave.grid_forget()
            slave.destroy()
        # Criar o botão para importar arquivos
        self.importButton = tk.Button(
            self,
            text=import_audio,
            command=self.setsound,
            anchor=tk.CENTER,
            font="Times 12 bold",
            width=20,
            height=1,
            background="#5e4b8b",
            activebackground="#5e4b8b",
            activeforeground="white",
            foreground="white",
            relief=tk.GROOVE,
            justify="center")
        # Inserir botão na janela
        self.importButton.grid(row=1, column=1, columnspan=2, sticky=tk.E+tk.W)

        # O path do arquivo a ser carregador
        self.soundpath = ""
        # Variável de texto informando a situação do arquivo
        # Se foi importado ou não, ou se o arquivo é válido
        self.fileResponse = tk.StringVar(value="Nenhum arquivo selecionado")
        # Criar label para mostrar a situação do arquivo
        self.fResponse = tk.Label(
            self,
            text=none_selected,
            textvariable=self.fileResponse,
            font=("Helvetica", 9),
            foreground="red")
        # Inserir label na janela
        self.fResponse.grid(row=2, column=1, columnspan=2)

        # Label para perguntar o que o usuário deseja lembrar
        self.rememberaskLabel = tk.Label(
            self,
            text=remember_ask,
            font=("Helvetica 10 bold"),
            justify="center")
        # Inserir label na janela
        self.rememberaskLabel.grid(row=3, column=1)
        # O que o usuário deseja lembrar
        # Vai ser usado para ler o que o usuário digitar
        self.remember_this = tk.StringVar(self, value="comentar")
        # O que o usuário deseja lembrar
        self.rememberEntry = tk.Entry(
            self,
            textvariable=self.remember_this,
            font=("Helvetica 10 bold"),
            justify="center")
        # Inserir label na janela
        self.rememberEntry.grid(row=3, column=2)

        # Label para informar ao usuário o que fazer
        self.periodLabel = tk.Label(
            self,
            text=ask_period,
            font=("Helvetica 10 bold"),
            justify="center")
        # Inserir label na janela
        self.periodLabel.grid(row=4, column=1)

        # Variável com o período(tempo do ciclo do programa)
        self.period = tk.IntVar(self, value=30)
        # Input para entrada do dado period
        self.enterperiod = tk.Entry(
            self,
            textvariable=self.period,
            font=("Helvetica 10"),
            justify='center')
        # Inserir entry na janela
        self.enterperiod.grid(row=4, column=2)

        # Opções de tempo
        self.OPTIONS = ["Horas", "Minutos", "Segundos"]
        # Varíavel com o tipo de tempo, padrão "Minutos"
        self.timeType = tk.StringVar(self, self.OPTIONS[1])
        # Menu dropdown com as opções de tempo
        self.timeChooser = tk.OptionMenu(self, self.timeType, *self.OPTIONS)
        # Inserir dropdown na janela
        self.timeChooser.grid(row=5, column=2, sticky="ew")

        # Botão para iniciar o programa
        self.startButton = tk.Button(
            self,
            text=start_string,
            state=tk.DISABLED,
            command=self.run,
            anchor=tk.CENTER,
            font="Times 12 bold",
            background="#5e4b8b",
            activebackground="#5e4b8b",
            foreground="white",
            activeforeground="white",
            relief=tk.GROOVE,
            justify="center")
        # Inserir o botão na janela
        self.startButton.grid(row=7, column=1, columnspan=2, sticky=tk.E+tk.W)

        # Configurar altura das linhas do programa
        self.grid_rowconfigure([1, 2, 3, 4, 5, 6, 7], minsize=26)

    # Definir o som que será reproduzido
    def setsound(self):
        # Pedir para o usuário selecionar o arquivo WAV
        fpath = filedialog.askopenfile(
            # Iniciar o diretório em que o programa está
            initialdir=os.path.dirname(os.path.abspath(__file__)),
            title=dialog_audio,
            filetypes=(
                ("Arquivos .wav", "*.wav"),
                ("all files", "*.*")))
        # Se o arquivo de áudio foi selecionado
        if fpath is not None:
            # Se o nome terminar com '.wav'
            # winsound reproduz apenas arquivos .wav
            if fpath.name.endswith('.wav'):
                self.soundpath = fpath.name
                self.fileResponse.set(selected_file+str(fpath.name))
                self.fResponse.config(fg="green")
                self.startButton.config(state=tk.ACTIVE)
            else:
                self.fileResponse.set(invalid_file)
                self.fResponse.config(fg="#ff7f50")
                self.startButton.config(state=tk.DISABLED)
        # Se não foi selecionado nenhum arquivo
        else:
            self.fileResponse.set(none_selected)
            self.fResponse.config(fg="red")
            self.startButton.config(state=tk.DISABLED)

    # Reproduzir som
    def playsound(self):
        # SND_LOOP - Reproduz com loop até o usuário tomar alguma ação
        # SND_ASYNC - Reproduz de forma assíncrona, sem travar o programa
        winsound.PlaySound(
            self.soundpath,
            winsound.SND_LOOP | winsound.SND_ASYNC)

    # Parar de reproduzir som
    def stopsound(self):
        winsound.PlaySound(None, winsound.SND_ALIAS)

    # Iniciar ciclo do programa
    def run(self):
        # Parar de raproduzir som se estiver reproduzindo
        self.stopsound()
        # Remover todos os campos presentes programa
        for slave in self.grid_slaves():
            slave.grid_remove()
            slave.grid_forget()
            slave.destroy()

        # Label com a mensagem ao concluir a contagem
        messageLabel = tk.Label(
            self,
            text=remember_to+self.remember_this.get(),
            font=("Helvetica 12 bold"),
            fg="#ff7f50")

        # Criar uma label apenas para mostrar o texto
        visualTimer = tk.Label(
            self,
            text="00:00:00",
            font=("Helvetica 24 bold"),
            fg="#5e4b8b")
        # Incluir label no grid
        visualTimer.grid(row=3, column=1, columnspan=2, sticky=tk.E+tk.W)

        # Recebe a variável que o usuário digitou convertida em segundos
        timeinseconds = 0
        if(self.timeType.get() == self.OPTIONS[0]):
            # Horas
            timeinseconds = (self.period.get() * 60) * 60
        elif(self.timeType.get() == self.OPTIONS[1]):
            # Minutos
            timeinseconds = self.period.get() * 60
        elif(self.timeType.get() == self.OPTIONS[2]):
            # Segundos
            timeinseconds = self.period.get()

        # Atualizar a label 'visualTimer'
        # e quando o tempo chegar a zero reproduz o som
        # mostra opções e mensagem de lembrete
        def update_timer(t):
            if(t >= 0):
                # Atualizar o texto da label visualTimer no formato de horas
                visualTimer.configure(text=str(timedelta(seconds=t)))
                # Decrementar dos segundos
                t -= 1
                # Esperar 1 segundo e fazer a recursão
                self.master.after(1000, update_timer, t)
            else:
                # Fazer a janela ficar na frente de tudo
                self.master.attributes('-topmost', 'true')
                # Restaurar/mostrar a janela
                self.master.deiconify()
                # Reproduzir o som
                self.playsound()
                # Alterar a cor do visualTimer(cronometro) para vermelho
                visualTimer.config(fg="#ff7f50")
                # Incluir mensagem no grid no grid
                messageLabel.grid(
                    row=2,
                    column=1,
                    columnspan=2,
                    sticky=tk.E+tk.W)
                # Criar um botão para resetar "cronometro"
                self.resetButton = tk.Button(
                    self,
                    text=remind_again,
                    command=self.run,
                    anchor=tk.CENTER,
                    font="Times 12 bold",
                    height=1,
                    background="#5e4b8b",
                    activebackground="#5e4b8b",
                    activeforeground="white",
                    foreground="white",
                    relief=tk.GROOVE,
                    justify="center")
                # Inserir botão na janela
                self.resetButton.grid(row=5, column=1, sticky=tk.E+tk.W)
                # Criar um botão para sair do programa
                self.exitButton = tk.Button(
                    self,
                    text=stop_reminding,
                    command=on_closing,
                    anchor=tk.CENTER,
                    font="Times 12 bold",
                    background="#ff7f50",
                    activebackground="#ff7f50",
                    activeforeground="white",
                    foreground="white",
                    height=1,
                    relief=tk.GROOVE,
                    justify="center")
                # Inserir botão na janela
                self.exitButton.grid(row=5, column=2, sticky=tk.E+tk.W)

        # Iniciar "cronometro"
        update_timer(timeinseconds)


class ExitDialog(tk.Toplevel):
    def __init__(self, parent, title=None):
        tk.Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.buttonbox()
        self.grab_set()

        # Definir icone no windows
        if os.name == 'nt':
            self.iconbitmap(bitmap=program_icon)

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master):
        # Criar corpo do diálogo. Retorna widget
        # Foco inicial. Método deve ser sobrescrito
        return tk.Label(master, text=dialog_question).grid(row=0)

    def buttonbox(self):
        # Adicionar botões padrão
        box = tk.Frame(self)

        w = tk.Button(
            box,
            text=dialog_confirm,
            width=10,
            background="#ff7f50",
            activebackground="#ff7f50",
            activeforeground="white",
            foreground="white",
            command=self.ok,
            default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(
            box,
            text=dialog_cancel,
            width=10,
            background="#5e4b8b",
            activebackground="#5e4b8b",
            activeforeground="white",
            foreground="white",
            command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # Botões padrão

    # Confirmar
    def ok(self, event=None):
        if not self.validate():
            # se o usuário não escolheu nada, mas fez algo
            self.initial_focus.focus_set()  # Focar novamete
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        # Sair do programa se confirmar
        self.master.destroy()

    # Cancelar
    def cancel(self, event=None):
        # Focar janela atual se cancelar
        # Focar na janela pai
        self.destroy()

    #
    # Base dos comandos
    def validate(self):
        return 1  # override

    def apply(self):
        pass  # override


# Protocolo de saída
# Quando for fechar o programa executar essa função
# Essa função exibe uma caixa de diálogo
def on_closing():
    ExitDialog(root)


# Definir o protoclo de saída
root.protocol("WM_DELETE_WINDOW", on_closing)


if __name__ == '__main__':
    # Definir classe que vai ser o programa
    # como parâmetro a janela principal
    app = Application(master=root)
    # Iniciar o programa
    app.mainloop()
