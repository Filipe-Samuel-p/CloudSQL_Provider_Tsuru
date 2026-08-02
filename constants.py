from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class _EnvVars(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    google_credential_cloudsql: str = Field(
        default='', alias='GOOGLE_CREDENTIAL_CLOUDSQL'
    )
    google_project_id: str = Field(alias='PROJECT_ID')

_env_vars = _EnvVars(_env_file='.env', _env_file_encoding='utf-8')

class GCloud:
    google_credential_cloudsql = _env_vars.google_credential_cloudsql
    google_project_id = _env_vars.google_project_id