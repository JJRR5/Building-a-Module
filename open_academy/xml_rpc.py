import xmlrpc.client


url = 'http://localhost:8069'
db = 'rd-demo'
username = 'admin'
key = '07b07311581f6ce9655735db6ca7aca675df5b2f'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, key, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
session_fields = models.execute_kw(
    db, uid, key,
    'session',
    'search_read',
    [[['name', '!=', False]]],
    {'fields': ['name', 'number_of_seats']}
)
new_session = models.execute_kw(
    db, uid, key,
    'session',
    'create',
    [{'name': 'Session from xml_rpc', 'course_id': 1, 'duration': 5}]
)
