from fastapi.security import HTTPBasic,HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from typing import Annotated
from constants import Credenditals
import secrets


security = HTTPBasic()

def get_current_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    tsuru_username = Credenditals.tsuru_username
    tsuru_password = Credenditals.tsuru_password

    current_username = credentials.username.encode("utf8")
    correct_username_credential= tsuru_username.encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username, correct_username_credential
    )

    current_password = credentials.password.encode("utf8")
    correct_password_credential = tsuru_password.encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password, correct_password_credential
    )

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="username or password: error",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username