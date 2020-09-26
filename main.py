'''Retrieves the current Unix time(epoch time)'''
import time
import os
from flask import Flask

app = Flask(__name__)

@app.route('/<timenow>/')
def get_time(timenow):
    time_now = time.time()
    return str(time_now)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)