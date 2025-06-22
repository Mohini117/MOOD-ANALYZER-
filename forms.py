# forms.py
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

# Load data
train_df = pd.read_csv("Data_social_media/train.csv")
# val = pd.read_csv("Data_social_media/val.csv")
X_data = train_df.drop(columns=["Dominant_Emotion","User_ID"])

class InputForm(FlaskForm):
    age = SelectField(
        label="Age",
        choices=[(age, age) for age in sorted(X_data["Age"].dropna().unique())],
        validators=[DataRequired()]
    )
    gender = SelectField(
        label="Gender",
        choices=[(g, g) for g in X_data["Gender"].dropna().unique()],
        validators=[DataRequired()]
    )
    platform = SelectField(
        label="Platform",
        choices=[(p, p) for p in X_data["Platform"].dropna().unique()],
        validators=[DataRequired()]
    )
    daily_usage_time = IntegerField(
        label="Daily_Usage_Time (minutes)",
        validators=[DataRequired()]
    )
    post_per_day = IntegerField(
        label="Posts_Per_Day",
        validators=[DataRequired()]
    )
    likes_per_day = IntegerField(
        label="Likes_Received_Per_Day",
        validators=[DataRequired()]
    )
    comments_received = IntegerField(
        label="Comments_Received_Per_Day",
        validators=[DataRequired()]
    )
    messages_sent = IntegerField(
        label="Messages_Sent_Per_Day",
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
