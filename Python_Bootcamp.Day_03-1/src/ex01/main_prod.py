import redis
import logging
import json
import requests

logging.warning('Watch out!')
data = {
    "metadata": {
        "from": 1023461745,
        "to": 5738456434
    },
    "amount": 10000
}
data = (2, 'd')
json_form = json.dumps(data)
print(type(json_form))
python_form = json.loads(json_form)
print(type(python_form))
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)

'''r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('test', 'ok')
print(r.get('test'))
for i in range(100):
    data = input()
    r.set(data, i)
    r.publish("ch1", data)'''
