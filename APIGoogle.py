from google.oauth2 import service_account

from PythonMadness.teste01 import imprimir_mensagem
from PythonMadness.QuickStartGoogle import fEventosAgenda

credentials = service_account.Credentials.from_service_account_file("cred_agenda_serv.json")

from googleapiclient.discovery import build

# Crie um objeto cliente para a API do Google Agenda
service = build('calendar', 'v3', credentials=credentials)

from datetime import datetime, timedelta

# Define o intervalo de datas para buscar eventos
now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indica UTC time
one_day_later = (datetime.utcnow() + timedelta(days=1)).isoformat() + 'Z'

# Chama a API para buscar eventos
events_result = service.events().list(
    calendarId='primary', timeMin=now, timeMax=one_day_later,
    maxResults=1000, singleEvents=True,
    orderBy='startTime').execute()

events = events_result.get('items', [])

if not events:
    print('Sem eventos agendados')
else:
    print('Events:')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

from datetime import datetime, timedelta
from pytz import timezone

# Define o intervalo de datas para buscar eventos
timezone = timezone('America/Sao_Paulo')
now = datetime.now(timezone).isoformat()
one_day_later = (datetime.now(timezone) + timedelta(days=100)).isoformat()

# Chama a API para buscar eventos
IDcalendario = 'aGVucmljay5mYXJpYXNAZ21haWwuY29t'
events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=one_day_later, singleEvents=True, orderBy='startTime').execute()

events = events_result.get('items', [])

if not events:
    print('Não foram encontrados eventos')
else:
    print('Events:')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_time = datetime.fromisoformat(start).strftime('%Y-%m-%d %H:%M:%S')
        print(start_time, event['summary'])
print(now, one_day_later)

imprimir_mensagem()
fEventosAgenda()
