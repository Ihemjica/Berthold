#!/usr/bin/python3
import requests
import json
import time

GAMEODDS={}

Leagues = [7076, 11113, 12821, 12829, 13521, 13709, 27687, 88637, 96463, 104509, 105759, 108319, 109313, 110163, 118587, 118593, 118663, 119235, 119237, 119577, 127733, 127759, 176125, 225733, 828065, 1841614, 1987921, 2018750, 2159744, 2187849]

TodaysLeagues = []
hr = 6

f = open("Games.txt", "w")

#curl 'https://astekbet.com/LineFeed/GetChampsZip?sport=1&lng=en&tf=1440&tz=1&country=132&partner=75&virtualSports=true'|jq|grep LI|grep -oP "\d+"

LOL = requests.get("https://1xbet.ng/LineFeed/GetChampsZip?sport=1&lng=en&tf={}&tz=1&country=132&partner=75&virtualSports=true".format(hr*60))

LOLs = json.loads(LOL.text)


#List of Leagues playing today
for i in LOLs['Value']:
#   if int(i['LI']) in Leagues:
      TodaysLeagues.append(i['LI'])
length=len(TodaysLeagues)
count=1

for i in TodaysLeagues:
#Getting GameIDs and Time
   s = requests.get("https://1xbet.ng/LineFeed/GetChampZip?champ={}&lng=en&tf={}&virtualSports=true".format(i,hr*60))
   t = json.loads(s.text)
   #Sorting through odds for each gameiD(CI)
   try:
    print(str(count)  + ' of ' + str(length))
    count+=1
    for k in t['Value']['G']:
      u = requests.get("https://1xbet.ng/LineFeed/GetGameZip?id={}&GroupEvents=true&countevents=250".format(k['CI']))
      v = json.loads(u.text)
      #Add Time and Game ID to GAMEODDS
      #GAMEODDS.update(str(k['S'])+'_'+str(k['CI']):[])
      #Array with details about the best game; Handicap, Parameter, Type1, Type2, Odd1, Odd2
      PERF=[]
      LOWEST = 2
      for j in v['Value']['GE']:
         #Over and Under
         if j['G'] == 17:
            for l in range(len(j['E'][0])):
               LOW = (1/j['E'][0][l]['C'])+(1/j['E'][1][l]['C'])
               if j['E'][0][l]['C'] < 1.1 or j['E'][1][l]['C'] < 1.1:
                  continue
               if LOW < 1.03 and LOW < LOWEST:
         #        print(str(j['E'][0][l]['P'])+' '+str(j['E'][0][l]['C'])+' '+str(j['E'][1][l]['C']))
                  LOWEST = LOW
                  PERF=['OU', j['E'][0][l]['P'], j['E'][0][l]['T'], j['E'][1][l]['T'], j['E'][0][l]['C'], j['E'][1][l]['C'], LOW]
         #Asian Over and Under
#         if j['G'] == 99:
 #           for l in range(len(j['E'][0])):
  #            LOW = (1/j['E'][0][l]['C'])+(1/j['E'][1][l]['C'])
   #           if j['E'][0][l]['C'] < 1.1 or j['E'][1][l]['C'] < 1.1:
    #             continue
     #         if LOW < 1.03 and LOW < LOWEST:
         #        print(str(j['E'][0][l]['P'])+' '+str(j['E'][0][l]['C'])+' '+str(j['E'][1][l]['C']))
      #            LOWEST = LOW
       #           PERF=['AOU', j['E'][0][l]['P'], j['E'][0][l]['T'], j['E'][1][l]['T'], j['E'][0][l]['C'], j['E'][1][l]['C'], LOW]
         #Handicap
         if j['G'] == 2:
            for l in range(len(j['E'][0])):
               LOW = (1/j['E'][0][l]['C'])+(1/j['E'][1][l]['C'])
               if j['E'][0][l]['C'] < 1.1 or j['E'][1][l]['C'] < 1.1:
                  continue
               if LOW < 1.03 and LOW < LOWEST:
         #        print(str(j['E'][0][l]['P'])+' '+str(j['E'][0][l]['C'])+' '+str(j['E'][1][l]['C']))
         #        LOWEST = LOW
                  if len(j['E'][0][l]) == 2:
                     continue
         #           PERF=['H', 0, j['E'][0][l]['T'], j['E'][1][l]['T'], j['E'][0][l]['C'], j['E'][1][l]['C'], LOW]
         #           print(PERF)
         #           continue
                  if j['E'][0][l]['P']%1==0:
                     continue
                  PERF=['H', j['E'][0][l]['P'], j['E'][0][l]['T'], j['E'][1][l]['T'], j['E'][0][l]['C'], j['E'][1][l]['C'], LOW]
                  print(PERF)
                  LOWEST = LOW
         #         continue
         #Asian Handicap
