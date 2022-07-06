#!/bin/bash
##script to encrypt plan data from a file and write to a encrypteddata file

#Envs
CURRENT_DIR=$(pwd)

##encrypt data in plaindata file and save to encrypteddata file with in base64 encoding in PKCS1_OAEP padding
## -oaep which gives PKCS1_OAEP will be key in how we decrypt in python
openssl rsautl -encrypt -oaep -pubin -inkey $CURRENT_DIR/keys/publickey.pem -in plaindata.txt | openssl base64 > encrypteddata
