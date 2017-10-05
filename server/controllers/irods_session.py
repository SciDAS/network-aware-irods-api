from irods.session import iRODSSession
from configparser import ConfigParser


def create_session(**kwargs):
    parser = ConfigParser()
    parser.read('ini/connexion.ini')
    session = iRODSSession(host=parser.get('irods', 'host'),
                           port=parser.get('irods', 'port'),
                           user=parser.get('irods', 'user'),
                           password=parser.get('irods', 'password'),
                           zone=parser.get('irods', 'zone'))
    return session
