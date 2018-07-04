my_d = {}
my_d['Nidhi'] = ['f',19]
my_d['Shivam'] = ['m',25]
my_d['Shourya'] = ['m', 16]
my_d['Ravi'] = ['m', 32]
my_d['Shreya'] = ['f', 14]
for key in my_d.keys():
    if my_d[key][0]=='m' and my_d[key][1]>18:
        print(key)
