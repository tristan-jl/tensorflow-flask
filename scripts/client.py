import pandas as pd
import requests

df = pd.read_csv("data/test.csv").head(5).fillna("")

for i in df.to_dict("records"):
    r = requests.post("http://127.0.0.1:8080/predict", json=i)
    r.raise_for_status()
    print(r.json())

r = requests.post("http://127.0.0.1:8080/predict_batch", json=df.to_dict("records"))
r.raise_for_status()
print(r.json())
