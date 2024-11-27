from aip import AipSpeech

# 初始化AipSpeech对象，传入APPID、API Key、Secret Key
appid = '116123078'
api_key = 'fL9c3xIuAAP5lcZWil4HIUIV'
secret_key = 'WakfRCsfuSfdbLUCNP8vlQLpOgdEfdO1'
client = AipSpeech(appid, api_key, secret_key)

# 调用语音合成接口，合成一段文本为语音
result = client.synthesis('你好，欢迎使用百度语音合成', 'zh', 1, {'per': 0})

# 如果result是一个错误码，说明合成失败；如果是二进制流，说明合成成功
if isinstance(result, dict):
    print("Error: ", result)
else:
    with open('output.mp3', 'wb') as f:
        f.write(result)
