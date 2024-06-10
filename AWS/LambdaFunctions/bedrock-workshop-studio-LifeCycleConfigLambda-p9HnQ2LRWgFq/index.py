import boto3
import base64
import cfnresponse

client = boto3.client('sagemaker')
lcc_up1 = '\n'.join((
    '#!/bin/bash',
    '',
    'set -ex',
    '',
    'if [ ! -z "${SM_JOB_DEF_VERSION}" ]',
    'then',
    '   echo "Running in job mode, skip lcc"',
    'else',
    '   git clone https://github.com/aws-samples/amazon-bedrock-workshop',
    '   echo "Repo cloned from git"',
    'fi',
    '',
))

lcc_name_up1 = "bedrock-workshop-studio-copy-notebooks"
up1 = "sagemakeruser|d-eckam841ymxg"

def get_lcc_base64_string(lcc_string):
    lcc_bytes = lcc_string.encode("ascii")
    base64_lcc_bytes = base64.b64encode(lcc_bytes)
    base64_lcc_string = base64_lcc_bytes.decode("ascii")
    return base64_lcc_string


def apply_lcc_to_user_profile(base64_lcc_string, lcc_config_name, profile):
    response = client.create_studio_lifecycle_config(
        StudioLifecycleConfigName=lcc_config_name,
        StudioLifecycleConfigContent=base64_lcc_string,
        StudioLifecycleConfigAppType="JupyterServer",
   )

    lcc_arn = response["StudioLifecycleConfigArn"]
    update_up = client.update_user_profile(
        DomainId=profile.split("|")[1],
        UserProfileName=profile.split("|")[0],
        UserSettings={
            "JupyterServerAppSettings": {
                "DefaultResourceSpec": {"LifecycleConfigArn": lcc_arn},
                "LifecycleConfigArns": [lcc_arn]
            }
        }
    )
    return update_up


def lambda_handler(event, context):
    print(event)
    try:
        base64_lcc_up1_string = get_lcc_base64_string(lcc_up1)
        updated_up1 = apply_lcc_to_user_profile(
            base64_lcc_up1_string,
            lcc_name_up1,
            up1
        )
        print("Response User Profile LCC update for UP1")
        print(updated_up1)

        response_value = 120
        response_data = {"Data": response_value}
        cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
    except Exception as e:
        if "RequestType" in event:
            if event["RequestType"] == "Delete":
                try:
                    response1 = client.delete_studio_lifecycle_config(
                        StudioLifecycleConfigName=lcc_name_up1
                    )
                    print(response1)
                    response_data = {}
                    cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
                    return
                except Exception as e2:
                    print(e2)
                    response_data = e2
                    cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
                    return
        print(e)
        response_data = {"Data": str(e)}
        cfnresponse.send(event, context, cfnresponse.FAILED, response_data)