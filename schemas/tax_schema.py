from marshmallow import Schema, fields, validate

class TaxCalculationInputSchema(Schema):
    salary = fields.Float(required=True, validate=validate.Range(min=0))
    tax_year = fields.Integer(required=True, validate=validate.OneOf([2019, 2020, 2021, 2022]))

class TaxBreakdownSchema(Schema):
    min = fields.Float(required=True)
    max = fields.Float(allow_none=True)  # max might be omitted (infinity)
    rate = fields.Float(required=True)
    tax = fields.Float(required=True)

class TaxCalculationOutputSchema(Schema):
    total_tax = fields.Float(required=True)
    effective_rate = fields.Float(required=True)
    tax_breakdown = fields.List(fields.Nested(TaxBreakdownSchema), required=True)
