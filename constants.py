from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class _EnvVars(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    google_project_id: str = Field(alias='PROJECT_ID')

    tsuru_username: str = Field(alias='TSURU_USERNAME')
    tsuru_password: str = Field(alias='TSURU_PASSWORD')

_env_vars = _EnvVars(_env_file='.env', _env_file_encoding='utf-8')

class Credenditals:
    tsuru_username = _env_vars.tsuru_username
    tsuru_password = _env_vars.tsuru_password

class GCloud:
    google_project_id = _env_vars.google_project_id