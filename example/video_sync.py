from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

video = "test.mxf"  # 或 "https://test.mp4"
options = {}
result = tupu.video_sync(video=video, options=options)

print(result)
