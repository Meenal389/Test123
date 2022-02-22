import csv
import pandas as pd
rows=[]
with open("total_stars.csv",'r') as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
stars_data = rows[1:]
headers[0] = 'Index'

# converting the data into SI Units
star_data = []
for s in stars_data:
    if s[3] != 'Mass': 
        s[3] = float(s[3].strip("\'"))*1.989e+30
    
    if s[4] != 'Radius':
        s[4] = float(s[4].strip("\'"))*6.957e+8
    star_data.append(s)

#calculate gravity
star_data_gravity = []
for s in star_data:
    if s[3] != 'Mass' and s[4] != 'Radius':
        gravity = (6.674e-11 * float(s[3]))/(float(s[4])*float(s[4]))
    s.append(gravity)
#appending the data in list
    star_data_gravity.append(s)

name = []
distance = []
mass = []
radius = []
gravity = []

for i in star_data_gravity:
    name.append(i[1])
    distance.append(i[2])
    mass.append(i[3])
    radius.append(i[4])
    gravity.append(i[5])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)
df.to_csv('Final.csv')