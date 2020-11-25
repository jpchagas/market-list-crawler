import schedule
import time
import os

print('Scheduler initialised')
schedule.every().day.at("00:15").do(lambda: os.system('scrapy crawl ceasars'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)