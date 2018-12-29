import csv
import matplotlib.pyplot as plt
list = []
names=[]
with open('reg.csv') as csvfile:
        nbalist = csv.reader(csvfile)
        g = 0
        for row in nbalist:
            #print row
            #print row
            # Account for the first two rows with bad data
            if g == 0 or g ==1:
                g = g + 1
                continue
            # Take out the bbref url part of the name (lol)
            nm =  row[1]
            nm = nm.split("\\")[0]
            tm = row[4]
            #print nm
            #print float(row[7])
            if float(row[7])*float(row[5])>200 and float(row[11])>1.5 and float(row[13])>0.25 and tm:
                #print "yes"
                with open('adv.csv') as csvfile2:
                        advlist = csv.reader(csvfile2)
                        g=0
                        for r in advlist:
                            if g == 0 or g ==1:
                                g = g + 1
                                continue
                            print r[18]
                            name2 = r[1]
                            name2 = name2.split("\\")[0]
                            team = r[4]
                            #print name2
                            if nm == name2 and float(r[26])>0 and float(r[18])<25:
                                #print name2
                                list.append([nm,r[26],row[13]])
                                names.append(nm)


colors = (0,0,0)
area = 0.5

# Some colors in an array
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.

for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

hfont = {'fontname':'Arial'}
x=[]
y=[]
names=[]
for l in list:
    x.append(l[1])
    y.append(l[2])
    names.append(l[0])
# plot!
plt.scatter(x, y, s=area, c=tableau20[0], alpha=0.5)
plt.title('dbpm', **hfont)
plt.xlabel('DBPM',  **hfont)
plt.ylabel('3P%', **hfont)
print x
#print names
print list
i=0
for player in list:
        print player
        name = names[i]
        #print name
        fname, lname = name.split(" ")
        init = fname[0]
        finalname = str(init) + ". " + lname
        string = '  '  + finalname
        plt.annotate(string, xy=(x[i], y[i]), arrowprops=dict(), size=10, **hfont)

        i = i + 1
            #if tm != "TOT":
            #    if tm:
plt.show()
