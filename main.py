from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask
import os


app = Flask(__name__)


def batch():
    os.system('scrapy crawl ceasars')


sched = BackgroundScheduler(daemon=True)
sched.add_job(batch, 'cron', day='*', hour='23', minute='59')
sched.start()


@app.route("/")
def index():
    return "<h1>Hello World</hi>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)