import os
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(PASTA_ATUAL, "cadastros.txt")
print ("seja bem vindo(a) ao nosso site")
while True:
    opcao = input("1 - login\n2 - cadastro\nEscolha: ")
    if opcao == "1":
        print("----TELA DE LOGIN----")
        with open(CAMINHO_ARQUIVO, "r") as arquivo:
            linhas = arquivo.readlines() 
        while True:
            email = input("digite seu E-mail: ")
            email_encontrado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if len(dados) >= 2 and dados[1] == email:
                    email_encontrado = True
                    break
            if email_encontrado:
                print("E-mail encontrado!")
                break
            else:
                print("E-mail não encontrado. Tente novamente.")
        while True:
            senha = input("agora digite sua senha: ")
            login_sucesso = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if len(dados) >= 4:
                    if dados[1] == email and dados[3] == senha:
                        login_sucesso = True
                        break
            if login_sucesso:
                print("\n✅ Acesso permitido!")
                break  
            else:
                print("\n❌ Senha incorreta! tente novamente")
    elif opcao == "2":
        print("----TELA DE CADASTRO----\n2")
        print ("faça seu cadasatro conosco")
        print ("precisamos de algumas informações...")
        nome = input('seu nome: ')
        while True:
            email = input('seu E-mail: ')
            if "@" in email:
                print("E-mail valido")
                break
            else:
                print("E-mail invalido, digite um E-mail valido")
        while True:
            idade = int(input("idade: "))
            if idade >= 18:
                print("cadastro aceito")
                break
            else:
                print("acesso negado, e preciso ter 18 anos para prosseguir")
        print(f"parabems {nome} cadastro criado com sucesso")
        print("agora crie uma senha")
        senha = input("crie uma senha forte...")
        with open(CAMINHO_ARQUIVO,"a") as arquivo:
            arquivo.write(f"{nome},{email},{idade},{senha}\n")

        print(f"cadastro finalizado ultilize {email} e sua senha para fazer login")
    else:
        print("opção invalida. escolha 1 ou 2.\n")