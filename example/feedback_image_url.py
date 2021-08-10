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
# 图普对应的任务Id, 参考：http://cloud.doc.tuputech.com/zh/taskList/imageLabel.html
taskId = "54bcfc6c329af61034f7c2fc"
result = tupu.feedback_image_url(images=images, taskId=taskId)

print(result)
