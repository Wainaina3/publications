from base64 import b64decode
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def test_decryption():
        encrypted_data_file = "encryptedconfig"

        private_key_file = "aptitudeprivatekey.pem"
         
        with open(private_key_file,'r') as key:
            #skip first and last line (-----BEGIN RSA PRIVATE KEY----- -----END RSA PRIVATE KEY-----)
            private_key_lines = key.readlines()[1:-1]
            private_key_clean = ""
            #clean the private file into readable format
            for line in private_key_lines:
                private_key_clean ="".join([private_key_clean,line.rstrip()])

            #working code but with externally cleaned private key
            #private_key = RSA.importKey(base64.b64decode(key.read()),passphrase="aptitude")

            #testing with cleaned private key
            private_key = RSA.importKey(base64.b64decode(private_key_clean),passphrase="aptitude")

        with open(encrypted_data_file,'r') as ecrypted_file:
            encrypted_data = ecrypted_file.read()

        rsa_cipher = PKCS1_OAEP.new(private_key)
        dec_data = rsa_cipher.decrypt(base64.b64decode(encrypted_data)).decode()
        #rsa_cipher = Cipher_PKCS1_v1_5.new(private_key)
        #dec_data = rsa_cipher.decrypt(base64.b64decode(encrypted_data), None).decode()
        print("Decrypting encrypted file data")
        print(dec_data)

test_decryption()