
# -*- coding: utf-8 -*-
import csv
import datetime

with open('full_export.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')

    chosen_date = \
        input('''Choose a date to show arrivals from in September (eg. 13/09/2014)
NB. format is important!
''')

    for row in reader:
        if chosen_date in row[0]:

# logic to remove the time in hours from the expected arrival date

            epected_date_time = row[0]
            (expected_date, epected_time) = epected_date_time.split(' ')

# nhr campus

            if 'Davidson' in row[6]:


                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - nhr_campus output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Lang' in row[6]:


                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - nhr_campus output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Temple' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - nhr_campus output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Fynden' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - nhr_campus output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Thorne' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - nhr_campus output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Vernon' in row[6]:

# city halls

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - city_halls output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Oaten' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - city_halls output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Holmes Court' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - city_halls output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'College Court' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - city_halls output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Wincheap' in row[6]:

# c'bury headlease

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Oxford' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Sturry' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'St Peters' in row[6]:

                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Hudson' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Nunnery' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Norman' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Starle' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Regency' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'St Martins' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Guildford' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'York' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Mary Green' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Craddock' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Martyrs' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Keyworth' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Anne Green' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Longport' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Crowthers' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Park Cottages' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Glenside' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - cbury_headlease output.csv'
                         % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif '(' in row[6]:

# homestay



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - homestay output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Lanfranc' in row[6]:

# lanfranc



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - lanfranc output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Amandos' in row[6]:

# parham rd



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - parham_rd output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Colton' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - parham_rd output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Rigby' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - parham_rd output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Freeman' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - parham_rd output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Hamill' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - parham_rd output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Parham' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - parham_rd output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Sargeants' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - parham_rd output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Benson' in row[6]:

# pin hill



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - pin_hill output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Carey' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - pin_hill output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Coggan' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - pin_hill output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Runcie' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - pin_hill output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Ramsey' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - pin_hill output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'St George' in row[6]:

# st georges



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - st_georges output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Havelock' in row[6]:

# university houses



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - owned_houses output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'North Holmes' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - owned_houses output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Monastery' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - owned_houses output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Priory' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - owned_houses output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Northwood' in row[6]:

# broadstairs



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - broadstairs output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Grange' in row[6]:

# broadstairs headlease houses



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - bstairs_headleased output.csv'
                          % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Queens' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - bstairs_headleased output.csv'
                          % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Dundonald' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - bstairs_headleased output.csv'
                          % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Codrington' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - bstairs_headleased output.csv'
                          % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Albion' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - bstairs_headleased output.csv'
                          % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Bellevue' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - bstairs_headleased output.csv'
                          % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            elif 'Richmond' in row[6]:



                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = \
                    open('generated on %s - bstairs_headleased output.csv'
                          % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()
            else:

# unsorted remainder


                timestamp = \
                    datetime.datetime.now().strftime('%d.%m.%Y-%H%M')
                file = open('generated on %s - unsorted output.csv'
                            % timestamp, 'a')

                # output to file in new order

                file.write(row[1] + ',' + row[2] + ',' + row[4] + ','
                           + row[6] + ',' + row[5] + ','
                           + expected_date + '\n')
                file.close()


