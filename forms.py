import pandas as pd
from flask_wtf import FlaskForm 
from wtforms import (
  SelectField,
  DateField,
  TimeField,
  IntegerField,
  SubmitField
)
from wtforms.validators import (
  DataRequired,
  NumberRange
)

# getting the data
train = pd.read_csv("Data/train.csv")
val = pd.read_csv("Data/val.csv")

X_data = pd.concat([train, val], axis=0).drop(columns="price")

class InputForm(FlaskForm):
  airline = SelectField(
    label="Airlines",
    choices=X_data.airline.unique().tolist(),
    validators=[DataRequired()]
  )

  date_of_journey = DateField(
    label="Date of Journey",
    validators=[DataRequired()]
  )

  source = SelectField(
    label="Source",
    choices=X_data.source.unique().tolist(),
    validators=[DataRequired()]
  )

  destination = SelectField(
    label="Destination",
    choices=X_data.destination.unique().tolist(),
    validators=[DataRequired()]
  )

  dep_time = TimeField(
    label="Departure time",
    validators=[DataRequired()]
  )

  arrival_time = TimeField(
    label="Arrival time",
    validators=[DataRequired()]
  )

  duration = IntegerField(
    label="Duration (in minutes)",
    validators=[DataRequired()]
  )

  total_stops = IntegerField(
    label="Total stops",
    default=0,
    validators=[NumberRange(min=0)],
  )

  additional_info = SelectField(
    label="Additional information",
    choices=X_data.additional_info.unique().tolist(),
    validators=[DataRequired()]
  )

  submit = SubmitField("Predict")