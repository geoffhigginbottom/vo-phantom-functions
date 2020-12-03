import json
import phantom
import victorops
import time

def checkIfDiskSpaceLow(theData):
    print("checking disk space")
    
    message = theData["entity_display_name"]
    
    msgtoCheck = "Critically Low Disk Space"
    res = message.find(msgtoCheck)
    
    print("result: " + str(res) + " " +  message + " " + msgtoCheck)    
    
    if ( res != -1):
        runPhantomWorkflow(theData)
    else:
        print("not running")


def runPhantomWorkflow(theData):
    print("abc")
    print(theData)

    # create container
    container_id = phantom.createContainer(theData)
    victorops.sendDeepLink(container_id, theData)

    victorops.sendAcknowledgement(container_id, theData)
    
    victorops.sendNote(container_id, theData)

    
    # add metadata
    phantom.addArtifact(container_id, theData)
    
    #playbook = theData["phantom_playbook_id"]
    
    # run runbook
    #phantom.runPlaybook(container_id, playbook)
    
    #time.sleep(6)
    
    #victorops.sendRecovery(theData)




def lambda_handler(event, context):
    
    #print(event)
    #print(context)
    
    data = event['body']

    print(data)

    print(type(data))
    
    if (type(data) == str ): 
        dataJson = json.loads(data)
    else:
        dataJson = data
    
#    dataJson = json.loads(data)
    
    
    checkIfDiskSpaceLow(dataJson)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
