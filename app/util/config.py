from pathlib import Path
from typing import Union, Dict
from json import load

class Configuration:
    def __init__(self, config_path: Union[str, Path]):
        # Wrap it
        self.config_path = Path(config_path)
        self.json_data = dict()

        # Keys for consistency; they're gonna be used more than once
        self.discord_key = "discord"
        self.bindbot_key = "BindBot"
        self.name_key = "name"
        self.version_key = "version"
        self.token_key = "token"

        # Do that checking
        if self.config_path.exists():
            # Make sure path exists, of course
            secrets_fp = self.config_path.open("r")
            self.json_data = load(secrets_fp)
            secrets_fp.close()

            # Base fields error checking
            if self.discord_key not in self.json_data:
                raise Exception(f"No '{self.discord_key}' key in {str(self.config_path)}")
            elif self.bindbot_key not in self.json_data[self.discord_key]:
                raise Exception(f"No '{self.bindbot_key}' key in {str(self.config_path)}")

    @property
    def name(self):
        if self.name_key not in self.json_data[self.discord_key][self.bindbot_key]:
            raise Exception(f"No '{self.name_key}' key in {str(self.config_path)}")
        else:
            return self.json_data[self.discord_key][self.bindbot_key][self.name_key]

    @property
    def version(self):
        if self.version_key not in self.json_data[self.discord_key][self.bindbot_key]:
            raise Exception(f"No '{self.version_key}' key in {str(self.config_path)}")
        else:
            return self.json_data[self.discord_key][self.bindbot_key][self.version_key]

    @property
    def token(self):
        if self.token_key not in self.json_data[self.discord_key][self.bindbot_key]:
            raise Exception(f"No '{self.token_key}' key in {str(self.config_path)}")
        else:
            return self.json_data[self.discord_key][self.bindbot_key][self.token_key]
