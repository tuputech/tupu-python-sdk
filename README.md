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

#### Parameters
    - **secretId**: user's secret-id for accessing the API
    - **private_key_path**: user's private key path
    - **url**: default is "http://api.open.tuputech.com/v3/recognition/"

## Example

    ```
    from tupu_api import TUPU
    tupu = TUPU(secret_id='xxxxxxxxxxxxxxxxxx',
                        private_key_path='./rsa_private_key.pem')
    # url
    images = ["http://example.com/001.jpg", "http://example.com/002.jpg"]
    result = tupu.api(images=images, is_url=True)
    # image file
    images = ["/home/user/001.jpg", "/home/user/002.jpg"]
    result = tupu.api(images=images, is_url=False)
    # zip file
    images = ["/home/user/001.zip", "/home/user/002.zip"]
    result = tupu.api(images=images, is_url=False)

    print result["verify_result"]
    ```
