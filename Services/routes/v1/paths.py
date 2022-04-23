
#Librerias basicas 
from flask import request, Blueprint
from http import HTTPStatus

#Vamos a especificar headers
from configuration.setup import headers

#Traemos nuestros ejercicios
from Services.routes.v1.ejercicio import procesos


#Creamos nuestra variable que llevara nuestros paths
v1 = Blueprint("version1", "version1", url_prefix="/v1")

#Inicio de creacion de paths --- GET
@v1.route('/ejercicio', methods=['GET','OPTIONS'])
def ejercicio():
    #Indicamos el nombre de la variable
    id_inicia=request.args.get('id_inicia')
    id_termina=request.args.get('id_termina')
    
    if request.method == 'OPTIONS':
        return ('', HTTPStatus.NO_CONTENT)

    if request.method == 'GET':
        response,http_code = procesos.get_paginated_list(procesos.llama_lista(), id_inicia,id_termina)
        
    http_code= HTTPStatus.OK   
    return (response, http_code,headers)