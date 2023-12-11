# #começa com variaveis zeradas 3 TENTATIVA QUESTAO 1


imp8 = 0
imp18 = 0
imp28 = 0

# INICIAR COM INPUT
# COMEÇA COM UM INPUT PARA SABER O SALARIO
renda = float(input("Digite sua renda: "))
# FAZER UMA FUNÇÃO
renda8 = (renda * 0.08 )
renda18 =( renda * 0.18 )
renda28 =( renda * 0.28 )

# VOU FAZER UNS IF ELSE ELIF PARA CLASSIFICAR A RENDA ENTRE ISENTO, 0.08, 0.18, 0.28
if renda <= 2000.00:
    print("ISENTO") #ISEÇÃO USANDO O MAIOR E IGUAL
elif 2000.01 <= renda <= 3000.00: #USANDO AGORA ELA NO MEIO PRA ASSIM COMPARAR A RENDA COM 2 TERMOS DIFERENTE
     imp8 = renda * 0.08 # USANDO O PRINCIPIDE DE MULTIPLICAR E DIVIDIR POR CEM MAS NAO PRECISA JA QUE O 0,08 JA ESTAR DIVIDIDO PELO O MESMO
     print(f"Valor do Imposto de 8%: {imp8:.2f}") #USANDO A FUNCAO ".2F" PARA CORTAS AS PROXIMAS CASAS DECIMAIS E FICAR SO 2
elif 3000.01 <= renda <= 4500.00:
     imp18 = renda * 0.18 
     print(f"Valor do Imposto de 18%: {imp18:.2f}")  #PRINT BASICO COM A FUNÇÃO DAS CASAS DECIMAIS
if renda > 4500.00:
     imp28 = renda * 0.28
     print(f"Valor do Imposto de 18%: {imp28:.2f}") # AGR FOI APENAS REPETIR O PROCESSO



#QUESTAO 2



salario=float(input("digite seu salario atual: "))

#PECO O SALARIO COM INPUT DE FLOUT PARA NUMEROS QUEBRADOS 

if 0 <= salario <= 400.00: 

#DECISAO 

    reajuste15 = (salario * 15 ) / 100 

#SE SIM APLICAR A FORMULA DE PORCENTAGEM

    print(f"novo salario: {reajuste15 + salario:.2f}" ) 

#FAZER O PRINT USANDO A FORMULA ":.2"PARA CORTAR AS CASA DECIMAIS Q SOBRAM

    print(f"reajuste ganho: {reajuste15:.2f}")

#IMPRIMIR O REAJUSTE GANHO           

    print("15%")
#

#AGORA SO REPETIR TUDO MUDANDO OS NUMEROS E SO repetir

if 400.01 <= salario <= 800.00:

    reajuste12 = (salario * 12 ) / 100

    print(f"novo salario: {reajuste12 + salario:.2f}" )

    print(f"reajuste ganho: {reajuste12:.2f}")

    print("12%")

if 800.01 <= salario <= 1200.00:

    reajuste10 = (salario * 10 ) / 100

    print(f"novo salario: {reajuste10 + salario:.2f}" )

    print(f"reajuste ganho: {reajuste10:.2f}")

    print("10%")

if 1200.01 <= salario <= 2000.00:

    reajuste7= (salario * 7 ) / 100

    print(f"novo salario: {reajuste7 + salario:.2f}" )

    print(f"reajuste ganho: {reajuste7:.2f}")

    print("7%")

if salario > 2000.01:

    reajuste4= (salario * 4 ) / 100

    print(f"novo salario: {reajuste4 + salario:.2f}" )

    print(f"reajuste ganho: {reajuste4:.2f}")
    
    print("4%")

#QUESTAO 3


senha= 2002

#DETERMINO A SENHA A SER SEGUIDA COMO CORRETA

user = int(input("digite sua senha:"))

#PEÇO A SENHA DO USER PARA COMPARAR COM A SENHA DEFINIDA

while user != senha:

#FAÇO O WHILE PARA FICAR RODADO O LOOP usando a condiçao de != diferente

    print("senha invalida")

#CONTATENADO COM O WHILE ELE VAI FICAR RODADO ATE O SER VERDADEIRO

    user = int(input("digite sua senha:"))

#CONTATENADO COM O WHILE ELE VAI FICAR RODADO ATE O WHILE SER VERDADEIRO

print("acesso permitido")

#FORA DO WHILE ELE VAI SER EXECUTADO QUANDO O WHILE TERMINAR 


#QUESTAO 4
def obter_DDD_e_cidade():
    # lista q mapeia DDD para cidades
    ddds_cidades = {
        61: "Brasília",
        71: "Salvador",
        11: "São Paulo",
        21: "Rio de Janeiro",
        32: "Juiz de Fora",
        19: "Campinas",
        27: "Vitória",
        31: "Belo Horizonte"
    }#assim fica mais facil doq apenas criar uma variavel e comparar usando varios if's e else's
    

    while True:
        #o while true e o while normal com a condicao q ele so pararar com a outra funcao chmada break 
        try:
            numero = int(input("Digite um DDD: "))
            #entrada com o ddd numa variavel int
            if numero in ddds_cidades:
                #um if para ver se o numero=ddd esta na lista de cidade e ddd
                cidade = ddds_cidades[numero]
                #ver o ddd ta em alguma cidade cadastrado
                print(f"você digitou o DDD: {numero} - Cidade: {cidade}")
                #pra imprimir o dd e a cidade q ta na lista
                break
            #para o loop se tudo ta certo
            else:
                #se der erro nos passo atras iniciar 
                print("DDD não cadastrado.")
        except ValueError:
            print("Por favor, digite um DDD válido.")

# invocar a funcao
obter_DDD_e_cidade()

#QUESTAO 5
numeros = []
#variavel para criar uma lista 
for i in range(5):
#range para percorrer o input o tanto de vezes dentro dos parenteses

    numero = int(input(f"digite o {i + 1} numero: "))
    #variavel criando com numero int com uma f de chaves para poder receber o i + 1 
    #assim toda vez q rodado o input ele aumentara o i para mais 1

    numeros.append(numero)
    #seria para guarda os numneros do input dentro da lista numeros



numeros_pares = [num for num in numeros if num % 2 == 0]
# os numeros na variavel numeros dividindo os por 2 e vendo se o resto representado por %
# é igual a 0 se for vai ser guardado na variavel numeros_pares 


quantidade_numeros_pares = len(numeros_pares)
#criando uma variavel de quanti usamos a funçao len para nos numeros pares assim tendo a quaintidade

print(f"A quantidade de números pares é: {quantidade_numeros_pares}")
#print com o f e funcao de {} para ter uma variavel dentro do texto


#QUESTAO 6
numeros = []
#uma variavel com uma lista aberta
soma_positivos = 0
#variavel da soma dos positivos zeradas
quantidade_positivos = 0
#variavel dos positivos zeradas
for x in range(5): 
#loop para fazer o input rodar 5x
    numero = float(input(f"Digite o {x+1}º numero:"))
#receber os numeros 
    numeros.append(numero)
    #amarzenar os numeros recebido do input na variavel numeros de lista
    if numero > 0:
#ver se os numero sao maiore que 0
        soma_positivos += numero
        quantidade_positivos += 1
if quantidade_positivos > 0:
#definir os positivos 
    media_positivos = soma_positivos / quantidade_positivos
# fazer o calculo de media das somas do positivos
    print(f"A média dos números positivos é: {media_positivos}")
#print com fucao de variavel dentro de string
else:
    print("Não foram inseridos números positivos.")
    # se a caso nao for inseridos os numeros positivos
