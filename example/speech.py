from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

speech = "test.mp3"  # "http://example.com/001.mp3"
result = tupu.speech(speech=speech)

print(result)
