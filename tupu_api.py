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


class TUPU:
    def __init__(self, secret_id, private_key_path, url='http://api.open.tuputech.com/v3/recognition/'):
        self.__url = url + ('' if url.endswith('/') else '/') + secret_id
        self.__text_url = url + 'text/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__video_sync_url = url + 'video/syncscan/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__video_async_url = url + 'video/asyncscan/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__video_stream_url = url + 'video/stream/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__video_close_url = url + 'video/close/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__video_result_url = url + 'video/result/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__video_rate_url = url + 'video/rate/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__speech_url = url + 'speech/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__speech_async_url = url + 'speech/recording/async/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__speech_result_url = url + 'speech/recording/result/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__speech_stream_url = url + 'speech/stream/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__speech_stream_close_url = url + 'speech/stream/close/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__speech_stream_search_url = url + 'speech/stream/search/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__feedback_image_file_url = url + 'feedback/image/file/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__feedback_image_url_url = url + 'feedback/image/url/' + \
            ('' if url.endswith('/') else '/') + secret_id
        self.__feedback_text_string_url = url + 'feedback/text/string/' + \
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
        self.__nonce = str(random.random())
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

    def video_async(self, video, callback_url, options={}):
        self.__sign()

        request_data = {
            "video": video,
            "callbackUrl": callback_url,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        if options:
            for key in options:
                request_data[key] = options[key]

        response = requests.post(
            self.__video_async_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def video_stream(self, video, callback_url, options={}):
        self.__sign()

        request_data = {
            "video": video,
            "callbackUrl": callback_url,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        if options:
            for key in options:
                request_data[key] = options[key]

        response = requests.post(
            self.__video_stream_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def video_sync(self, video, options={}):
        self.__sign()

        request_data = {
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        if options:
            for key in options:
                request_data[key] = options[key]

        if os.path.isfile(video):
            files = {'video': (video, open(video, 'rb'), "video/mp4")}
        else:
            files = {'video': (None, video)}
        response = requests.post(
            self.__video_sync_url, data=request_data, files=files)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def video_close(self, videoId):
        self.__sign()

        request_data = {
            "videoId": videoId,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__video_close_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def video_result(self, videoId):
        self.__sign()

        request_data = {
            "videoId": videoId,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__video_result_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def video_rate(self):
        self.__sign()

        request_data = {
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__video_rate_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def speech(self, speech, options={}):
        self.__sign()
        request_data = {
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature,
        }
        if options:
            for key in options:
                request_data[key] = options[key]
        files = ""
        if os.path.isfile(speech):
            files = {'speech': (speech, open(speech, 'rb'))}
        else:
            request_data["speech"] = (None, speech)
        response = requests.post(
            self.__speech_url, data=request_data, files=files)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def speech_async(self, recording):
        self.__sign()

        request_data = {
            "recording": recording,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__speech_async_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def speech_result(self, requestId):
        self.__sign()

        request_data = {
            "requestId": requestId,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__speech_result_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def speech_stream(self, speechStream):
        if not isinstance(speechStream, list):
            raise Exception('[ArgsError] speechStream is a list')
        self.__sign()

        request_data = {
            "speechStream": speechStream,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }

        response = requests.post(
            self.__speech_stream_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def speech_stream_close(self, speechStream):
        if not isinstance(speechStream, list):
            raise Exception('[ArgsError] speechStream is a list')
        self.__sign()

        request_data = {
            "speechStream": speechStream,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__speech_stream_close_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def speech_stream_search(self, requestId):
        self.__sign()

        request_data = {
            "requestId": requestId,
            "timestamp": float(self.__timestamp),
            "nonce": float(self.__nonce),
            "signature": self.__signature
        }
        response = requests.post(
            self.__speech_stream_search_url, json=request_data)
        response_json = json.loads(response.text)
        if not "error" in response_json:
            response_json['verify_result'] = self.__verify(
                response_json['signature'], response_json['json'])
            response_json['json'] = json.loads(
                response_json['json'])
        return response_json

    def feedback_image_url(self, images, taskId):
        self.__sign()
        headers = {
            "timestamp": self.__timestamp,
            "nonce": self.__nonce,
            "signature": self.__signature,
        }
        request_data = {
            "taskId": taskId,
            "fileList": images
        }
        print(request_data)
        response = requests.post(
            self.__feedback_image_url_url, headers=headers, json=request_data)
        response_json = json.loads(response.text)
        return response_json

    def feedback_image_file(self, images):
        if not isinstance(images, list):
            raise Exception('[ArgsError] images is a list')
        self.__sign()
        headers = {
            "timestamp": self.__timestamp,
            "nonce": self.__nonce,
            "signature": self.__signature,
        }
        request_data = {
            "taskId": [],
            "label": []
        }

        multiple_files = []
        for imageObject in images:
            multiple_files.append(
                ('image', (imageObject["image"], open(imageObject["image"], 'rb'))))
            request_data["taskId"].append(imageObject["taskId"])
            request_data["label"].append(imageObject["label"])
        print(multiple_files)
        response = requests.post(
            self.__feedback_image_file_url, headers=headers, data=request_data, files=multiple_files)
        response_json = json.loads(response.text)
        return response_json

    def feedback_text_string(self, texts, taskId):
        self.__sign()
        headers = {
            "timestamp": self.__timestamp,
            "nonce": self.__nonce,
            "signature": self.__signature,
        }
        request_data = {
            "taskId": taskId,
            "texts": texts
        }
        print(request_data)
        response = requests.post(
            self.__feedback_text_string_url, headers=headers, json=request_data)
        response_json = json.loads(response.text)
        return response_json
