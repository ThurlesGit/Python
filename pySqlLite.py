import sqlite3
import time
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

DbFileIn = 'Bayer.db'
Query1 = "SELECT * FROM ResultData"
Query2 = "SELECT Meter_SerialNumber, Test_Time, Measurement_Value, PersonGUID, Test_Date FROM ResultData"


def DbConn(DbFile):
  conn = sqlite3.connect(DbFile)
  return conn

def DbQuery(conn, query):
  c = conn.cursor()
  c.execute(query)
  all = c.fetchall()
  return all

def OutputRes(HeaderStr, OutStr, OutList):
                      #*HeaderStr is unpacked array
  print(OutStr.format(*HeaderStr))
  Count = 0
  for row in data:
    Count += 1
    #*row is unpacked array
    print(OutStr.format(Count, *row))

  print ("\nOperation outputted {} elements successfully,".format(len(OutList)))

def GenPlots(OutList):
  labels = '0-1', '1-2', '2-3', '3-4', '4-5','5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '21-'
  sizes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  #explode = (0, 0.1, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

  for row in data:
    x = int(row[2])/1
    sizes[int(x)] += 1

  FigStr = "Fig 2: Nice Bar Chart"
  PlotBarChart(labels, sizes,  FigStr)

  FigStr = "Fig 1: Nice Pie Chart"
  PlotPie(labels, sizes,  FigStr)
  


def PlotPieExplode(Labels, Sizes, Explode, FigTitle):
  FigStr, ax1 = plt.subplots()
  ax1.pie(Sizes, explode=Explode, labels=Labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


def PlotPie(Labels, Sizes, FigTitle):
  FigStr, ax1 = plt.subplots(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
  ax1.pie(Sizes, labels=Labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.title(FigTitle , position=(0.1,1),bbox={'facecolor':'0.8', 'pad':5})
  plt.text(-1.3,-1.1, "Pie Bugger", bbox=dict(facecolor='white', alpha=0.5), fontsize=14)  
  plt.tight_layout()

def PlotBarChart(Labels, Sizes, FigTitle):

  y_pos = np.arange(len(Labels))
  fig, ax = plt.subplots(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
  ax.bar(y_pos, Sizes, align='center', alpha=.5)
  plt.xticks(y_pos, Labels)
  plt.ylabel('Count')
  plt.xlabel('Range')
  plt.title(FigTitle)
  plt.text(-4.8,-25.3, "Bar Bugger", bbox=dict(facecolor='white', alpha=0.5), fontsize=14)  

if __name__=="__main__":

  conn = DbConn(DbFileIn)
  data = DbQuery(conn,Query2)
  
  #Wtite to screen
  Header = ["Number", "Meter_SerialNumber", "Test_Time", "Measurement_Value", "   PersonGUID", "   Test_Date"]
  # Format output text
  Out = "{:6} {:20} {:10} {:18} {:20} {:20}"
  OutputRes(Header, Out, data)
  
  # Generate a pie chart
  GenPlots(data)
  plt.show()

  conn.close()
