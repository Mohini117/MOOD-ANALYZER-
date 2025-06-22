# main.py
import pandas as pd
import joblib
from flask import Flask, render_template, request
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

model = joblib.load("final_model_pipeline.pkl")  # your trained model

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    message = None
    if form.validate_on_submit():
        # Construct DataFrame with exact expected column names
        x_new = pd.DataFrame([{
            "Age": form.age.data,
            "Gender": form.gender.data,
            "Platform": form.platform.data,
            "Daily_Usage_Time (minutes)": form.daily_usage_time.data,
            "Posts_Per_Day": form.post_per_day.data,
            "Likes_Received_Per_Day": form.likes_per_day.data,
            "Comments_Received_Per_Day": form.comments_received.data,
            "Messages_Sent_Per_Day": form.messages_sent.data
        }])

        prediction = model.predict(x_new)[0]
        message = f"SO HOW'S YOUR FEELING AFTER PROCRASTINATION? 😅 → {prediction}"
        # print("PREDICTION:", prediction) # shows in terminal
    else:
        if request.method == "POST":
            print("Form errors:", form.errors)
            message = "⚠️ Please provide valid input details!"

    return render_template("predict.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)
