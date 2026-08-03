import google.auth
from google.cloud.sql.connector import Connector
from googleapiclient.discovery import build


credential, _ = google.auth.default()

def cloudsql_admin_client():
    client = build('sqladmin','v1', credentials=credential)
    return client

def cloudsql_data_connector():
    conn = Connector(credentials=credential)
    return conn