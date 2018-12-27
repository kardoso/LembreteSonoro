# Lembrete Sonoro

![Lembrete Sonoro](docs/LembreteSonoro_icon.png)

Um programa para te lembrar de fazer algo reproduzindo um áudio de sua escolha em ciclos.

Se você não está aqui pelo código pule para a sessão de [como usar](#Como-usar).

### Tópicos
* [Requerimentos](#requerimentos)

* [Personalizar](#Personalizar)

* [Montar o executável](#Montar-o-executável)

* [Como usar](#Como-usar)


## Requerimentos
* [Python 3](https://www.python.org/downloads/)

* [Tkinter](https://tkdocs.com/tutorial/install.html) - Uma biblioteca gráfica para python.<br> 
A partir da versão 3.1 do Python essa biblioteca já está inclusa nas distribuiçõs Python.<br>
No windows pode ser instalado usando o prompt de comando ou o IDLE:<br>
No prompt de comando utilize o comando `python` para abrir a linha de comando Python.<br>
Para instalar o Tkinter utilize os dois comandos seguintes:<br>
`import tkinter`<br>
`tkinter._test()`

* [winsound](https://docs.python.org/3.7/library/winsound.html) - Uma biblioteca de interface de som para windows.<br>
Também já está incluso nas distribuições do Python, basta importar.

* [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/)(Caso queira fazer a build do programa) - 
Um dos muitos programas que compila programas Python em executáveis stand-alone.


## Personalizar
O programa tem apenas uma função: Lembrar o usuário de algo.<br>

Porém as palavras mostradas ao usuário podem ser alteradas.<br>

No início do script estão todas as variáveis do tipo string que serão mostradas ao usuário.<br>

Todas as variáveis têm comentários, então é fácil saber qual altera o quê.

Por exemplo: a caixa de diálogo de encerramento do programa.

![Diálogo de encerramento](docs/exit_dialog.png)

Todas as palavras visíveis são definidas pelas variáveis(exceto o título da janela).

"Já vai?" é o valor da variável dialog_question;

"Sim (Enter)" é o valor da variável dialog_confirm;

"NÃO (Esc)" é o valor da variável dialog_cancel.

Simples, não?

## Montar o executável
Para simplificar, há um arquivo batch com os comandos necessários.

Execute o arquivo de lotes `setup.bat` no windows.<br>
É necessário ter o pyinstaller instalado, pois ele é quem vai criar o executável.

Isso vai criar a pasta `Lembrete Sonoro` com o programa dentro da pasta `dist`.


## Como usar
Se você não veio aqui pelo código, mas sim pelo programa
volta lá no topo da página e clica em um botão verde com o texto "Clone or Download" e depois em "Download ZIP".<br>
O programa vai estar dentro da pasta `Lembrete Sonoro`.

Este é o programa:

![Inicial](docs/initial.png)

* No primeiro botão você seleciona o áudio que vai tocar.<br>(No momento apenas no formato .wav)
* Logo abaixo do botão vai mostrar o arquivo que você carregou.
* Na caixa abaixo você informa a ação que você quer fazer depois que o temporizador chegar ao fim.
* Mais abaixo você informa o tempo, podendo escolher entre horas, minutos e segundos.
* E, enfim, o botão para iniciar o programa.<br>(Ele fica ativo apenas quando há um arquivo de som selecionado)
* Ao iniciar você pode minimizar e ir fazer outra coisa

Ao final do tempo o som que você escolheu vai tocar e a janela aparecerá na tela com uma mensagem:
![Final da contagem](docs/end.png)

O som toca em loop até uma decisão ser tomada.
* O botão da esquerda recomeça o ciclo e começa a contar novamente.
* O botão da direita exibe a caixa de diálogo para confirmar a saída do programa.
