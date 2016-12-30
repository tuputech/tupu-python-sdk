from tupu_api import TUPU

if __name__ == '__main__':
    tupu = TUPU(secret_id='', #secretId
                private_key_path='', #私钥证书路径
                tupu_public_key_path='', #图普公钥路径
                url='http://api.open.tuputech.com/v3/recognition/')

    # url
    images = ["http://xxxxx/test.jpg", ]#url 路径
    print tupu.api(images=images, is_url=True)

    # image
    images = ['xxxxx/image.jpg', ]#本地文件路径
    print tupu.api(images=images, is_url=False)

    # zip
    images = ['xxxxx/zip_test.zip', ]
    print tupu.api(images=images, is_url=False)
