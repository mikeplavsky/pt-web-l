import subprocess
import os

def lambda_handler(event=None, context=None):

    [os.putenv(k, event[k]) for k in event.keys()]

    res = subprocess.check_output(
            [event["PT_WEB"]])

    print res

    print "Done"

if __name__ == "__main__":

    vrs = ["PT_PROJECT_ID", 
           "PT_RELEASE_NAME", 
           "PT_START_DATE", 
           "PT_TOKEN", 
           "PT_WEB"]

    evt = dict()

    [evt.update(
        (k,os.getenv(k)) for k in vrs)]

    lambda_handler(evt)
