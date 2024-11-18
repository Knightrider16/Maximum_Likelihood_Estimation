import pandas as pd

def mle():
    data=pd.read_csv("data.csv")
    infected = len(data[data['infected'] == 1])
    non_infected = len(data[data['infected'] == 0])
    total = len(data)

    infected_prob=infected/total
    non_infected_prob=non_infected/total
    
    if infected_prob>non_infected_prob:
        print(f"The model predicts that likelihood of getting infected is more\nChance of getting infected={infected_prob}")
    else:
        print(f"The model predicts that likelihood of not getting infected is more\nChance of getting infected={infected_prob}")
mle() 