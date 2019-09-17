"""Servicios basicos de la app"""

import configparser
import os
import logging
import logging.handlers
import psutil
from waitress import serve
from paste.translogger import TransLogger
from routes.router import app

class service_run():
    """Servicios basicos de la app"""
    def run():
        """Funcion encargada de correr el servicio con Waitress"""
        config = configparser.ConfigParser()
        config.read('.conf') 
        configurate = config['ENVIRONMENT']
        os.system('cls')
        logger = logging.getLogger('waitress') 

        formato = ('%(REMOTE_ADDR)s,[%(time)s],''%(REQUEST_METHOD)s,%(REQUEST_URI)s,%(HTTP_VERSION)s,''%(status)s,%(bytes)s,%(HTTP_REFERER)s,%(HTTP_USER_AGENT)s')

        

        fh = logging.handlers.RotatingFileHandler('./storage/logs/log.csv', maxBytes= config['LOGS'].getint('maxBytes') , backupCount=config['LOGS'].getint('backupCount'))
        logger.addHandler(fh)
        logger.setLevel(logging.DEBUG)
        HOST = configurate['server']
        PORT = configurate['port']
        pid = os.getpid()
        py = psutil.Process(pid)
        memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
        print('memory use:', memoryUse)
        serve(TransLogger(app,setup_console_handler=True,logger=logger,format=formato) ,host=HOST,port=PORT) 

        
