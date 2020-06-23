from marshmallow import Schema, fields

class BookSchema(Schema):
    # id = fields.Int(required=True)
    # name = fields.Str(required=True)
    # author = fields.Str(required=True)
    # status = fields.Str(required=True) 

class UserSchema(Schema):
    # id = fields.Int(required=True)
    # name = fields.Str(required=True)
    # gender = fields.Int(required=True)
    # status = fields.Str(required=True) 

class CommandResultSchema(Schema):
    # err = fields.Int(required=True)
    # msg = fields.Str(required=True)