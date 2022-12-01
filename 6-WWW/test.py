# Author = Dennis Turco

import http.client

# apro la connessione
conn = http.client.HTTPSConnection("localhost:80")
conn.request("GET", "/")

# stampo informazioni sulla connessione
response = conn.getresponse()
print (f"Server status: {response.status} \treason: {response.reason}")

# ottengo e stampo in risultato della richiesta
data = response.read()
print(data)

# chiudo la connessione
conn.close()