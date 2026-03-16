import pandas as pd
from faker import Faker
import random

fake = Faker()

data = []

categories = ["Electronics","Books","Clothes","Home","Sports"]

for i in range(1000):

    data.append({
        "name": fake.word(),
        "price": random.uniform(10,500),
        "quantity": random.randint(1,100),
        "category": random.choice(categories)
    })

df = pd.DataFrame(data)

df.to_csv("csv_module/data.csv",index=False)

print("CSV created")