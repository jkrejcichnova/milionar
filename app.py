import yaml
def load_config():
    with open("config.yaml") as stream:
        try:
            config: dict[dict[str]] = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config
print(load_config()['paths']['login_data'])