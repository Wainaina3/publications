#!/bin/bash
##script to create rsa keys
#Envs
CURRENT_DIR=$(pwd)
APP_DIR="/app"
APP_NAME="aptitude"

#check where the app is installed. If its /app then its in a container else, local
if [[ ${CURRENT_DIR} == ${APP_DIR} ]]
then   
    #save the encrytion key to default keys folder
    #ssh-keygen -t rsa -N ${APP_NAME} -f /aptitude/keys
    openssl genrsa -out $APP_DIR/aptitude/keys/aptitudeprivatekey.pem -passout pass:${APP_NAME} 1024
    openssl rsa -in $APP_DIR/aptitude/keys/aptitudeprivatekey.pem -passin pass:${APP_NAME} -pubout -out $APP_DIR/aptitude/keys/aptitudepublickey.pem
else
    #save the encrytion key locally in the configs folder
    #ssh-keygen -t rsa -N ${APP_NAME} -C "aptitudekey" -f $CURRENT_DIR/configs/configfiles/aptitude_key 
    openssl genrsa -out $CURRENT_DIR/configs/configfiles/aptitudeprivatekey.pem -passout pass:${APP_NAME} 1024

    openssl rsa -in $CURRENT_DIR/configs/configfiles/aptitudeprivatekey.pem -passin pass:${APP_NAME} -pubout -out $CURRENT_DIR/configs/configfiles/aptitudepublickey.pem
fi

#openssl genrsa -out rsaprivatekey.pem -passout pass:trousers -aes128 1024 >> create private key
#openssl rsa -in rsaprivatekey.pem -passin pass:trousers -pubout -out rsapublickey.pem >> create public key
#openssl rsautl -encrypt -pubin -inkey rsapublickey.pem -in wakeserver.sh -out cipher.txt >> encrypt data
#openssl rsautl -decrypt -inkey rsaprivatekey.pem -in cipher.txt -passin pass:trousers -out plain.txt  >> decrypt data

 