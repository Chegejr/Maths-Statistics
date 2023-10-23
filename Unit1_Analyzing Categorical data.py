# In this unit we are going to dig deep in categorical data
import pandas as pd
data = {
    "":{
        "Boardroom":120,
        "Bassford":60,
        "Fernery":200
    },
     "Room name":{
        "Boardroom":120,
        "Bassford":60,
        "Fernery":200
    }
}
x= pd.DataFrame(data)
print(x)