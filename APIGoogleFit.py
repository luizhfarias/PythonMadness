from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("cred_agenda_serv.json")

# Configuração da autenticação
creds = Credentials.from_authorized_user_file('cred_google_fit.json', ['https://www.googleapis.com/auth/fitness.heart_rate.read'])

# Configuração do serviço de histórico de batimentos cardíacos
service = build('fitness', 'v1', credentials=credentials)
data_source = 'derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm'

# Definição do intervalo de tempo para a busca dos dados
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=7)

# Busca dos dados de batimentos cardíacos
try:
    request = service.users().dataSources().datasets(). \
        get(userId='me', dataSourceId=data_source,
            startTime=start_time.isoformat()+'Z', endTime=end_time.isoformat()+'Z')
    response = request.execute()
    print(response)
except HttpError as error:
    print('Erro na solicitação:', error.content)