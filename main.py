import datetime

# Coleta do horário atual
hora_atual = datetime.datetime.now().hour

# Definição da saudação com base no horário
if hora_atual < 12:
    saudacao = "Bom dia"
elif hora_atual < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# Coleta de informações do paciente
nome = input("Qual é o nome do paciente? ").capitalize()

especie_valida = False
while not especie_valida:
    especie = input("Qual é a espécie do paciente? [C/G] ").lower()
    if especie == "c" or especie == "cão":
        especie = "🐶"
        especie_valida = True
    elif especie == "g" or especie == "gato":
        especie = "🐱"
        especie_valida = True
    else:
        print("Espécie inválida. Por favor, insira C para cão ou G para gato.")

alimentacao = ""
while alimentacao != "s" and alimentacao != "n":
    alimentacao = input(f"O paciente se alimentou? [S/N] ").lower()

observacao_alimentacao = input("Observação sobre a alimentação do paciente? ")
if observacao_alimentacao == "n":
    observacao_alimentacao = ""

urina = ""
while urina != "s" and urina != "n":
    urina = input(f"O paciente urinou? [S/N] ").lower()

observacao_urina = input("Observação sobre a urina do paciente? ")
if observacao_urina == "n":
    observacao_urina = ""

fezes = ""
while fezes != "s" and fezes != "n":
    fezes = input(f"O paciente evacuou? [S/N] ").lower()

observacao_fezes = input("Alguma observação sobre as fezes do paciente? ")
if observacao_fezes == "n":
    observacao_fezes = ""

evolucao = ""
while evolucao != "s" and evolucao != "n":
    evolucao = input(f"A evolução do paciente está dentro do esperado? [S/N] ").lower()

observacao_evolucao = input("Alguma observação sobre a evolução do paciente? ")
if observacao_evolucao == "n":
    observacao_evolucao = ""

previsao_alta = ""
while previsao_alta != "s" and previsao_alta != "n":
    previsao_alta = input(f"Previsão de alta? [S/N] ").lower()
observacao_previsao_alta = input("Alguma observação sobre a previsão de alta? ")
if observacao_previsao_alta == "n":
    observacao_previsao_alta = ""
elif len(observacao_previsao_alta) > 2:
    observacao_previsao_alta = observacao_previsao_alta.capitalize()

# Montagem do boletim médico
boletim = boletim = f"====================================================\n\n\n" \
                    f" \n\n\n" \
                    f"{saudacao}. Aqui estão as informações sobre o paciente {nome}. {especie}\n" \
                    f"Alimentou-se? ({'X' if alimentacao == 's' else ' '})Sim ({'X' if alimentacao == 'n' else ' '})Não. {observacao_alimentacao}\n" \
                    f"Urinou? ({'X' if urina == 's' else ' '})Sim ({'X' if urina == 'n' else ' '})Não. {observacao_urina}\n" \
                    f"Evacuou? ({'X' if fezes == 's' else ' '})Sim ({'X' if fezes == 'n' else ' '})Não. {observacao_fezes}\n" \
                    f"Evolução dentro do esperado? ({'X' if evolucao == 's' else ' '})Sim ({'X' if evolucao == 'n' else ' '})Não. {observacao_evolucao}\n" \
                    f"Previsão de alta? ({'X' if previsao_alta == 's' else ' '})Sim ({'X' if previsao_alta == 'n' else ' '})Não. {observacao_previsao_alta}\n" \

# Exibição do boletim médico
#somente print
print(boletim)

