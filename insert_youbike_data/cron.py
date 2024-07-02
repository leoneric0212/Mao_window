from crontab import CronTab
import os
cron = CronTab(user=True)
path = os.path.abspath("./lesson2.py")
job = cron.new(command=f"/home/pi/miniconda3/bin/python '{path}'")
job.minute.every(1)
cron.write()