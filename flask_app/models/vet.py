from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import re, flash
from pprint import pprint

DATABASE = 'vet_helping_vets'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Vet:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.branch = data['branch']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO vets (first_name, last_name, branch, email, password) VALUES ( %(first_name)s, %(last_name)s, %(branch)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

        ## ! used in vet validation
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM vets WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        # Didn't find a matching vet
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_vet_with_things(cls, data:dict):
        query = "SELECT * FROM vets LEFT JOIN things ON vets.id = things.vet_id WHERE vets.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        pprint(results)
        vet = cls(results[0])
        for result in results:
            thing_dict = {
                'id': result['things.id'],
                'column1': result['column1'],
                'column2': result['column2'],
                'column3': result['column3'],
                'column4': result['column4'],
                'column5': result['column5'],
                'column6': result['column6'],
                'vet_id': result['vet_id'],
                'created_at': result['things.created_at'],
                'updated_at': result['things.updated_at']
            }
            vet.things.append(vet(thing_dict))
        return vet

    @staticmethod
    def validate_vet(vet:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(vet['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(vet['last_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if vet['branch'] == '':
            flash("must select Branch")
            is_valid = False
        if not EMAIL_REGEX.match(vet['email']): 
            flash("Invalid email address!")
            is_valid = False
        if vet['password'] != vet['confirm-password']:
            flash("Passwords do not match")
            is_valid = False
        if len(vet['password']) < 8:
            flash("Password must be at least 8 character long.")
            is_valid = False
        return is_valid