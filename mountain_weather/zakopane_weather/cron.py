from django_cron import CronJobBase, Schedule
from mountain import get_data

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'zakopane_weather.my_cron_job' 
    def do(self):
        get_data()
        print("job is done")
