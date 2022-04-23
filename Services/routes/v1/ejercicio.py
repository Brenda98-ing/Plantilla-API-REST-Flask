
#Standar library
import json
from http import HTTPStatus

class procesos:
    
    #Se crea lista llena referencia id
    def llama_lista():
       data = [{'employee_id': i+1} for i in range(10)]
       return data

    #Vamos a mandar el json, cuando empieza , y hasta donde termina
    def get_paginated_list(data, start, limit):
   
       start = int(start)
       #2
       limit = int(limit)
       #5
       count = len(data)

       #validamos que no esten vacias nuestras variables
       if count < start or limit < 0:
           print("404 ALGO ANDA MAL")
    
    
       # Armamos el reponse como primeros campos los datos:
       obj = {}
       obj['start'] = start
       obj['limit'] = limit
       obj['count'] = count

       # finally extract result according to bounds
       obj['results'] = data[(start - 1):(start - 1 + limit)]
       #Convertimos muestra lista en JSON
       obj=json.dumps(obj)

       http_code= HTTPStatus.OK 
       return obj,http_code                           