#         if j['G'] == 2854:
 #           for l in range(len(j['E'][0])):
  #             LOW = (1/j['E'][0][l]['C'])+(1/j['E'][1][l]['C'])
   #            if j['E'][0][l]['C'] < 1.1 or j['E'][1][l]['C'] < 1.1:
    #              continue
     #          if LOW < 1.03 and LOW < LOWEST:
         #        print(str(j['E'][0][l]['P'])+' '+str(j['E'][0][l]['C'])+' '+str(j['E'][1][l]['C']))
      #            LOWEST = LOW
       #           PERF=['AH', j['E'][0][l]['P'], j['E'][0][l]['T'], j['E'][1][l]['T'], j['E'][0][l]['C'], j['E'][1][l]['C'], LOW]
      if LOWEST != 2:
         GAMEODDS.update({str(k['S'])+'_'+str(k['CI']):PERF})
   except:
    continue

#Get sorted list of time for games
Time = []

for i in GAMEODDS.keys():
   Time.append(i.split('_')[0])

Time = sorted(set(Time))

#Final list of games with lowest margin for each time
GAMEODDS2 = {}

for i in Time:
   LOWEST=2
   for j in GAMEODDS.keys():
      if i in j and GAMEODDS[j][-1] < LOWEST:
         GG = j
         LOWEST = GAMEODDS[j][-1]
   GAMEODDS2.update({GG:GAMEODDS[GG]})

#Human clickable links
for i in GAMEODDS2.keys():
 try:
   #GameID
   GameID=i.split('_')[1]
   u = requests.get("https://1xbet.ng/LineFeed/GetGameZip?id="+GameID+"&GroupEvents=true&countevents=250&lng=en")
   v = json.loads(u.text)
   f.write(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(int(i.split('_')[0]))))
   print(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(int(i.split('_')[0]))))
   link="https://1xbet.ng/en/line/Football/"+str(v['Value']['LI'])+"-"+v['Value']['L'].replace(' ','-').replace('.','')+"/"+str(v['Value']['CI'])+"-"+v['Value']['O1'].replace(' ','-').replace('.','')+"-"+v['Value']['O2'].replace(' ','-').replace('.','')+"/"
   print(link)
   f.write("\n"+link+"\n")
   if GAMEODDS2[i][0] == 'H':
      print("Handicap " + str(GAMEODDS2[i][1]) + " " + str(GAMEODDS2[i][4]) + " " + str(GAMEODDS2[i][5]))
      f.write("Handicap," + str(GAMEODDS2[i][1]) + "," + str(GAMEODDS2[i][4]) + "," + str(GAMEODDS2[i][5]))
   if GAMEODDS2[i][0] == 'OU':
      print("Over and Under " + str(GAMEODDS2[i][1]) + " " + str(GAMEODDS2[i][4]) + " " + str(GAMEODDS2[i][5]))
      f.write("Over and Under," + str(GAMEODDS2[i][1]) + "," + str(GAMEODDS2[i][4]) + "," + str(GAMEODDS2[i][5]))
   if GAMEODDS2[i][0] == 'AH':
      f.write("Asian Handicap," + str(GAMEODDS2[i][1]) + "," + str(GAMEODDS2[i][4]) + "," + str(GAMEODDS2[i][5]))
      print("Asian Handicap " + str(GAMEODDS2[i][1]) + " " + str(GAMEODDS2[i][4]) + " " + str(GAMEODDS2[i][5]))
   if GAMEODDS2[i][0] == 'AOU':
      print("Asian Over and Under " + str(GAMEODDS2[i][1]) + " " + str(GAMEODDS2[i][4]) + " " + str(GAMEODDS2[i][5]))
      f.write("Asian Over and Under," + str(GAMEODDS2[i][1]) + "," + str(GAMEODDS2[i][4]) + "," + str(GAMEODDS2[i][5]))
   f.write("\n")
   print('')
   print('')
   print('')
 except:
   continue
