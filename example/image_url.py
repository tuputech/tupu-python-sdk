from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

images = ["http://example.com/001.jpg", "http://example.com/002.jpg"]
result = tupu.api(images=images, is_url=True)

print(result)
