from tupu_api import TUPU
tupu = TUPU(secret_id='your_secret_id',
            private_key_path='./rsa_private_key.pem', 'http://feedback.open.tuputech.com/v1/')
texts = [{
    "content": "string",
    "mainLabel": "string",
    "subLabel": "string",
    "level": "danger"
}, {
    "content": "string2",
    "mainLabel": "string3",
    "subLabel": "string2",
    "level": "danger"
}]
taskId = "图普对应的任务id"
result = tupu.feedback_text_string(texts=texts, taskId=taskId)
print(result)
