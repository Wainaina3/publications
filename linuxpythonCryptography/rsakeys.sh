#!/bin/bash
##script to create rsa keys
#Envs
CURRENT_DIR=$(pwd)

APP_NAME="linuxpythonCryptography"

##create keys directory
mkdir keys
##create private key with app name as passphrase and 1024 is the numbits or keysize in bits
openssl genrsa -out $CURRENT_DIR/keys/privatekey.pem -passout pass:${APP_NAME} 1024

##pass app name as passphrase and private key to create public key
openssl rsa -in $CURRENT_DIR/keys/privatekey.pem -passin pass:${APP_NAME} -pubout -out $CURRENT_DIR/keys/publickey.pem