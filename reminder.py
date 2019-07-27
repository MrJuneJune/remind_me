from datetime import datetime
import webbrowser
import time
import csv

class reminder():
    def __init__(self):
        # Storing what it need to be reminded in a list.
        self.datetime_format = '%H:%M %d %m %y'
        today = datetime.now().strftime("%d %b %y")
        print("Today is {0} !".format(today))

        # Write in CSV file
        reminders = open('remind_me.csv','a')
        csv_out=csv.writer(reminders)
        while True:
            remind_me_this = input("What do you want to be reminded of (if nothing, press enter) ?\n")
            if remind_me_this != '':
                time_for_reminder = datetime.strptime(input("At what time and date ? {0}\n".format(self.datetime_format)), self.datetime_format)
                if datetime.now() < time_for_reminder:
                    csv_out.writerow((remind_me_this, time_for_reminder.strftime(self.datetime_format)))
            else:
                break
        reminders.close()

    def remind_me(self):
        # Read CSV file
        reminder_list = list(csv.reader(open('remind_me.csv', 'r'), delimiter=',', quotechar='|'))
        
        # Filtering pasted tasks
        reminder_list_clean = []
        for i in range(len(reminder_list)):
            if datetime.now() < datetime.strptime(reminder_list[i][1], self.datetime_format):
                reminder_list_clean.append(reminder_list[i])

        print(*reminder_list_clean, sep = "\n")
        while True:
            if len(reminder_list_clean) == 0:
                break

            # Checking every 10 seconds.
            time.sleep(10)

            # TODO: only read lines that is in the future.
            for i in range(len(reminder_list_clean)):
                if datetime.now().replace(second=0, microsecond=0) == datetime.strptime(reminder_list_clean[i][1], self.datetime_format):

                    # Opening up browser to let you know.
                    webbrowser.open('https://www.google.com/search?client=ubuntu&channel=fs&q={0}&ie=utf-8&oe=utf-8'.format(reminder_list_clean[i][0]))

                    # Popping
                    reminder_list_clean.pop(i)
                    print("There are {0} more things to do !".format(len(reminder_list_clean)))

if __name__ == "__main__":
    x = reminder()
    x.remind_me()
