import os
import random
import datetime
import rsa
import requests
import base64
import json
import time


TUPU_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDyZneSY2eGnhKrArxaT6zswVH9
/EKz+CLD+38kJigWj5UaRB6dDUK9BR6YIv0M9vVQZED2650tVhS3BeX04vEFhThn
NrJguVPidufFpEh3AgdYDzOQxi06AN+CGzOXPaigTurBxZDIbdU+zmtr6a8bIBBj
WQ4v2JR/BA6gVHV5TwIDAQAB
-----END PUBLIC KEY-----
"""


class VideoOptions:
    def __init__(self):
        self.customInfo = dict()
        self.interval = 1
        self.callbackRules = dict()
        self.realTimeCallback = False
        self.audio = False
        self.task = list()


class TUPU:
    def __init__(self, secret_id, private_key_path, url='http://api.open.tuputech.com/v3/recognition/'):
        self.__url = url + ('' if url.endswith('/') else '/') + secret_id
        self.__text_url = url + 'text/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__video_url = url + 'video/asyncscan/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__secret_id = secret_id
        # get private key
        with open(private_key_path) as private_key_file:
            self.__private_key = rsa.PrivateKey.load_pkcs1(
                private_key_file.read())
        # get tupu public key
        self.__public_key = rsa.PublicKey.load_pkcs1_openssl_pem(
            TUPU_PUBLIC_KEY)

    def __sign(self):
        """get the signature"""
        self.__timestamp = str(time.time())
        self.__nonce = str(random.randint(1 << 4, 1 << 32))
        sign_string = "%s,%s,%s" % (
            self.__secret_id, self.__timestamp, self.__nonce)
        self.__signature = base64.b64encode(
            rsa.sign(sign_string.encode("utf-8"), self.__private_key, 'SHA-256')).decode('utf-8')

    def __verify(self, signature, verify_string):
        """verify the signature"""
        try:
            rsa.verify(verify_string.encode("utf-8"),
                       base64.b64decode(signature), self.__public_key)
            return "Success"
        except rsa.pkcs1.VerificationError:
            print("Verification Failed")
        return "Failed"

    def api(self, images, is_url=False):
        if not isinstance(images, list):
            raise Exception('[ArgsError] images is a list')
        self.__sign()
        request_data = {
            "timestamp": self.__timestamp,
            "nonce": self.__nonce,
            "signature": self.__signature
        }
        response = None
        if is_url:
            request_data["image"] = images
            response = requests.post(self.__url, data=request_data)
        else:
            multiple_files = []
            for image_file in images:
                if not os.path.isfile(image_file):
                    print('[SKIP FILE] No such file "%s"' % image_file)
                    continue
                multiple_files.append(
                    ('image', (image_file, open(image_file, 'rb'), 'application/*')))
            response = requests.post(
                self.__url, data=request_data, files=multiple_files)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(response_json['json'])
        return response_json

    def text_api(self, texts):
        if not isinstance(texts, list):
            raise Exception('[ArgsError] texts is a list')
        self.__sign()
        request_data = {
            "text": texts,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__text_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def video_async(self, video_url, callback_url, options: VideoOptions = None):
        self.__sign()

        request_data = {
            "video": video_url,
            "callbackUrl": callback_url,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        if options:
            if options.customInfo:
                request_data['customInfo'] = options.customInfo
            if options.interval:
                request_data['interval'] = options.interval
            if options.callbackRules:
                request_data['callbackRules'] = options.callbackRules
            if options.task:
                request_data['task'] = options.task
            request_data['realTimeCallback'] = options.realTimeCallback
            request_data['audio'] = options.audio

        response = requests.post(
            self.__video_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json
