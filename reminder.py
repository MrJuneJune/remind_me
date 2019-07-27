from datetime import datetime
import webbrowser
import time
import csv

class reminder():
    def __init__(self):
        # Storing what it need to be reminded in a list.
        self.total_schedule = []
        datetime_format = '%H:%M %d %m %y'
        today = datetime.now().strftime("%d %b %y")
        print("Today is {0} !".format(today))
        while True:
            remind_me_this = input("What do you want to be reminded of (if nothing, press enter) ?\n")
            if remind_me_this != '':
                time_for_reminder = datetime.strptime(input("At what time and date ? {0}\n".format(datetime_format)), datetime_format)
                if datetime.now() < time_for_reminder:
                    self.total_schedule.append((remind_me_this, time_for_reminder))
            else:
                break

        # Creating csv file of this.
        with open('remind_me.csv','w') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(['Task', 'Time'])
            for row in self.total_schedule:
                csv_out.writerow(row) 

    def remind_me(self):
        print(self.total_schedule)
        while True:
            # Checking every 10 seconds.
            time.sleep(10)
            for i in range(len(self.total_schedule)):
                if datetime.now().replace(second=0, microsecond=0) == self.total_schedule[i][1]:
                    # Opening up browser to let you know.
                    webbrowser.open('https://www.google.com/search?client=ubuntu&channel=fs&q={0}&ie=utf-8&oe=utf-8'.format(self.total_schedule[i][0]))
                    self.total_schedule.pop(i)
                    print("There are {0} more things to do !".format(len(self.total_schedule)))
            if len(self.total_schedule) == 0:
                break

if __name__ == "__main__":
    x=reminder()
    x.remind_me()
