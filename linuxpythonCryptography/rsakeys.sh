#!/bin/bash
##script to create rsa keys
#Envs
CURRENT_DIR=$(pwd)

APP_NAME="linuxpythonCryptography"

##create private key with app name as passphrase and 1024 bytes
openssl genrsa -out $CURRENT_DIR/keys/aptitudeprivatekey.pem -passout pass:${APP_NAME} 1024

##pass app name as passphrase and private key to create public key
openssl rsa -in $CURRENT_DIR/keys/aptitudeprivatekey.pem -passin pass:${APP_NAME} -pubout -out $CURRENT_DIR/configs/configfiles/aptitudepublickey.pem