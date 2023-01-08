from tinydb import TinyDB


db = TinyDB('../db.json')
db.insert(
        {
            "name": "Form template name",
            "field_name_1": "email",
            "field_name_2": "phone"
        }
)
# db.insert({})
