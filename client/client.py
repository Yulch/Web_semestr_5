import requests
#r = requests.get('http://127.0.0.1:5000/users')
#print(r.json())
#r = requests.post('http://127.0.0.1:5000/users', json={'name': "Dilan", 'surname': "Nolan"})
#print(r.json())
#r = requests.delete('http://127.0.0.1:5000/users', json={'id': 6})

r = requests.put('http://127.0.0.1:5000/users', json={'id': 6, 'name': 'Chris', 'surname': 'Ouen' })
print(r.json())
#r = requests.get('http://127.0.0.1:5000/users')
