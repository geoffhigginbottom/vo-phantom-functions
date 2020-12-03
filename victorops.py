import json
import boto3

VICTOROPSURL = os.environ['VICTOROPSURL'] # GH Added Env Var instead of using hard coded URL
VOAPIID = os.environ['VOAPIID'] # GH Added Env Var
VOAPIKEY = os.environ['VOAPIKEY'] # GH Added Env Var
PHANTOMDEEPLINKURL = os.environ['PHANTOMDEEPLINKURL'] # GH Added Env Var


# victoropsUrl = "https://alert.victorops.com/integrations/generic/20131114/alert/86eebbb7-f101-4e43-ba15-755fceca87c3/"
victoropsUrl = VICTOROPSURL # GH Added Env Var instead of using hard coded URL

# VOheaders = {"Content-Type": "application/json", "X-VO-Api-Id": "dd437e41", "X-VO-Api-Key": "d0f221240482a3773be4b3e4d40ea8af"}
VOheaders = {"Content-Type": "application/json", "X-VO-Api-Id": VOAPIID, "X-VO-Api-Key": VOAPIKEY} # GH Added Env Var
GeneralHeader = {"Content-Type": "application/json" }


from botocore.vendored import requests

def sendNote(container_id, theData):
    print("sendNote")
    
    incidentId = theData["incident"]
    
    # phantomDeepLinkURL = "https://ec2-3-95-210-57.compute-1.amazonaws.com/mission/" + str(container_id) + "/analyst/timeline"
    phantomDeepLinkURL = PHANTOMDEEPLINKURL + str(container_id) + "/analyst/timeline" # GH Added Env Var
 

    notePayload = json.dumps({"name":"phantomContainer", "display_name":"Phantom Container", "json_value":{"id":container_id, "url": phantomDeepLinkURL}})

    voNotesURI = "https://api.victorops.com/api-public/v1/incidents/" + str(incidentId) + "/notes"

    voNotesResponse = requests.request("POST", voNotesURI, headers=VOheaders, data = notePayload)

    print(voNotesResponse)   
    


def sendAcknowledgement(container_id, theData):
    print("sendAcknowledgement")
    
    
    entity_id = theData["entity_id"] 
    
    # phantomDeepLinkURL = "https://ec2-3-95-210-57.compute-1.amazonaws.com/mission/" + str(container_id) + "/analyst/timeline"
    phantomDeepLinkURL = PHANTOMDEEPLINKURL + str(container_id) + "/analyst/timeline"
    
    
    ackPayload = json.dumps({"message_type" : "ACKNOWLEDGEMENT", "entity_id" : entity_id, "monitoring_tool" : "signalfx", "state_message" : "running phantom playbook to remediate", "vo_annotate.u.Phantom Container" : phantomDeepLinkURL })
    
    print(victoropsUrl)
    
    print(ackPayload)
    
    response = requests.request("POST", victoropsUrl, headers=GeneralHeader, data = ackPayload, verify=False)

    print(response)    
    print(response.text)   
    
    #resp = json.loads(response.text)
 
def sendDeepLink(container_id, theData):
    print("sendAcknowledgement")
    
    
    entity_id = theData["entity_id"] 
    
    # phantomDeepLinkURL = "https://ec2-3-95-210-57.compute-1.amazonaws.com/mission/" + str(container_id) + "/analyst/timeline"
    phantomDeepLinkURL = PHANTOMDEEPLINKURL + str(container_id) + "/analyst/timeline" # GH Added Env Var
    
    
    ackPayload = json.dumps({"message_type" : "INFO", "entity_id" : entity_id, "monitoring_tool" : "phantom", "state_message" : "creating phantom container", "vo_annotate.u.Phantom Container" : phantomDeepLinkURL })
    
    print(victoropsUrl)
    
    print(ackPayload)
    
    response = requests.request("POST", victoropsUrl, headers=GeneralHeader, data = ackPayload, verify=False)

    print(response)    
    print(response.text)   
    
    #resp = json.loads(response.text)   

def sendRecovery(theData):
    print("sendRecovery")
    
    
    entity_id = theData["entity_id"] 
    
    recoveryPayload = json.dumps({"message_type" : "RECOVERY", "entity_id" : entity_id, "monitoring_tool" : "signalfx", "state_message" : "21% free, 73GB available" })
    
    print(victoropsUrl)
    
    print(recoveryPayload)
    
    response = requests.request("POST", victoropsUrl, headers=GeneralHeader, data = recoveryPayload, verify=False)

    print(response)    
    print(response.text)   
    
    #resp = json.loads(response.text)
