from ibm_watson_machine_learning import APIClient
import json

space_id = input('Enter Space id : ')

f = open("key_file", "r")
obj=json.loads(f.read())
apikey=obj["apikey"]

with open(".env", "a") as f:
    f.write("\n#Api key\nAPI_Key=\""+apikey+"\"\n")
    f.write("\n#Space id\nSpace_ID=\""+space_id+"\"\n")

wml_credentials = {
  "apikey": apikey,
  "url": "https://us-south.ml.cloud.ibm.com"
}
client = APIClient(wml_credentials)

MODEL_NAME = "Personal Loan Prediction model"
DEPLOYMENT_SPACE_NAME = "LoanApprovalNew"

client.spaces.list()
all_spaces = client.spaces.get_details()['resources']
space_id = None
for space in all_spaces:
    if space['entity']['name'] == DEPLOYMENT_SPACE_NAME:
        space_id = space["metadata"]["id"]
        print("\nDeployment Space GUID: ", space_id)

if space_id is None:
    print("WARNING: Your space does not exist. Create a deployment space before proceeding to the next cell.")

client.set.default_space(space_id)

deploy_meta = {
     client.deployments.ConfigurationMetaNames.NAME: 'Deployment of '+ MODEL_NAME,
     client.deployments.ConfigurationMetaNames.ONLINE: {}
}
published_model_id="<YOUR_MODEL_ID>"
created_deployment = client.deployments.create(published_model_id, meta_props=deploy_meta)
scoring_endpoint = client.deployments.get_scoring_href(created_deployment)
print('MODEL_URL :' + scoring_endpoint + '?version=2021-12-07')
