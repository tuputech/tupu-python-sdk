from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')
requestId = ""
result = tupu.speech_result(requestId=requestId)

print(result)
