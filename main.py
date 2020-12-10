from apscheduler.schedulers.background import BackgroundScheduler
from market_list_crawler.controller.price_controller import PriceController

from flask import Flask, request
import os


app = Flask(__name__)



def batch():
    os.system('scrapy crawl ceasars')


sched = BackgroundScheduler(daemon=True)
sched.add_job(batch, 'cron', day='*', hour='23', minute='59')
sched.start()


@app.route("/price", methods=["GET"])
def get_prices():
    pc = PriceController()
    return pc.get_price_information(request)


@app.route("/price", methods=['POST'])
def get_price_by_name_date():
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)