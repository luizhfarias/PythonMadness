from google.oauth2 import service_account

# Carrega o arquivo de credenciais
credentials = service_account.Credentials.from_service_account_file("cred_agenda_serv.json")

from googleapiclient.discovery import build

# Cria o cliente da API do Google Sheets
service = build('sheets', 'v4', credentials=credentials)

# Obtém a lista de planilhas disponíveis na conta
#result = service.spreadsheets().get().execute()
#sheets = result.get('sheets', [])

# Especifica o ID da planilha e o nome da aba
spreadsheet_id = '1ZV1Sncwl_9rdZqFTVfvteYyocjz5kaVeQhA--pjfzD8'
sheet_name = 'Homolog Disparos'
# Especifica o intervalo de células a serem lidas (notação A1)
range_name = 'Comunicados!A1:D10'

# Obtém os dados da planilha
result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

# Converte os dados em uma lista de listas
vResultado = result.get('values', [])

# Converte a lista de listas em um DataFrame do Pandas
import pandas as pd
df = pd.DataFrame(vResultado[1:], columns=vResultado[0])

print(df)

