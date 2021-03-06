import json


class Spell(object):

    name = None
    school = None
    subschool = None
    descriptors = []
    levels = None
    action = None
    components = []
    range = None
    effect = None
    duration = None
    saving_throw = None
    spell_resistance = None
    description = None
    source_book = None
    url = None

    def __init__(self):
        return

    def to_string(self):
        return self.__dict__

    def json(self):
        return json.dumps(self.__dict__)
