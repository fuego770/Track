from os import system,popen,rename, remove
from time import ctime,sleep
import csv
import matplotlib.pyplot as plt
from sys import exit

uptime=''
def uptime_update():
    global uptime
    uptime=popen('uptime').read().lstrip().split()[2].rstrip(',').split(':')

#assign_time variables:
focus_time=[]
task_time={}
today=''

#lock variable:
failsafe=''

#set_usage_time variables:
overtime=[]
limit_time=0
limit_time=0

#input_for_graph variables:
def_safe=''
def_mediocre=''

#start() variables:
menu='''
Version:1.0.1

    }----------------------MENU----------------------{
    {1}---Create Not-to-use Time
    {2}---PC Uptime
    {3}---Set Usage Time
    (4)---Stats

    {11}--Help
    {0}---Exit
'''

stats_menu='''
    }----------------------MENU----------------------{
    {1}---Usage Stat
    {2}--Graph

    {11}--Back to Main menu
    {0}---Exit
'''

help_txt='''
Hello User, Welcome to Track, your laptop usage manager.

Track contains a lot features, namely:
    1) Create Not-to-use Time:
        Here you can create your to-do's and hence. The time you fix in here will
        render you laptop/pc locked for usage, but under emergency you uncol it,
        by pressing CTRL+C, and provide the reason.

    2) PC Uptime:
        This function gives you the time of how much your system has been in use
        in a singl run.

    3)Set usage Time:
        With the help of this function you can set the amount of time, you want
        to use your system on a single run.

    4)Stats:
        Contains two more options:
            (i) Usage Stats:
                With the help of this function you can monitor how long you used
                your system on a single run. If exceeded the function returns a
                message reading, "You have exceeded your limit" and the amount
                of time exceeded, else returns the time left before the limit is
                hit.

            (ii) Graphs:
                Give a pictorial representation in form of bar graphs with a lot
                information given about the system usage time of past seven days.

'''

menu='''
Version:1.0.1

    }----------------------MENU----------------------{
    {1}---Create Not-to-use Time
    {2}---PC Uptime
    {3}---Set Usage Time
    (4)---Stats

    {11}--Help
    {0}---Exit
'''

stats_menu='''
    }----------------------MENU----------------------{
    {1}---Usage Stat
    {2}--Graph

    {11}--Back to Main menu
    {0}---Exit
'''

help_txt='''
Hello User, Welcome to Track, your laptop usage manager.

Track contains a lot features, namely:
    1) Create Not-to-use Time:
        Here you can create your to-do's and hence. The time you fix in here will
        render you laptop/pc locked for usage, but under emergency you uncol it,
        by pressing CTRL+C, and provide the reason.

    2) PC Uptime:
        This function gives you the time of how much your system has been in use
        in a singl run.

    3)Set usage Time:
        With the help of this function you can set the amount of time, you want
        to use your system on a single run.

    4)Stats:
        Contains two more options:
            (i) Usage Stats:
                With the help of this function you can monitor how long you used
                your system on a single run. If exceeded the function returns a
                message reading, "You have exceeded your limit" and the amount
                of time exceeded, else returns the time left before the limit is
                hit.

            (ii) Graphs:
                Give a pictorial representation in form of bar graphs with a lot
                information given about the system usage time of past seven days.

'''

