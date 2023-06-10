from marshmallow import Schema, fields


class RunnersSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    half_marathon = fields.Str(required=True)
    marathon = fields.Str(required=True)
