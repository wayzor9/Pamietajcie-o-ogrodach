from marshmallow import Schema, fields, validate, EXCLUDE


class SpecificationsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    growth_habit = fields.Str()
    growth_rate = fields.Str(allow_none=True)
    toxicity = fields.Str(
        validate=validate.OneOf(["low", "medium", "high", "none"]), allow_none=True
    )
    average_height = fields.Dict(keys=fields.Str(), values=fields.Int(allow_none=True))
    maximum_height = fields.Dict(keys=fields.Str(), values=fields.Int(allow_none=True))


class GrowthSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    description = fields.Str(allow_none=True)
    sowing = fields.Str(allow_none=True)
    ph_minimum = fields.Float(validate=validate.Range(min=0, max=14), allow_none=True)
    ph_maximum = fields.Float(validate=validate.Range(min=0, max=14), allow_none=True)
    light = fields.Int(validate=validate.Range(min=0, max=10), allow_none=True)
    atmospheric_humidity = fields.Int(
        validate=validate.Range(min=0, max=10), allow_none=True
    )
    growth_months = fields.Str(allow_none=True)
    bloom_months = fields.Str(allow_none=True)
    fruit_months = fields.Str(allow_none=True)
    minimum_precipitation = fields.Dict(
        keys=fields.Str(), values=fields.Int(allow_none=True)
    )
    maximum_precipitation = fields.Dict(
        keys=fields.Str(), values=fields.Int(allow_none=True)
    )
    minimum_temperature = fields.Dict(
        keys=fields.Str(), values=fields.Int(allow_none=True)
    )
    soil_nutriments = fields.Int(
        validate=validate.Range(min=0, max=10), allow_none=True
    )
    soil_salinity = fields.Int(validate=validate.Range(min=0, max=10), allow_none=True)
    soil_texture = fields.Int(validate=validate.Range(min=0, max=10), allow_none=True)
    soil_humidity = fields.Int(validate=validate.Range(min=0, max=10), allow_none=True)


class MainSpeciesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    duration = fields.List(fields.Str(), allow_none=True)
    growth = fields.Nested(GrowthSchema)
    specifications = fields.Nested(SpecificationsSchema)


class DataSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    main_species = fields.Nested(MainSpeciesSchema)


class FinalSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    data = fields.Nested(DataSchema, allow_none=True)

"""
load output:
{'data': {'main_species': {'duration': None,
                           'growth': {'atmospheric_humidity': None,
                                      'bloom_months': None,
                                      'fruit_months': None,
                                      'growth_months': None,
                                      'light': None,
                                      'maximum_precipitation': {'mm': 1270},
                                      'minimum_precipitation': {'mm': 812},
                                      'minimum_temperature': {'deg_c': -35,
                                                              'deg_f': -31},
                                      'ph_maximum': 7.5,
                                      'ph_minimum': 4.7,
                                      'soil_humidity': None,
                                      'soil_nutriments': None,
                                      'soil_salinity': None,
                                      'soil_texture': None,
                                      'sowing': None},
                           'specifications': {'average_height': {'cm': None},
                                              'growth_habit': 'Shrub',
                                              'growth_rate': 'Moderate',
                                              'maximum_height': {'cm': None},
                                              'toxicity': 'none'}}}}
"""

