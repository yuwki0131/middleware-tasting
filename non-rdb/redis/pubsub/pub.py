import redis
import time

# Redisクライアントの設定
client = redis.Redis(host='localhost', port=6379, db=0)

# メッセージを定期的に送信
while True:
    client.publish('my_channel', 'Hello, Redis!')
    time.sleep(1)  # 1秒ごとにメッセージを送信
