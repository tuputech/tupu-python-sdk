from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

result = tupu.speech_stream_close([{
    "requestId": "60f12563d59aa5877b7e9a19"
}])

print(result)
