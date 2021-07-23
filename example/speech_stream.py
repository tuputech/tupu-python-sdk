from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

speech = "https://test.mp3"

result = tupu.speech_stream([{
    "url": speech,
    "callback": "http://test/callback",
    "roomId": "test122",
    "userId": "test122",
    "forumId": "test122"
}])

print(result)
