import hmac
import hashlib
import base64

# 定义密钥和消息
key = b'secret_key'  # 使用字节格式的密钥
message = b'This is a message.'  # 使用字节格式的消息

# 生成 HMAC-SHA256 加密
hmac_sha256 = hmac.new(key, message, hashlib.sha256).digest() # .hexdigest()

print("HMAC-SHA256:", hmac_sha256)
hmac_sha256 = base64.b64encode(hmac_sha256)
print("HMAC-SHA256:", hmac_sha256)
hmac_sha256 = hmac_sha256.decode('utf-8')
print("HMAC-SHA256:", hmac_sha256)