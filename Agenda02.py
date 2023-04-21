from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging
logging.basicConfig(filename='logApiAgenda.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
# Autenticação usando uma chave de API do Google
credentials = service_account.Credentials.from_service_account_file(
    'cred_agenda_serv.json')

# Criação do objeto da API do Google Calendar
service = build('calendar', 'v3', credentials=credentials)

# ID do evento que deseja buscar participantes
#event_id = '15hfv25rfnve660l9uov011m7c'
event_id = '0l3ssqbtbh75oii4b3scpo65ks'

# ID do calendário que deseja buscar eventos
calendar_id = 'henrick.farias@gmail.com'

# Parâmetros da chamada para buscar participantes
paramsParticipante = {
    'calendarId': calendar_id,
    'eventId': event_id,
    'fields': 'attendees'
}

# Faz a chamada GET para a API de eventos do Google Calendar
response = service.events().get(**paramsParticipante).execute()

# Exibe as informações sobre cada participante
attendees = response.get('attendees', [])
for attendee in attendees:
    name = attendee.get('displayName')
    email = attendee.get('email')
    phone = attendee.get('phone')
    if 'phone' in attendee.get('extendedProperties', {}).get('private', {}):
        phone = attendee['extendedProperties']['private']['phone']
    print(name, email, phone)
print('/--'*10)
resultados = [attendee.get('email', []) for attendee in attendees]
resultado_str = ", ".join(str(r) for r in resultados)
print('Resultado unificado em lista...')
print(resultado_str)
print('/--'*10)

print('Lista de eventos!')

# Parâmetros da chamada para buscar eventos
paramsEvento = {
    'calendarId': calendar_id,
   # 'eventId': event_id,
    'timeMin': '2023-03-26T00:00:00Z',
    'timeMax': '2024-03-27T00:00:00Z',
    'maxResults': 10,
    'singleEvents': True,
    'orderBy': 'startTime',
    'fields': 'items(id,summary,start,end)'
}
logging.info(paramsEvento)
# Faz a chamada GET para a API de eventos do Google Calendar
response = service.events().list(**paramsEvento).execute()

# Exibe as informações sobre cada evento retornado pela chamada
events = response.get('items', [])
for event in events:
    vEvendoID = event.get('id')
    evento = event.get('id'), event.get('summary'), event.get('start').get('dateTime'), event.get('end').get('dateTime')
    #organizador = event['organizer'].get('displayName', event['organizer'].get('email'))
    #print(evento)
    resultados = [attendee.get('email', []) for attendee in attendees]
    resultado_str = ", ".join(str(r) for r in resultados)
    if event.get('id') == event_id:
        print('Participantes: ', resultado_str)
        print('Evento: ', evento)
        print('IdEvento', vEvendoID)
    else:
        print('Evento: ', event.get('id'), event.get('summary'), event.get('start').get('dateTime'), event.get('end').get('dateTime'))
        print('IdEvento', vEvendoID)

logging.info(events)

print('Pronto...')

