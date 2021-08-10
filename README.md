# TUPU Python SDK

SDK for TUPU visual recognition service
######
<https://www.tuputech.com> 


## Install Dependencies
Use python3

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

### image file （图片文件）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

images = ["/home/user/001.jpg", "/home/user/002.jpg"]
result = tupu.api(images=images, is_url=False)

print(result)
```

### image url （图片链接）
```python
from tupu_api import TUPU

tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

images = ["http://example.com/001.jpg", "http://example.com/002.jpg"]
result = tupu.api(images=images, is_url=True)

print(result)
```

### text （文本）
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

### video syncscan  （视频同步识别）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

video = "http://example.com/001.mp4" or "/home/source/001.mp4"

# 可选参数
options = { 
    "interval": 1,
    "maxFrames": 200,
    "tag": "tag",
    "task": ["id"]
}
result = tupu.video_sync(video=video, options=options)

print(result)
```

### video asyncscan  （视频文件异步识别）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

video = "http://example.com/001.mp4"
callbackUrl = "http://example.com/callbackUrl"

# 可选参数
options = { 
    "customInfo": {},
    "interval": 3,
    "callbackRules": {},
    "realTimeCallback": false,
    "audio": false,
    "task": ["id"]
}
result = tupu.video_async(video=video, callbackUrl=callbackUrl, options=options)

print(result)
```


### video stream  （视频流异步识别）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

video = "http://example.com/001.mp4"
callbackUrl = "http://example.com/callbackUrl"

# 可选参数
options = { 
    "customInfo": {},
    "interval": 3,
    "fragmentTime": 60,
    "callbackRules": {},
    "audio": false,
    "task": ["id"]
}
result = tupu.video_stream(video=video, callbackUrl=callbackUrl, options=options)

print(result)
```

### video close  （关闭异步识别）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

videoId = ""
result = tupu.video_close(videoId=videoId)

print(result)
```

### video search  （查询异步识别结果）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

videoId = ""
result = tupu.video_result(videoId=videoId)

print(result)
```

### video rate  （查询异步识别并发及待处理任务数）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

result = tupu.video_rate()

print(result)
```


### speech （语音文件同步）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

speech = "http://example.com/001.mp3" or "/home/source/001.mp3"
result = tupu.speech(speech=speech)

print(result)
```

### speech async（语音文件异步）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

recording = {
    "url": "http://www.tupu.com/test.mp3",
    "callbackUrl": "http://your_cb.com",
    "roomId": "your_room_id",
    "userId": "your_user_id",
    "forumId": "your_forum_id"
  }
result = tupu.speech_async(recording=recording)

print(result)
```

### speech async result（语音文件异步结果查询）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

requestId = "your_requestId"
result = tupu.speech_result(requestId=requestId)

print(result)
```

### speech stream（音频流提交接口）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

speechStream = [
  {
    "url": "rtmp://pili-Room-4daedc9c7a5db36c325f6609000c0201",
    "callback": "http://www.tupu.com/callback",
    "roomId": "111111",
    "userId": "23231",
    "forumId": "321313"
  }
]
result = tupu.speech_stream(speechStream=speechStream)

print(result)
```


### speech stream close（音频流关闭接口）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

speechStream = [
  {
      "requestId": "5c8213b9bc807806aab0a321"
  }
]
result = tupu.speech_stream_close(speechStream=speechStream)

print(result)
```


### speech stream search（语音流状态查询接口）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem')

requestId = "your_requestId"
result = tupu.speech_stream_search(requestId=your_requestId)

print(result)
```

### feedback image file（数据回流-图片文件上传接口）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem', 'http://feedback.open.tuputech.com/v1/')

images = [{
    "image": "/home/user/001.jpg",
    "taskId": "54bcfc6c329af61034f7c2fc" # 图普对应的任务Id, 参考：http://cloud.doc.tuputech.com/zh/taskList/imageLabel.html
    "label": 1  # 图普对应的任务标签
}]
result = tupu.feedback_image_file(images=images)

print(result)
```

### feedback image url（数据回流-图片url上传接口）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem', 'http://feedback.open.tuputech.com/v1/')

images = [{
    "imageUrl": "http://example.com/001.jpg",
    "label": 1  # 图普对应的任务标签
}, {
    "imageUrl": "http://example.com/002.jpg",
    "label": 1  # 图普对应的任务标签
}]
taskId = "54bcfc6c329af61034f7c2fc" # 图普对应的任务Id, 参考：http://cloud.doc.tuputech.com/zh/taskList/imageLabel.html
result = tupu.feedback_image_url(images=images, taskId=taskId)

print(result)
```


### feedback text url（数据回流-文本上传接口）
```python
from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem', 'http://feedback.open.tuputech.com/v1/')

texts = [{
    "content": "string",  # 文本
    "mainLabel": "string",  # 第一级类别取值
    "subLabel": "string",  # 第二级类别取值
    "level": "danger"   # 违规危险程度 ['danger', 'warn']
}]
taskId = "57c4036c557603652aeeb222" # 图普对应的任务Id, 参考：http://cloud.doc.tuputech.com/zh/taskList/textLabel.html
result = tupu.feedback_text_string(texts=texts, taskId=taskId)

print(result)
```