from datetime import datetime, timedelta
import pandas
import matplotlib.pyplot as plt
import sys

def make_plot(year, month, day, hour):
    data = dict()

    start_min = datetime(year, month, day, hour)
    plot_legend = str(start_min.year) + "년 " + str(start_min.month) + "월 " + str(start_min.day) + "일 " + str(start_min.hour) + "시 데이터" 

    for i in range(0, 60):
        time = start_min + timedelta(minutes=i)

        data[time] = 0

    f = open("blink_data.txt", 'r')

    lines = f.readlines()

    for line in lines:
        time_count_data = line.split(' ')

        time = time_count_data[0] + ' ' + time_count_data[1]
        count = time_count_data[2]

        time_parsed = datetime.strptime(time, '%Y/%m/%d %H:%M:%S')
        time_converted = datetime(time_parsed.year, time_parsed.month, time_parsed.day, time_parsed.hour, time_parsed.minute)

        if time_converted in data.keys():
            data[time_converted] += int(count)

    name = []
    value = []

    for datum in data:
        name.append('{:#02d}'.format(datum.minute) + ":" + '{:#02d}'.format(datum.second))
        value.append(data[datum])

    plt.rcParams['font.family'] = 'BM DoHyeon OTF'    
    df = pandas.DataFrame({'name':name, 'value':value})
    ax = df.plot(kind='bar', x='name', y='value', rot=0, title=plot_legend)
    ax.xaxis.set_visible(False)
    plt.rc('font', family='AppleMyungjo')
    ax.plot()
    
    plt.savefig('output.png')

def main(args):
    year = args[1] 
    month = args[2]
    day = args[3]
    hour = args[4]
    
    try:
        make_plot(int(year), int(month), int(day), int(hour))
    except:
        print('제대로 된 값을 입력하세요')

if __name__ == '__main__':
    main(sys.argv)