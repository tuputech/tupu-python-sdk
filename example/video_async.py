from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

video_url = "https://test.mp4"
callback_url = "http://test"
options = {}
result = tupu.video_async(
    video_url=video_url, callback_url=callback_url, options=options)

print(result)
