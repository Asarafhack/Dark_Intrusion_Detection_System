from flask import Flask, request, jsonify
from collections import defaultdict
import time

app = Flask(__name__)

# Rate-limiting storage
request_counts = defaultdict(int)
last_request_time = defaultdict(float)
THRESHOLD = 10  # Max requests per second

@app.route('/test', methods=['GET', 'POST'])
def test():
    client_ip = request.remote_addr
    current_time = time.time()

    # Check rate-limiting
    if current_time - last_request_time[client_ip] < 1:
        request_counts[client_ip] += 1
    else:
        request_counts[client_ip] = 1

    last_request_time[client_ip] = current_time

    if request_counts[client_ip] > THRESHOLD:
        return jsonify({"error": "Too many requests. You are blocked!"}), 429

    return "Packet received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
