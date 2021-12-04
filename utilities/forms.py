class FieldsetsBuilder:
    def __init__(self):
        self.fieldsets = [[None, {}]]
        self.current_section = self.fieldsets[0][1]

    def section(self, section_name=None):
        section = next(fieldset for fieldset in self.fieldsets + [[section_name, {}]] if fieldset[0] == section_name)
        if section_name == section[0]:
            self.fieldsets.append(section)

        self.current_section = section[1]
        return self

    def fields(self, *args):
        # aggiunge fields in orizzontrale o verticale
        args = map(lambda x: tuple(x) if isinstance(x, list) else x, args)
        self.current_section.setdefault('fields', []).extend(args)
        return self

    def classes(self, *args):
        # aggiunge classi alla sezione
        self.current_section.setdefault('classes', args)
        return self

    def description(self, description):
        # aggiunge descrizione alla sezione
        self.current_section.setdefault('description', description)
        return self

    def build(self):
        if not self.fieldsets[0][1]:
            self.fieldsets.pop(0)
        return self.fieldsets
