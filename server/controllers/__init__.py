from irods.session import iRODSSession
from configparser import ConfigParser

parser = ConfigParser()
parser.read('ini/connexion.ini')
Session = iRODSSession(host=parser.get('irods', 'host'),
                       port=parser.get('irods', 'port'),
                       user=parser.get('irods', 'user'),
                       password=parser.get('irods', 'password'),
                       zone=parser.get('irods', 'zone'))

