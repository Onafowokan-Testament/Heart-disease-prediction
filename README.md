# Heart Disease Prediction with FastAPI and Machine Learning ❤️

Welcome to the **Heart Disease Prediction** project! This project uses machine learning to predict the likelihood of heart disease based on patient data. The model is integrated into a FastAPI web application, allowing users to input their data and receive predictions in real-time. The project uses **scikit-learn** for machine learning and **FastAPI** for building the web interface.

---

## Features

- **Real-Time Prediction**: Users can input their health data and receive instant predictions.
- **Machine Learning Model**: Uses a Logistic Regression model trained on heart disease data.
- **Data Preprocessing**: Includes scaling and encoding of categorical variables.
- **Interactive Web Interface**: Built with FastAPI and Jinja2 templates for a seamless user experience.

---

## How It Works

1. **User Input**: Users input their health data (e.g., age, blood pressure, cholesterol, etc.) via a web form.
2. **Data Preprocessing**: The input data is scaled and encoded to match the format used during model training.
3. **Prediction**: The preprocessed data is passed to the machine learning model, which predicts the likelihood of heart disease.
4. **Result Display**: The prediction result is displayed to the user on the web interface.

---

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- FastAPI
- scikit-learn
- pandas
- numpy
- uvicorn

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**:
   ```bash
   uvicorn app:app --reload
   ```

4. **Open the application**:
   Visit `http://localhost:8000` in your browser.

---

## Usage

1. Open the web application in your browser.
2. Fill out the form with your health data.
3. Click the "Predict" button to receive the prediction result.

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [scikit-learn](https://scikit-learn.org/) for the machine learning model.
- [pandas](https://pandas.pydata.org/) for data manipulation.
- [numpy](https://numpy.org/) for numerical computations.

---

Predict heart disease risk with ease using this Heart Disease Prediction project! 🚀❤️
