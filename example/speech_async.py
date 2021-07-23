from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

speechUrl = "https:/test.mp3"
result = tupu.speech_async({
    "url": speechUrl,
    "callbackUrl": "http://test/callbackUrl",
    "roomId": "test122",
    "userId": "test122",
    "forumId": "test122"
})

print(result)
