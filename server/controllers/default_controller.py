import sys

from controllers.irods_session import create_session
from configparser import ConfigParser
from irods.models import Collection, DataObject, Resource, ResourceMeta
from irods.column import Criterion
from irods.exception import CollectionDoesNotExist, DataObjectDoesNotExist
from flask import jsonify

parser = ConfigParser()
parser.read('ini/connexion.ini')

sys.path.append(parser.get('sys-path', 'controllers'))


def get_host_node_get(resource_name) -> str:
    sess = create_session()
    conditions = [
        Resource.name == resource_name
    ]
    results = sess.query(Resource.name, Resource.location).filter(*conditions).all()
    sess.cleanup()
    data = {}
    data['hostnode'] = []
    for r in results.rows:
        r_loc = r.popitem()
        r_name = r.popitem()
        # print(r_name[1] + ':' + r_loc[1])
        data['hostnode'] += {str(r_loc[1])}

    return jsonify(data)


def find_resources_by_metadata(meta_key=None, meta_value=None) -> str:
    session = create_session()
    conditions = []
    if meta_key:
        conditions += [ResourceMeta.name == meta_key]
    if meta_value:
        conditions += [ResourceMeta.value == meta_value]
    res = session.query(Resource.name,
                        ResourceMeta.name,
                        ResourceMeta.value).filter(*conditions).all()
    session.cleanup()
    return jsonify(list(set([r[Resource.name] for r in res.rows])))


def get_resource_metadata(resource_name) -> str:
    sess = create_session()
    conditions = [
        Resource.name == resource_name
    ]
    res = sess.query(Resource.name,
                     Resource.location,
                     ResourceMeta.name,
                     ResourceMeta.value).filter(*conditions).all()
    sess.cleanup()
    if not res.rows:
        return jsonify(dict(error='Resource not found: %s'%resource_name)), 404
    resp = {r[ResourceMeta.name]: r[ResourceMeta.value] for r in res.rows}
    resp.update(name=res.rows[0][Resource.name],
                host=res.rows[0][Resource.location])
    return jsonify(resp)


def get_host_site_get(resource_name) -> str:
    # TODO
    data = {
        'site': {
            'perfsonar_node': 'string',
            'sitename': resource_name,
            'TODO': 'Not implemented at this time'
        }
    }

    return jsonify(data)


def get_logical_location_get(filename, match_exact = None, include_trash = None) -> str:
    max_rows = 1000
    offset = 0
    sess = create_session()
    conditions = []
    if match_exact:
        conditions += [DataObject.name == str(filename)]
    else:
        conditions += [Criterion('like', DataObject.name, '%' + str(filename) + '%')]
    if not include_trash:
        conditions += [Criterion('not like', Collection.name, '%/trash/%')]
    results = sess.query(DataObject.name,
                            Collection.name).\
        filter(*conditions).\
        offset(offset).\
        limit(max_rows).all()
    sess.cleanup()
    data = {}
    data['irods_filenames'] = []
    for r in results.rows:
        l_path = r.popitem()
        f_name = r.popitem()
        data['irods_filenames'] += {str(l_path[1]) + '/' + str(f_name[1])}

    return jsonify(data)


def get_data_object(filename) -> str:
    try:
        sess = create_session()
        obj = sess.data_objects.get(filename)
        sess.cleanup()
        data = dict(path=filename, type=obj.type, size=obj.size)
        for replica in obj.replicas:
            data.setdefault('replicas', []).append({
                'resource_name': str(replica.resource_name),
                'number': int(replica.number),
                'path': str(replica.path),
                'status': int(replica.status)
            })
    except (CollectionDoesNotExist, DataObjectDoesNotExist):
        return jsonify(dict(error="Data object '%s' is not found"%filename)), 404
    return jsonify(data)


def get_data_objects(filenames) -> list:
    sess = create_session()
    data_objs = []
    for fn in filenames:
        try:
            data_objs += sess.data_objects.get(fn),
        except (CollectionDoesNotExist, DataObjectDoesNotExist):
            print('%s is not found'%fn)
    sess.cleanup()
    data = []
    for o in data_objs:
        data_obj = dict(path=o.path, type=o.type, size=o.size)
        for rep in o.replicas:
            data_obj.setdefault('replicas', []).append(dict(
                resource_name=str(rep.resource_name),
                number=int(rep.number),
                path=str(rep.path),
                status=int(rep.status)))
        data += data_obj,
    return jsonify(data)
