import pandas as pd
import tensorflow_decision_forests as tfdf

# kaggle titanic dataset
dataset = pd.read_csv("data/train.csv")
tf_dataset = tfdf.keras.pd_dataframe_to_tf_dataset(dataset, label="Survived")

model = tfdf.keras.GradientBoostedTreesModel()
model.fit(tf_dataset)

print(model.summary())
model.save("gb_model")
