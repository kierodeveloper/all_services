from flask_script import Manager
from routes.router import app
from config.globals_service_RUN import service_run
import os
from flask_mail import Mail, Message

import configparser
from flask_jwt_extended import JWTManager


config = configparser.ConfigParser()
config.read('.conf')
configurate = config['ENVIRONMENT']
HOST = str(configurate.get('SERVER'))
PORT = configurate['PORT']

manager = Manager(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'contacto@kiero.co',
    "MAIL_PASSWORD": 'qwpoeri1452a!a'
}
app.config.update(mail_settings)
mail = Mail(app)
app.config['JWT_SECRET_KEY'] = '7(Jc=X=4&ex"P9[b'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@manager.command
def run():
    """INICIAR SERVIDOR"""
    service_run.run()

if __name__ == '__main__': 
    #manager.run()
    app.run(host='10.4.28.90',port=6549) 