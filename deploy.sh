if [ -z "$1" ]; then
    echo "ERROR: version is required"    
    exit 1
fi 

VERSION=$1
NAME="pt_web.v"$VERSION".zip"

echo "Downloading $NAME"
aws s3 cp "s3://pt-spb/"$NAME $NAME

echo "Unzipping $NAME"

unzip -o $NAME
rm $NAME

zip -r pt-web-l.zip . -x *.pyc -x *.swp -x *.git* -x *.zip
echo "Zipped. Uploading..."

aws s3 cp pt-web-l.zip "s3://pt-spb/pt-web-l.v"$VERSION".zip"

