from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

videoId = ""
result = tupu.video_close(videoId=videoId)

print(result)
