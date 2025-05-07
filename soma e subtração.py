import math
def soma(a,b):
    return a+b
def subtracao (a,b):
    return a-b
def multiplicacao (a,b):
    return a*b
def divisao (a,b):
    return a/b
def potencia (a,b):
    return a**b
def porcentagem (a,b):
    return (a*b)/100
print('Escolha a operação:')
print('+ soma')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('** potência')
print('% porcentagem')
opcao=input('digite a opção(+/-/*/(/)/**/%):')
num1=float(input('Digite o n°'))
num2=float(input('Digite outro n°'))
if opcao=='+':
    print('Resultado:',soma(num1,num2))
elif opcao =='-':
    print('Resultado:',subtracao(num1,num2))
elif opcao=='*':
    print('Resultado:',multiplicacao(num1,num2))
elif opcao =='/':
    print('Resultado:',divisao(num1,num2))
elif opcao =='**':
    print('Resultado:',potencia(num1,num2))
elif opcao=='%':
    print('Resultado:',porcentagem(num1,num2))
else:
    print('opção inválida')
import tkinter as Tk
#Função chamada ao clicar nos botoes
def clicar (botao):
    atual = entrada.get()
    if botao == "=":
        try:
            resultado = str(eval(atual))
            entrada.delete(0, Tk.END)
            entrada.insert(0, resultado)
            #Adiciona ao histórico
            historico_text.insert(Tk.END, f"{atual}={resultado}\n")
        except:
            entrada.delete(0, Tk.END)
            entrada.insert(0, "erro")
    elif botao == "C":
        entrada.delete(0, Tk.END)
    else:
        entrada.insert(Tk.END, botao)
# Janela principal
janela = Tk.Tk()
janela.title("Calculadora")
#Entrada de texto
entrada=Tk.Entry(janela,width=16,font=("Arial",24), borderwidth=2,relief="solid",justify="right")
entrada.grid(row=0,column=0,columnspan=4)
#Botoes
botoes=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","0",
    "+","-","**","%",
    " ","C","="," "
]
linha=1
coluna=0
for botao in botoes:
    Tk.Button(janela,text=botao,width=5,height=2,font=("Arial",18),command=lambda b=botao: clicar(b)).grid(row=linha,column=coluna)
    coluna += 1
    if coluna >3:
        coluna=0
        linha+=1
#Caixa de historico ao lado direito
historico_label= Tk.Label(janela,text="Histórico", font=("Arial",14,"bold"))
historico_label.grid(row=0,column=4,padx=10)
historico_text=Tk.Text(janela,width=25,height=10,font=("Arial",14))
historico_text.grid(row=1, column=4,rowspan=5,padx=10,pady=5)
janela.mainloop()
