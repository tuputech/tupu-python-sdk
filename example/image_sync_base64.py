from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

images = ["base64_0", "base64_1"]
options = {}
result = tupu.image_sync_base64(images=images, options=options)

print(result)
