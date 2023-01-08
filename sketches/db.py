from pprint import pprint
from tinydb import TinyDB


db = TinyDB('db.json')
# field_name = 'value'
# value = 2
# db.update({field_name: value}, doc_ids=[1])
pprint(db.all())
