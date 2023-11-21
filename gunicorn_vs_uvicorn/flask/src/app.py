from flask import Flask, request
import time
import os

app = Flask(__name__)

t=float(os.environ.get("WAITING_TIME"))

@app.route('/wait', methods=['GET'])
def hello():
    start = time.time()
    time.sleep(t)
    elapsed_time =  time.time() - start
    print(f"wait: {elapsed_time}")
    return {"wait": f"{elapsed_time}"}

if __name__ == '__main__':
    app.run(debug=True)
