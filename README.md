# Flight Price Prediction with Flask

This project is a web application built with Flask to predict flight prices based on user inputs. It leverages a machine learning model trained on historical flight data, allowing users to enter flight details and get a predicted price for their journey.

## Project Structure

```plaintext
├── data/                     # Folder containing raw data files used for training
├── model training.ipynb      # Jupyter Notebook for model training and evaluation
├── templates/                # HTML templates for the web app
│   ├── home.html             # Homepage of the application
│   ├── layout.html           # Base template for consistent styling
│   └── predict.html          # Form page for user input and displaying predictions
├── app.py                    # Main Flask application file
├── form.py                   # WTForms classes for managing user input
├── model.joblib              # Serialized machine learning model
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Project Files

- **data/**: Contains raw data files used for training the machine learning model. Ensure you add your dataset here before training.
- **model training.ipynb**: Jupyter notebook used to preprocess the data, train the machine learning model, and save it as a `.joblib` file.
- **templates/**: HTML templates for the web application interface.
  - `home.html`: Main landing page.
  - `layout.html`: Base template to manage consistent styling.
  - `predict.html`: Form page where users input flight details for price prediction.
- **app.py**: Flask application file that serves the web app, loads the model, and handles user requests.
- **form.py**: Contains the form definitions for WTForms, managing input fields and validation for the prediction form.
- **model.joblib**: Serialized machine learning model that the application loads to make predictions.
- **requirements.txt**: List of required Python packages for the application. Run `pip install -r requirements.txt` to install dependencies.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   `git clone <repository-url>
   cd flight-price-prediction`

2. **Install dependencies**: 
  Make sure you have Python installed, then run:
  `pip install -r requirements.txt`

3. **Train the Model (optional)**: 
  If you want to retrain the model, open `model training-2.ipynb` and follow the steps to preprocess data, train the model, and save it as `model.joblib`.

4. **Run the Application**: 
  Start the Flask application by running:
  `python app.py`

5. **Access the Web Application**: Open a web browser and go to `http://127.0.0.1:5000` to interact with the flight price prediction form.

## Usage

* Go to the homepage to start a new prediction.
* Enter the flight details (airline, date, source, destination, etc.).
* Click Predict to get a price estimate for the entered details.
Model
* The machine learning model was trained on historical flight data to predict the flight price based on input parameters. The model is saved as `model.joblib` and loaded in `app.py` for inference.

## Acknowledgements
This project uses the following tools and frameworks:

* Flask for the web application
* WTForms for managing form input and validation
* Joblib for saving and loading the machine learning model
* Scikit-Learn for building and training the model

## Live Demo

The application is deployed on Render. You can access it here:

[Flight Price Prediction App](https://flight-price-prediction-using-flask-1.onrender.com/)
