'''
 que precisa para criar um app
1 - um campo de texto para ser traduzido
1 - um campo de texto para o que foi traduzido
1 - selecionar a linguagem de entrada 
1 - selecionar a linguagem de saida 
1 - um botão para traduzir 
'''
from tkinter import Frame, Tk, ttk, Text, Button
from googletrans import Translator
from ttkthemes import ThemedTk
from ttkbootstrap import Style

translator = Translator()

def traduzir(evento=None):
    # vai da primeira letra ate o final  '1.0 ate and' não existe linha 0 dentro do tk 1 linha coluna 0 = 1.0
    texto = entrada.get('1.0', 'end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    #print(texto, src, dest)
    resultado = translator.translate(text=texto, src=src, dest=dest)
    

    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0',resultado.text)
    saida.configure(state='disabled')

# janela tk default
#janela = Tk()
# para ver os temas https://ttkthemes.readthedocs.io/en/latest/themes.html
# quando copia o tema tem que começa com letra minuscula no site esta Black mas vai fica black em theme=

# janela do ttkthemes
#janela= ThemedTk(theme='winxpblue')

# janela do ttkbootstrap thema style estilo tudo a mesma coisa
# https://ttkbootstrap.readthedocs.io/en/latest/
# vai na Handbook para ver os temas
style =  Style(theme='superhero')

janela = style.master

janela.title('TRADUTOR DO ALFREDO')
# esse frame é para colori as outros frames
frame_geral= ttk.Frame()
values = ['pt', 'es', 'en', 'hi', 'ru', 'zh-tw']


# entrada
# foi criado um contener = frame para colocar as entradas de saida e entra de lado a alado
# no caso o frame_entrada vai vira argumento no label, combo, entrada
frame_entrada = ttk.Frame(frame_geral)

# text é a etiquela = label pode ser qualquer nome 
label_entrada = ttk.Label(
    frame_entrada, 
    text='Entrada', 
    font=(None, 20)
    )

combo_entrada = ttk.Combobox(
    frame_entrada,
    values=values,
    font=(None, 20) 
     )

combo_entrada.set('pt')


# como seta isso para ficar de lado a lado nesse caso usou o grip para isso
# colocamos uma diferença entre as linhas entra e saida
# o padx usado para aumenta a distancia no sentido horizontal para direita 
label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)
frame_entrada.pack()

# 10 na vertical e 50 caracter na horizontal
entrada = Text(frame_geral, height=10, width=50, font=(None, 15))
# esse padx faz as alterais da janela como uma borda
# para redimencionar faz  fill='both' como argumento de pack junto com  expand faz com que a janela se redimencione
entrada.pack(padx=10, pady=10, fill='both', expand='yes')


# saida
frame_saida = ttk.Frame(frame_geral)

label_saida = ttk.Label(
    frame_saida,
    text='Saida', 
    font=(None, 20)
    )

combo_saida = ttk.Combobox(
    frame_saida,
    values=values,
    font=(None, 20) 
     )

combo_saida.set('en')

label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1, padx=10, pady=10)
frame_saida.pack()

saida = Text(
    frame_geral,
    height=10, 
    width=50,
    font=(None, 15),
    # desativa a entrada de texto no, state = estado desabilitado
    state='disabled'
    )


saida.pack(padx=10, pady=10, fill='both', expand='yes')


botão = ttk.Button(
    frame_geral,
    text='Traduzir!',
    #font=(None, 20),
    command=traduzir
    )

botão.pack(fill='both', padx=20,pady=20)
# todo bind gera um evento por isso na função traduzir recebeu como argumento event=None
# que quer dizer para não gera nenhum evento ou novo evento mas no caso abaixo ao aperta enter vai traduzir
janela.bind('<Return>', traduzir)
frame_geral.pack()

janela.mainloop()
