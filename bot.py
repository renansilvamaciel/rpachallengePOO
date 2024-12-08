
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from rpachallenge import RpaChallenge
import pandas as pd


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    try:

        bot = RpaChallenge()



        #########################
        # PASSO 1: ABRIR O SITE #
        #########################

        # abrimos o site do RPA Challenge
        bot.login()

        bot.escolher_desafio()

        #################################################
        # PASSO 2 :FAZER O DOWNLOAD DO CSV COM OS DADOS #
        #################################################
        file_path = bot.baixar_csv_input_forms()

        # ler a planilha com os dados em CSV,  exporta para um Dataframe
        employees = pd.read_excel(file_path)


        ###############################
        # PASSO 4: PREENCHER OS DADOS #
        ###############################
        try:
            for employee in employees:
                ...

        except Exception as valeueError:
            print(valeueError)

        # PASSO 5 FINALIZAR
    except Exception as errors:
        print(errors)


if __name__ == '__main__':
    main()
