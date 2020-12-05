#!/bin/bash

prod=""
if [ -z $1 ]
then
    echo "Building in development mode!"
else
    if [ $1 = "prod" ]
    then
        echo "Building in production mode!"
        prod="--prod --output-hashing none"
    fi
fi

ng build $prod --deploy-url /static/ang/ --output-path ../backend/static/ang/ --resources-output-path ressources &&

echo "\nMoving index.html!" &&
mv -v ../backend/static/ang/index.html ../backend/templates &&

echo "\nCopying static files!" &&
cp -vr ../backend/static/ang/static/* ../backend/static &&

echo "\nDeleting origin static files!" &&
rm -vr ../backend/static/ang/static &&

echo "\nBuild success!"
