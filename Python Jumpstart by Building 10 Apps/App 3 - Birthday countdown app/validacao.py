import datetime

def minha_data():

    ano = int(input('informe o seu ano de nascimento [YYYY]: '))
    mes = int(input('informe o seu mes de nascimento [MM]: '))
    dia = int(input('informe o seu dia de nascimento [DD]: '))
    data_nascimento = datetime.datetime(ano, mes, dia)

    return data_nascimento

def calculo_data(data_original, data_agora):
    data1 = data_agora
    data2 = datetime.datetime(data_agora.year, data_original.month, data_original.day)
    data_final = data1 - data2
    days = int(data_final.total_seconds() / 60 / 60 / 24)

    return days

def main():
    data_original = minha_data()
    data_agora = datetime.datetime.now()
    data_agora.year
    x = calculo_data(data_original, data_agora)
    print(x)

main()


