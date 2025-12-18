import yaml

def load_config() -> dict[str, dict[str, str]]:
    with open("config.yaml") as stream:
        try:
            config: dict[str, dict[str, str]] = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return default_config()
    return config

def default_config() -> dict[str, dict[str, str]]:
    return {'paths': 
        {'login_data': 'login/',
         'login_data_filename': 'logins.db',
         'question_data': 'info/quiz_questions.csv',
         'winner_data': 'info/games.csv'}
    }