class Functionalities:
    '''
        Part 1:
        Part 1 consistes of functions that are used to create tasks and monitor focus time
    '''

    def task(self):
        '''
            Function to create the tasks file which contains the working or foxusing hour.
        '''

        print('Create your study time here in 24 hour format. Press enter key twice to end the input.')
        print('For eg: 17 to 1930.\n')

        lines=[]
        while True:
            line=input()
            if line:
                lines.append(line.rstrip(' '))
            else:
                break

        with open('tasks','w') as file:
            file.write(ctime()[:10]+'\n')
            for i in lines:
                file.write(i)

        print('Please check the file.')
        sleep(3)
        system('nano tasks')


    def assign_time(self):
        '''
            Function to to extract data and create the data from tasks file.
        '''

        global focus_time
        global task_time
        global today

        with open('tasks','r') as file:
            tasks=file.readlines()
            today=tasks[0].rstrip('\n')

            for task in range(len(tasks)):
                if task!=0:
                    data=tasks[task].rstrip('\n').split()
                    for i in data:
                        if i.isnumeric():
                            if len(i)==2:
                                focus_time.append(int(i+'00'))
                            else:
                                focus_time.append(int(i))

        temp=1
        try:
            for i in range(0,len(focus_time),2):
                task_time[temp]=[focus_time[i],focus_time[i+1]]
                temp+=1
        except:
            pass


    def lock(self):
        '''
            Function to to lock the the system if the time comes between the focus or study time.
        '''

        global task_time
        global today
        global failsafe

        temp=1
        current_time=int(ctime()[11:13]+ctime()[14:16])

        while True:

            if ctime()[:10]==today:

                try:

                    if current_time<=task_time[temp][1]:
                        if current_time>=task_time[temp][0]:
                            print('You are trying to use your laptop during the scheduled time. press CTRL+c to enter failsafe.')
                            sleep(1)
                            system('xdotool key ctrl+alt+l')
                            sleep(1)
                            self.lock()

                        else:
                            temp+=1
                            self.start()

                    else:
                        self.start()

                except KeyboardInterrupt:
                    print('Entering failsafe:')
                    choice=input('''
1) Go To Menu:
2) Exit

Choose between 1 or 2: ''')

                    if choice=='1':
                        self.start()

                    elif choice=='2':
                        exit()

                    else:
                        print('Wrong input, going to menu\n')
                        self.start()

                else:
                    temp+=1

            else:
                self.start()


    '''
        End of part one
    '''

    '''
        Part 2:
            These functionsions are for the monitoring of the usage of the system and shoe them with visual representation
    '''

    def pc_running_time(self):
        '''
            Function to print the time the system has been in use.
        '''

        uptime_update()

        if len(uptime)==1:
            print('You have used your system for {} minutes.'.format(uptime[0]))

        elif len(uptime)==2:
            print('You have used your system for {} hours and {} minutes.'.format(uptime[0],uptime[1]))

        elif len(uptime)==3:
            print('You have used your system for {} days, {} hours and {} minutes.'.format(uptime[0],uptime[1],uptime[2]))


    def set_usage_time(self):
        '''
            Function to create,monitor & limit the usage time.
        '''

        global limit_time
        global uptime
        global overtime

        print('Set your if usage time(daily usage of the system): ')
        while True:
            hours=input('Enter the number of hours(if no input just press enter): ')
            mins=input('Enter the number of minutes(if no input just press enter): ')

            if mins=='':
                mins='00'

            if hours!='':
                if int(hours)>23 or (int(mins)<0 or int(mins)>60):
                    print('Invalind input, retry: ')
                else:
                    break

            elif hours=='':
                if int(mins)<0 or int(mins)>60:
                    print('Invalid input, retry: ')
                else:
                    break

        if hours!='':
            if len(hours)==1:
                if len(mins)==1:
                    limit_time=int('0'+hours+'0'+mins)
                else:
                    limit_time=int('0'+hours+mins)
            else:
                if len(mins)==1:
                    limit_time=int(hours+'0'+mins)
                else:
                    limit_time=int(hours+mins)

        else:
            if len(mins)==1:
                limit_time=int('0'+mins)
            else:
                limit_time=int(mins)


    def stats_pc_uptime(self):
        uptime_update()
        global overtime
        global limit_time

        total_time=''
        for i in uptime:
            total_time+=i
        total_time=int(total_time)

        if limit_time>=total_time:
            overtime.append(False)
        else:
            overtime.append(True)

        if overtime[0]:
            total_overtime=total_time-limit_time
            overtime.append(total_overtime)
        else:
            total_overtime=total_time-limit_time
            overtime.append(total_overtime)

        if overtime[0]==True:
            exceded_time=overtime[1]
            if exceded_time>59:
                hours=exceded_time//60
                mins=exceded_time%60
                exceded_time='%d:%d' % (hours,mins)

                t=exceded_time.split(':')
                print('You have exceeded the usage limit by {} hours & {} minutes.'.format(t[0],t[1]))

            else:
                print('You have exceeded the usage limit by {} minutes.'.format(exceded_time))

        else:
            left_time=overtime[1]*-1
            if left_time>59:
                hours=left_time//60
                mins=left_time%60
                left_time='%d:%d' % (hours,mins)

                t=left_time.split(':')
                print('You have {} hours & {} minutes still left before running out of time.'.format(t[0],t[1]))

            else:
                print('You have {} minutes still left before running out of time.'.format(left_time))


    def day_manager(self):
        '''
            Function to manage file for graphs
        '''

        uptime_update()
        days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun','Mon']

        time_data=''
        for i in uptime:
            time_data+=i

        if len(time_data)>2:
            if len(time_data)==3:
                time_data=time_data[:1]+':'+time_data[1:]
            elif len(time_data)==4:
                time_data=time_data[:2]+':'+time_data[2:]

        with open('graph.csv','r+') as file:
            writer=csv.writer(file)
            reader=csv.reader(file)

            l=[]
            for i in reader:
                l.append(i)

            day=int(l[0][0])

            if day==0:
                    with open('graph_new.csv','w+') as file_new:
                        writer_new=csv.writer(file_new)
                        day+=1
                        writer_new.writerow([day])
                        writer_new.writerow([ctime()[:3],time_data])

                        remove('graph.csv')
                        rename('graph_new.csv','graph.csv')

            elif day>0 and day<7:
                last_day=l[-1][0]
                if ctime()[:3]==days[days.index(last_day)+1]:
                    l.append([ctime()[:3],time_data])

                    with open('graph_new.csv','w+') as file_new:
                        writer_new=csv.writer(file_new)
                        day+=1
                        writer_new.writerow([day])

                        for i in l:
                            if len(i)==2:
                                writer_new.writerow([i[0],i[1]])

                        remove('graph.csv')
                        rename('graph_new.csv','graph.csv')


            elif day==7:
                check=False
                for i in l:
                    if len(i)==2 and i[0]==ctime()[:3] and i[1]==time_data:
                        l[l.index(i)]=[ctime()[:3],time_data]
                        check=True

                if check:
                    with open('graph_new.csv','w+') as file_new:
                        writer_new=csv.writer(file_new)
                        writer_new.writerow([day])

                        for i in l:
                            if len(i)==2:
                                writer_new.writerow([i[0],i[1]])

                        remove('graph.csv')
                        rename('graph_new.csv','graph.csv')


    def input_for_graph(self):
        global def_safe
        global def_mediocre
        def_safe=input('Enter your safe usage value for using(in format HH:MM): ')
        def_mediocre=input('Enter your mediocre value for using(in format HH:MM): ')


    def graph(self):
        global def_safe
        global def_mediocre

        with open('graph.csv','r+') as file:
            reader=csv.reader(file)
            data=[]
            for i in reader:
                data.append(i)

            time=[]
            for i in data:
                if len(i)==2:
                    time_used=i[1].split(':')
                    time.append(int(time_used[0]+time_used[1]))

            days=[]
            for i in data:
                if len(i)==2:
                    days.append(i[0])

            barlist=plt.bar(days,time)

            #coloring the graphs
            green='#31F704'
            max_red='#800000'
            orange='#E55A0A'
            yellow='#FFFF00'

            safe_limit=int((def_safe.split(':')[0])+(def_safe.split(':')[1]))
            mediocre_limit=int((def_mediocre.split(':')[0])+(def_mediocre.split(':')[1]))
            safe_values=[i for i in time if i<=safe_limit]
            mediocre=[i for i in time if i>safe_limit and i<=mediocre_limit]
            over=[i for i in time if i>mediocre_limit]

            for i in safe_values:
                barlist[time.index(i)].set_color(green)
            for i in mediocre:
                barlist[time.index(i)].set_color(yellow)
            for i in over:
                barlist[time.index(i)].set_color(orange)
            barlist[time.index(max(i for i in time))].set_color(max_red)

            plt.title('DAILY USAGE')
            plt.xlabel('''Day

            The X axis represents the day of the week and Y axis represents the total time in the format
            700 meaning 7 hours and 00 minutes. The last 2 digits represents the minutes and the next ones
            represents the hours.
            ''')
            plt.ylabel('''Safe ---> Green, Yellow ---> Mediocre, Orange ---> Over, Dark-red ---> Maximum


            Time''')

            mng = plt.get_current_fig_manager()
            mng.resize(*mng.window.maxsize())
            plt.show()

    def start(self):
        global limit_time
        global def_safe
        global menu
        global stats_menu
        global overtime

        while True:
            print(menu)
            choice=input('Enter your choice: ')

            if choice.isdigit() and (int(choice) in [1,2,3,4,11,0]):
                choice=int(choice)

                if choice==1:
                    self.task()
                elif choice==2:
                    self.pc_running_time()
                elif choice==3:
                    self.set_usage_time()

                elif choice==4:
                    system('clear')
                    print(stats_menu)
                    choice_stats=input('Please choose an option: ')

                    if choice_stats.isdigit() and (int(choice_stats) in [1,2,11,0]):
                        if choice_stats=='1':
                            if not limit_time:
                                print('Go to Set UsageTime to create usage time settings first.')
                                self.start()
                            else:
                                self.stats_pc_uptime()

                        elif choice_stats=='2':
                                self.day_manager()

                                if not def_safe:
                                    print('Create settings for graphs first: ')
                                    self.input_for_graph()
                                    self.graph()

                                else:
                                    self.day_manager()
                                    while True:
                                        settings_choice=input('Do you want to continue with old settings(y/n): ')
                                        if settings_choice not in ['y','n']:
                                            print('Input should be between y or n, retry.')

                                        else:
                                            if settings_choice=='y':
                                                self.day_manager()
                                                self.graph()
                                            else:
                                                self.day_manager()
                                                self.input_for_graph()
                                                self.graph()

                        elif choice_stats=='11':
                            self.start()

                        elif choice_stats=='0':
                            exit()

                elif choice==11:
                    print(help_txt)

                elif choice==0:
                    exit()

            else:
                print('Choose again')
                self.start()

#Program over
#Program Version 1.0.1
