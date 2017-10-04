import sys
from controllers import Session
from configparser import ConfigParser
from irods.models import Collection, DataObject, Resource
from irods.column import Criterion
from flask import jsonify

parser = ConfigParser()
parser.read('ini/connexion.ini')

sys.path.append(parser.get('sys-path', 'controllers'))


def get_host_node_get(resource_name) -> str:
    conditions = [
        Resource.name == resource_name
    ]
    results = Session.query(Resource.name,
                            Resource.location).\
        filter(*conditions).all()
    data = {}
    data['hostnode'] = []
    for r in results.rows:
        r_loc = r.popitem()
        r_name = r.popitem()
        # print(r_name[1] + ':' + r_loc[1])
        data['hostnode'] += {str(r_loc[1])}
    return jsonify(data)


def get_host_site_get(resourceName) -> str:
    # TODO
    data = {
        "site": {
            "perfsonar_node": "string",
            "sitename": "string"
        }
    }

    return jsonify(data)


def get_logical_location_get(filename, match_exact = None, include_trash = None) -> str:
    max_rows = 1000
    offset = 0
    conditions = []
    if match_exact:
        conditions += [DataObject.name == str(filename)]
    else:
        conditions += [Criterion('like', DataObject.name, '%' + str(filename) + '%')]
    if not include_trash:
        conditions += [Criterion('not like', Collection.name, '%/trash/%')]

    print(match_exact, include_trash)

    results = Session.query(DataObject.name,
                            Collection.name).\
        filter(*conditions).\
        offset(offset).\
        limit(max_rows).all()
    data = {}
    data['irods_filenames'] = []
    for r in results.rows:
        l_path = r.popitem()
        f_name = r.popitem()
        # print(l_path[1] + '/' + f_name[1])
        data['irods_filenames'] += {str(l_path[1]) + '/' + str(f_name[1])}

    return jsonify(data)


def get_replicas_get(filename) -> str:
    data = {}
    data['replicas'] = []
    obj = Session.data_objects.get(filename)
    for replica in obj.replicas:
        data['replicas'] += [{
            'resource_name': str(replica.resource_name),
            'number': int(replica.number),
            'path': str(replica.path),
            'status': int(replica.status)
        }]
    print(data)

    return jsonify(data)
