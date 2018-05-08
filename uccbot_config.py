import json

from uccbot.config_values import ConfigValues


def read_config_file(file_name):
    with open(file_name) as config_file:
        data = json.load(config_file)

    values = ConfigValues(data["join_message"],
                          data["general_channel_name"],
                          data["discord_token"])
    return values
