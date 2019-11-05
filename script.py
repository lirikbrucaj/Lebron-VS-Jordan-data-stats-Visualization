import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

jordan  = pd.read_csv('jordan_career.csv')
lebron = pd.read_csv('lebron_career.csv')
print(jordan.head())
lebronDiv = [" avg field goal %", "avg three point %", "avg free throw %", "avg assists", "avg steals", "avg blocks", "avg turnovers", "avg points"]
jordanDiv = ["field goal %", "three point %", "free throw %", "assist", "steal", "block", "turnover", "points"]
lebronNum = [lebron["fgp"].mean(),lebron["threep"].mean(),lebron["ftp"].mean(),lebron["ast"].mean(),lebron["stl"].mean(),lebron["blk"].mean(),lebron["tov"].mean(),lebron["pts"].mean()]
jordanNum = [jordan["fgp"].mean(),jordan["threep"].mean(),jordan["ftp"].mean(),jordan["ast"].mean(),jordan["stl"].mean(),jordan["blk"].mean(),jordan["tov"].mean(),jordan["pts"].mean()]

index = np.arange(len(lebronDiv))
width = .30
plt.barh(index, lebronNum, width, color = 'red', label = 'Lebron')
plt.barh(index + width, jordanNum,width, color = 'blue', label = 'Jordan')

plt.title("Lebron VS Jordan Career Stats")
plt.xlabel("Numbers")
plt.ylabel("Stats")
plt.yticks(index+width/2, lebronDiv)
plt.legend(loc = "best")
plt.show()

