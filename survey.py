import datetime
import webbrowser

FULL_NAME = ['ANAKIN TROTTER', 'ZHENDA HU']
UCLA_ID = ['805809257', '405734589']
DATE_AND_TIME = datetime.datetime.now().strftime('%#m/%e/%Y') + ' 9:21 AM'
NEXT_DAY = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%#m/%e/%Y')

for i in range(len(FULL_NAME)):
    html_file = open('orig.html', encoding='utf8')
    html = html_file.readlines()

    html_out = open('copy' + str(i) + '.html', 'w', encoding='utf8')

    for line in html:
        if 'INSERT_FULL_NAME' in line:
            html_out.write('style="color:black">' + FULL_NAME[i] + '&nbsp;</span></b><br>')
        elif 'INSERT_UCLA_ID' in line:
            html_out.write('<b><span style="color:black">' + UCLA_ID[i] + '</span></b>&nbsp;<br>')
        elif 'INSERT_DATE_AND_TIME_2' in line:
            html_out.write('time:&nbsp;'+ DATE_AND_TIME)
        elif 'INSERT_DATE_AND_TIME' in line:
            html_out.write('on&nbsp;<b>' + DATE_AND_TIME + '</b>.<br>')
        elif 'INSERT_NEXT_DAY' in line:
            html_out.write('style="color:black">' + NEXT_DAY + '&nbsp;4:00AM.</span></b></span></span></span><br>')
        else:
            html_out.write(line)

    html_file.close()
    html_out.close()

    webbrowser.open_new_tab('copy' + str(i) + '.html')

