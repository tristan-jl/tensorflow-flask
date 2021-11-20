import pandas as pd
import tensorflow_decision_forests as tfdf
from flask import Flask
from flask import jsonify
from flask import request
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model("gb_model")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = tfdf.keras.pd_dataframe_to_tf_dataset(pd.DataFrame(data, index=[0]))
    prediction = model.predict(df)
    return jsonify({"survival": str(prediction.flatten()[0])})


if __name__ == "__main__":
    app.run(port=8080)
