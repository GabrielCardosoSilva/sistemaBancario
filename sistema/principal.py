from time import sleep

# menu de opções do sistema bancario
menu = '''\033[36m
——————————————————————
   Sistema Bancario
——————————————————————

\033[32m[ D ] → Depositar
\033[31m[ S ] → Sacar
\033[33m[ E ] → Extrato
\033[34m[ F ] → Saida Do Programa

\033[mOpção: '''

saldo = 0

limite_saque = 3

extrato = []


while True:
    options = input(menu)

    # opção de encerrar o programa
    if options.strip().upper()[0] in "F":
        print("\033[31m\nFim Do Serviço Bancario, Volte Sempre...\n\n\033[m")
        break

    # opção de depositar dinheiro
    elif options.strip().upper()[0] in "D":
        print("\033[32m\n→Deposito: \033[m")

        # tratamento de erro para nao entrar valor invalido
        try:
            deposito = float(input("  Valor Que Deseja Depositar: R$"))

            if deposito > 0:
                extrato.append(f"{'Deposito':<10}R${deposito:.2f}")
                saldo += deposito
                print(f"\033[32m\n✅Valor de R${deposito:.2f} Adicionado com Sucesso.\033[m")

            else:
                print("\n⛔\033[31mDeposito Invalido Tente Novamente...\033[m")

        except:
            print("\n⛔\033[31mDeposito Invalido Tente Novamente...\033[m")

    # opção de sacar dinheiro
    elif options.strip().upper()[0] in "S":
        print("\033[31m\n→Sacar: \033[m")

        if limite_saque == 0:
            print("\n⛔\033[31mLimite De Saque Diario Alcançado...\033[m")

        else:
            if saldo > 0:

                # tratamento de erro para nao entrar valor invalido
                try:
                    saque = float(input("  Valor Que Deseja Sacar: R$"))

                    if saque == 0 or saque > saldo:
                        print("\n⛔\033[31mSaque Indisponivel Tente Novamente...\033[m")

                    elif saque < saldo and limite_saque > 0:
                        extrato.append(f"{'Saque':<10}R${saque:.2f}")
                        saldo -= saque
                        limite_saque -= 1
                        print(f"\033[32m\n✅Valor de R${saque:.2f} Retirado com Sucesso.\033[m")
                except:
                    print("\n⛔\033[31mSaque Invalido Tente Novamente...\033[m")

            else:
                print("\n⛔\033[31mSaldo Vazio, Deposite algo primeiro.\033[m")

    # opção de visualizar o extrato bancario
    elif options.strip().upper()[0] in "E":
        print("""\033[33m
==========================
    EXTRATO BANCARIO
==========================
        \033[m""")

        for h in extrato:
            print(f"\033[33m→{h}\033[m")

        print(f"{'Saldo Atual:':<15}R${saldo:.2f}\n")

    else:
        print(f"\033[31m\n\'{options}\' Não é uma opção valida, Tente Novamente...\033[m\n")
    sleep(1)
