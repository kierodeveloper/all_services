from flask_script import Manager
from routes.router import app
from config.globals_service_RUN import service_run
import os
import configparser
config = configparser.ConfigParser()
config.read('.conf')
configurate = config['ENVIRONMENT']
HOST = str(configurate.get('SERVER'))
PORT = configurate['PORT']

manager = Manager(app)

@manager.command
def run():
    """INICIAR SERVIDOR"""
    service_run.run()

if __name__ == '__main__': 
    #manager.run()
    app.run(host=HOST,port=PORT)