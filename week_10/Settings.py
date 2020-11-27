def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        pass
        # the value was not an int let's try float
    try:
        return float(value)
    except ValueError:
        return value
        # the value was not a float we'll leave it as a string


class Settings:

    def __init__(self, setting_names=None, settings_file="settings.txt"):
        if setting_names is None:
            setting_names = []
        self.settings_file = settings_file
        self.settings = {}

        # read the settings file
        try:
            with open(self.settings_file) as saved_settings:
                for line in saved_settings.read().splitlines():
                    name, value = line.split(" = ")
                    self.settings[name] = safe_convert(value)
        except FileNotFoundError:
            # the file doesn't exist (yet)
            pass

        # check if settings are available for all named settings
        for name in setting_names:
            self.get(name)

    def get(self, name, default=None):
        if name not in self.settings and default is not None:
            self.settings[name] = default
            self.save(name)
        elif name not in self.settings:
            user_input = input("What should be the value for " + str(name) + "? ")
            self.settings[name] = safe_convert(user_input)
            self.save(name)

        return self.settings[name]

    def save(self, name=None):
        line_format = "{} = {}\n"
        if name is None:
            with open(self.settings_file, "w+") as saved_settings:
                for name, value in self.settings.items():
                    saved_settings.write(line_format.format(name, value))
        else:
            with open(self.settings_file, "a+") as saved_settings:
                saved_settings.write(line_format.format(name, self.settings[name]))
