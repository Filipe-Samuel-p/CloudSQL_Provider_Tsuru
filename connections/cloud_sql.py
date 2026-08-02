from google.oauth2 import service_account
from constants import GCloud
from google.cloud.sql.connector import Connector
from googleapiclient.discovery import build

                                

credential = service_account.Credentials.from_service_account_file(GCloud.google_credential_cloudsql)

def cloudsql_admin_client():
    client = build('sqladmin','v1', credentials=credential)
    return client

def cloudsql_data_connector():
    conn = Connector(credentials=credential)
    return conn