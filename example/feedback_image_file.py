from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem', 'http://feedback.open.tuputech.com/v1/')

images = [{
    "image": "/home/user/001.jpg",
    "taskId": "图普对应的任务id",
    "label": 1  # 图普对应的任务标签
}, {
    "image": "/home/user/002.jpg",
    "taskId": "图普对应的任务id",
    "label": 1  # 图普对应的任务标签
}]
result = tupu.feedback_image_file(images=images)

print(result)
