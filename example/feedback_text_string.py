from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem', 'http://feedback.open.tuputech.com/v1/')
texts = [{
    "content": "string",  # 文本
    "mainLabel": "string",  # 第一级类别取值
    "subLabel": "string",  # 第二级类别取值
    "level": "danger"   # 违规危险程度 ['danger', 'warn']
}]
# 图普对应的任务Id, 参考：http://cloud.doc.tuputech.com/zh/taskList/textLabel.html
taskId = "57c4036c557603652aeeb222"
result = tupu.feedback_text_string(texts=texts, taskId=taskId)

print(result)
