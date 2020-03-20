from tupu_api import TUPU

tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

# content and contentId are required
texts = [
    {
        "content": "test from python sdk",
        "userId": "your_userId",
        "forumId": "your_forumId",
        "contentId": "your_content_id"
    },
    {
        "content": "test from python sdk",
        "contentId": "your_content_id_2"
    }
]
result = tupu.text_api(texts=texts)

print(result)
