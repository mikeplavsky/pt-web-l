if [ -z "$1" ]; then
    echo "ERROR: version is required"    
    exit 1
fi 

VERSION=$1

zip -r pt-web-l.zip . -x *.pyc -x *.swp -x *.git* -x *.zip
echo "Zipped. Uploading..."

aws s3 cp pt-web-l.zip "s3://pt-spb/pt-web-l.v"$VERSION".zip"

