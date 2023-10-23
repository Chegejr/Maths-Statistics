# In this unit we are going to dig deep in categorical data
# Below is a table containing data comparing rooms at a conference center.
import pandas as pd
data = {
    "Room Name":["Boardroom","Bassford","Fernery"],
    "Seating Capacity":[120,60,200],
    "Hire Cost":["$ 400","$ 300","$ 600"],
    "Projector":["Yes","Yes","Yes"],
    "Accessible":["Yes","Yes","Yes"]
}
rooms = pd.DataFrame(data)
print(rooms) # Output------>Below
"""
   Room Name  Seating Capacity Hire Cost Projector Accessible
0  Boardroom               120     $ 400       Yes        Yes
1   Bassford                60     $ 300       Yes        Yes
2    Fernery               200     $ 600       Yes        Yes
"""
# The "Individuals" in this data set are "Rooms at a conference center"
# This data set contains 4 variables, 2 of which are quantitative
# the 4 variables are [Seating Capacity,Hire Cost, Projector, Accessible]
# the two quantitative variables are :[Seating capacity and hire cost]
