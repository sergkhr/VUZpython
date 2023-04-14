import csv
import datetime
import requests
import matplotlib.pyplot as plt

checks_url = "https://raw.githubusercontent.com/true-grue/kispython/main/data/checks.csv"
messages_url = "https://raw.githubusercontent.com/true-grue/kispython/main/data/messages.csv"
statuses_url = "https://raw.githubusercontent.com/true-grue/kispython/main/data/statuses.csv"


def get_csv(url):
    r = requests.get(url)
    return r.text


def csv_to_list(inp):
    reader = csv.reader(inp.splitlines(), delimiter=',')
    return list(reader)


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


# id, task, variant, group, time
messages = csv_to_list(get_csv(messages_url))

# id, message_id, time, status
checks = csv_to_list(get_csv(checks_url))

# task, variant, group, time, status, achievements
statuses = csv_to_list(get_csv(statuses_url))


def draw_activity_by_days_graph():
    # get the number of messages sent by the student per day
    messages_per_day = [0] * 7
    for message in messages:
        messages_per_day[parse_time(message[4]).weekday()] += 1

    # draw the graph
    plt.xticks(range(7), range(1, 8))
    plt.bar(range(7), messages_per_day, label="messages")
    plt.legend()
    plt.show()


def draw_activity_by_hours_graph():
    # get the number of messages sent by the student per hour
    messages_per_hour = [0] * 24
    for message in messages:
        messages_per_hour[parse_time(message[4]).hour] += 1

    # draw the graph
    plt.xticks(range(24), range(24))
    plt.bar(range(24), messages_per_hour, label="messages")
    plt.legend()
    plt.show()


# draw_activity_by_days_graph()
draw_activity_by_hours_graph()