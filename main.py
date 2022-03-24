import os, time, requests
from fake_useragent import UserAgent

URL = 'https://app.sli.do/eu1/api/v0.5/events'

ua = UserAgent()
user_agent = ua.chrome

def get_uuid(event_id):
  return requests.get(URL, params={'hash': event_id}, headers={'User-Agent': user_agent}).json()[-1]['uuid']

def get_access_token(uuid):
  return requests.post(f'{URL}/{uuid}/auth', headers={'User-Agent': user_agent}).json()['access_token']

def vote(uuid, question_id):
  headers = {
    'Authorization': f'Bearer {get_access_token(uuid)}',
    'User-Agent': user_agent
  }

  time.sleep(2) # prevent detection
  return requests.post(f'{URL}/{uuid}/questions/{question_id}/like', json={'score': 1}, headers=headers)

def automate():
  global user_agent
  event_id, question_id, count = os.environ.get('EVENT'), os.environ.get('QUESTION'), os.environ.get('COUNT')
  print('=> getting uuid')
  uuid = get_uuid(event_id)
  for i in range(int(count)):
    print(f'- processing vote {i+1}')
    vote(uuid, question_id)
    user_agent = ua.chrome

  print('=> DONE')
  
automate()

# EVENT=bumesua62hpssnDHNiaSSK QUESTION=50523266 COUNT=30 python3 main.py