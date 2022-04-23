__author__ = "Brenda Medina Arroyo"
__copyright__ = "Plantilla Básica 2022"
__version__ = "1.0.1"
__maintainer__ = "Brenda Medina"
__email__ = "***"
__status__ = "dev"

#Flask
from flask import Flask
from flask_cors import CORS

# standard library
from datetime import datetime
import pytz
import os

#De servicios trae los paths en la variable v
from Services.routes.v1.paths import v1

# flask app
app = Flask(__name__)
CORS(app)

# register blueprint con versiones
app.register_blueprint(v1, url_prefix="/v1")

# Este apartado toma puerto de PC
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    utc_now = datetime.utcnow()
    utc_now = utc_now.astimezone(pytz.timezone('America/Mexico_City'))
    print(utc_now)
    app.run(threaded=True, host='0.0.0.0', port=port)


    