import subprocess
import os

def lambda_handler(event=None, context=None):

    os.putenv("PT_RELEASE_NAME", event["PT_RELEASE_NAME"])
    os.putenv("PT_START_DATE", event["PT_START_DATE"])
    os.putenv("PT_TOKEN", event["PT_TOKEN"])
    os.putenv("PT_PROJECT_ID", event["PT_PROJECT_ID"])

    res = subprocess.check_output(["env"])
    print res

    res = subprocess.check_output(["ls"])
    print res

    res = subprocess.check_output(
            ["./pt_web_v.0.1"])

    print res

    print "Done"

if __name__ == "__main__":
    lambda_handler(dict(

            PT_PROJECT_ID=os.getenv("PT_PROJECT_ID"),
            PT_RELEASE_NAME=os.getenv("PT_RELEASE_NAME"),
            PT_START_DATE=os.getenv("PT_START_DATE"),
            PT_TOKEN=os.getenv("PT_TOKEN")

        ))
