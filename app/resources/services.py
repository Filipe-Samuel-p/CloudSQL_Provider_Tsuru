from .schemas import InstanceRequest, InstanceResponse
from connections.cloud_sql import cloudsql_admin_client
from constants import GCloud

cloudsql_admin = cloudsql_admin_client()

def new_instance(data: InstanceRequest):
    try:

        database_instance = {
            "name": data.instance_name,
            "region": data.region,
            "databaseVersion":"MYSQL_8_0",
            "settings":{
                "tier": data.plan,
                "dataDiskSizeGb": "10",
                "dataDiskType": "PD_HDD",      
                "storageAutoResize": False,
                "availabilityType": "ZONAL",
                "ipConfiguration": {
                    "ipv4Enabled": True
                }
            }
        }

        request = cloudsql_admin.instances().insert(project=GCloud.google_project_id,body=database_instance)
        response = request.execute()

        return InstanceResponse(**response)
    
    except Exception as e:
        raise Exception(e)


def get_instance(instance_id:str):
    try:

        request = cloudsql_admin.instances().get(
            project=GCloud.google_project_id,
            instance=instance_id)
        response = request.execute()

        return response

    except Exception as e:
        raise Exception(e)
    

def delete_instance(instance_id:str):
    try:

        request = cloudsql_admin.instances().delete(
            project=GCloud.google_project_id,
            instance=instance_id)
        response = request.execute()

        return InstanceResponse(**response)

    except Exception as e:
        raise Exception(e)