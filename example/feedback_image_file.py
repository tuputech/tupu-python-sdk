from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem', 'http://feedback.open.tuputech.com/v1/')

images = [{
    "image": "/home/user/001.jpg",
    # 图普对应的任务Id, 参考：http://cloud.doc.tuputech.com/zh/taskList/imageLabel.html
    "taskId": "54bcfc6c329af61034f7c2fc"
    "label": 1  # 图普对应的任务标签
}]
result = tupu.feedback_image_file(images=images)

print(result)
