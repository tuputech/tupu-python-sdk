from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

images = ["/home/user/001.jpg", "/home/user/002.jpg"]
result = tupu.api(images=images, is_url=False)

print(result)
