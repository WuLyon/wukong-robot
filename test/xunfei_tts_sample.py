import base64
import hmac
import hashlib
import datetime
import requests

# 配置参数
APPID = "c1452e18"  # 替换为实际的APPID
APIKey = "38044e44441372ce9ca4d645757fd897"  # 替换为实际的APIKey
APISecret = "NjI1OWNkOGQwZTliNTIxYzg3ZjE2MzIy"  # 替换为实际的APISecret
text = "科大讯飞智能语音测试文本"  # 合成的文本内容
filename = "tts_sample.wav"  # 输出的音频文件名

# 生成 Authorization 鉴权
def get_authorization():
    date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    signature_origin = f"host: tts-api.xfyun.cn\ndate: {date}\nPOST /v2/tts HTTP/1.1"
    signature_sha = hmac.new(APISecret.encode('utf-8'), signature_origin.encode('utf-8'), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(signature_sha).decode('utf-8')
    authorization_origin = f'api_key="{APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature}"'
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode('utf-8')
    return authorization, date

# 发送 TTS 请求
def text_to_speech(text, filename):
    authorization, date = get_authorization()
    headers = {
        "Authorization": authorization,
        "Date": date,
        "Host": "tts-api.xfyun.cn",
        "Content-Type": "application/json",
    }
    payload = {
        "common": {"app_id": APPID},
        "business": {
            "aue": "raw",
            "auf": "audio/L16;rate=16000",
            "vcn": "xiaoyan",
            "tte": "UTF8"
        },
        "data": {
            "status": 2,
            "text": base64.b64encode(text.encode('utf-8')).decode('utf-8')
        }
    }
    
    response = requests.post("https://tts-api.xfyun.cn/v2/tts", headers=headers, json=payload)
    
    # 错误处理
    if response.status_code != 200:
        print(f"请求失败，状态码：{response.status_code}")
        print("响应内容：", response.content)
        return

    # 保存音频文件
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"合成完毕，音频已保存为{filename}")

# 执行合成
text_to_speech(text, filename)
