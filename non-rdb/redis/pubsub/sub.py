import redis

def message_handler(message):
    print("Received:", message['data'].decode())

# Redisクライアントの設定
client = redis.Redis(host='localhost', port=6379, db=0)
pubsub = client.pubsub()

# チャンネルの購読
pubsub.subscribe(**{'my_channel': message_handler})

# メッセージの待受
pubsub.run_in_thread(sleep_time=0.001)
