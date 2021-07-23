from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

video = "https://test.mp4"
callback_url = "http://test"
options = {}
result = tupu.video_async(
    video=video, callback_url=callback_url, options=options)

print(result)
