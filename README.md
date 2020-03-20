# TUPU Python SDK

SDK for TUPU visual recognition service
######
<https://www.tuputech.com> 

## Install Dependencies
```
sudo pip install rsa requests base64 json
```

## Interface
```
tupu_client = TUPU(secret_id, private_key_path, url)
```

### Parameters
- **secretId**: user's secret-id for accessing the API
- **private_key_path**: user's private key path
- **url**: default is "http://api.open.tuputech.com/v3/recognition/"

## Example

### image file
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

images = ["/home/user/001.jpg", "/home/user/002.jpg"]
result = tupu.api(images=images, is_url=False)

print(result)
```

### image url
```python
from tupu_api import TUPU

tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

images = ["http://example.com/001.jpg", "http://example.com/002.jpg"]
result = tupu.api(images=images, is_url=True)

print(result)
```

### text
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

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
```
