from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    email = fields.Email(required=True)
    name = fields.Str(required=True)
    mobile = fields.Str(required=True)

    @validates('mobile')
    def validate_mobile(self, value):
        if len(value) < 10:  # Example: Validate mobile length
            raise ValidationError('Mobile number must be at least 10 digits.')

class ExpenseSchema(Schema):
    amount = fields.Float(required=True)
    split_method = fields.Str(required=True, validate=lambda x: x in ['equal', 'exact', 'percentage'])
    user_id = fields.Int(required=True)
    participants = fields.List(fields.Int(), required=False)
    exact_splits = fields.Dict(keys=fields.Str(), values=fields.Float(), required=False)
    percentage_splits = fields.Dict(keys=fields.Str(), values=fields.Float(), required=False)
    description = fields.Str(required=False)

    @validates('split_method')
    def validate_split_method(self, value):
        if value not in ['equal', 'exact', 'percentage']:
            raise ValidationError('Invalid split method.')

    @validates('percentage_splits')
    def validate_percentage(self, value):
        if sum(value.values()) != 100:
            raise ValidationError('Percentages must add up to 100.')

    @validates('exact_splits')
    def validate_exact_splits(self, value):
        # Use self.context to get the amount
        amount = self.context.get('amount')
        if amount is None:
            raise ValidationError('Amount is required in context.')
        if sum(value.values()) != amount:
            raise ValidationError('Exact splits must sum up to the amount.')
