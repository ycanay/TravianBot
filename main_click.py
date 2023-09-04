import schedule
import Click_Farms as cf
import time

def task():
    cf.open_edge()
    cf.go_farm_list()
    cf.click_farms()

schedule.every(15).minutes.do(task)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
