import json

VOAPIID = os.environ['VOAPIID'] # GH Added Env Var
VOAPIKEY = os.environ['VOAPIKEY'] # GH Added Env Var
PHANTOMBASEURL = os.environ['PHANTOMBASEURL'] # GH Added Env Var


# VOheaders = {"Content-Type": "application/json", "X-VO-Api-Id": "dd437e41", "X-VO-Api-Key": "d0f221240482a3773be4b3e4d40ea8af"}
VOheaders = {"Content-Type": "application/json", "X-VO-Api-Id": VOAPIID, "X-VO-Api-Key": VOAPIKEY} # GH Added Env Var
GeneralHeader = {"Content-Type": "application/json" }


from botocore.vendored import requests

# phantomBaseURL = "https://admin:nuwmod-wAmgi7-vyxgow@ec2-3-95-210-57.compute-1.amazonaws.com"
phantomBaseURL = PHANTOMBASEURL # GH Added Env Var


def createContainer(theData):
    print("createContainer")
    
    createContainerUrl = phantomBaseURL + "/rest/container/"
    
    incidentName = "victorops incident# "+  theData["incident"] + " " + theData["entity_display_name"] 
    
    print(incidentName)
    
    containerPayload = json.dumps({"name" : incidentName , "label":"events", "template_id":4, "status":"new", "role_id":"1", "severity":"medium", "sensitivity":"amber", "type":"default" })
    
    print(createContainerUrl)
    
    print(containerPayload)
    
    response = requests.request("POST", createContainerUrl, headers=GeneralHeader, data = containerPayload, verify=False)

    print(response)    
    print(response.text)   
    
    resp = json.loads(response.text)
    return (resp["id"])
    
    
    
    
    
    
    
def addArtifact(container_id, theData):
    print(__name__)   
    print("container_id: " + str(container_id) + " " + json.dumps(theData))
    
    addArtifactUrl = phantomBaseURL + "/rest/artifact/"
    
    #incidentName = "victorops incident# "+  theData["incident"] + " " + theData["entity_display_name"] 
    
   # print(incidentName)
    
 #   artifactPayload = json.dumps({ "owner": 1, "container_id": container_id, "severity": "medium", "label": "event", "version": 1, "cef": {"environment" : "production", "entity_state" : "critical", "deviceHostname": "abc.com", "deviceOS" : "linux", "entity_id" : "123xxx", "monitoring_tool" : "signalfx", "teams" : "devops", "command" : "disk check", "incident_link" : "https://portal.victorops.com/ui/buttercup-games/incident/16753/details/"}, "name": "incident details", "source_data_identifier": "5f726c89-e445-4418-9da6-97d5314cde23"})
 
    artifactPayload = json.dumps({ "owner": 1, "container_id": container_id, "severity": "medium", "label": "event", "version": 1, "cef": theData, "name": "incident details", "source_data_identifier": "5f726c89-e445-4418-9da6-97d5314cde23"})
    
    print(addArtifactUrl)
    
    print(artifactPayload)
    
    response = requests.request("POST", addArtifactUrl, headers=GeneralHeader, data = artifactPayload, verify=False)

    print(response)    
    print(response.text)   
    
    #resp = json.loads(response.text)
   
    
    
    
def runPlaybook(container_id, playbook_id):
    print("running playbook: " + str(playbook_id) + " on container_id: " + str(container_id))
    
    runPlaybookURL = phantomBaseURL + "/rest/playbook_run"
    
    playbookPayload = json.dumps({ "playbook_id": int(playbook_id), "container_id": container_id, "run": "true", "scope": "new"})
    

    print(runPlaybookURL)
    
    print(playbookPayload)
    
    response = requests.request("POST", runPlaybookURL, headers=GeneralHeader, data = playbookPayload, verify=False)

    print(response)    
    print(response.text)  
