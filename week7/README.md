## 🌸 Project Overview

This week's assignment focused on the deployment of a machine learning model. The objective was to take a trained model, build an interactive web application around it, and allow users to get real-time predictions through a simple user interface.

The project consists of two main parts:
1.  **Model Training:** A simple classification model was trained on the classic Iris dataset to predict the species of an iris flower based on its sepal and petal measurements. The trained model was then saved as a `model.pkl` file.
2.  **Web App Deployment:** A web application was built using the **Streamlit** framework. This app loads the pre-trained model and provides sliders for the user to input flower measurements. It then uses the model to predict the species and displays the result.

## 📚 Key Concepts & Techniques

This project demonstrates the end-to-end process of a simple machine learning application:

* **Model Training:** Using Scikit-learn to train a classifier (e.g., Logistic Regression or similar) on a standard dataset.
* **Model Serialization:** Saving the trained model object to a file using `pickle` so it can be loaded later for inference without retraining.
* **Web Application Development:** Using the `streamlit` library to create a user-friendly web interface with interactive widgets like sliders and buttons.
* **Model Deployment:** Loading the serialized model into the web app to make live predictions based on user input.

## 🛠️ Tools & Libraries Used

* **Language:** `Python`
* **Machine Learning:** `Scikit-learn`, `Pandas`
* **Model Serialization:** `pickle`
* **Web Framework:** `Streamlit`

## ⚙️ Project Structure & Workflow

The repository for this week contains the following key files:

* `train_model.py`: A script to load the Iris dataset, train a classification model, and save the trained model to `model.pkl`.
* `model.pkl`: The serialized, pre-trained machine learning model.
* `app.py`: The main Streamlit application script. It loads `model.pkl`, creates the UI, and handles user input to make predictions.

### Workflow:
1.  The `train_model.py` script is run once to generate the `model.pkl` file.
2.  The `app.py` script is run using the `streamlit run` command.
3.  The Streamlit app creates a web server, opens a browser window with the UI, and loads the `model.pkl` model into memory.
4.  The user interacts with the sliders to provide input features (sepal length, sepal width, etc.).
5.  On clicking the "Predict" button, the app sends these features to the loaded model.
6.  The model returns a prediction (the Iris species), which is then displayed to the user on the web page.

## 🚀 How to Run the Application

To run this project on your local machine, follow these steps:

1.  **Clone the repository and navigate to the `Week-07` folder.**

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install streamlit scikit-learn pandas
    ```

4.  **Run the Streamlit application:**
    Open your terminal in the `Week-07` directory and run the following command:
    ```bash
    streamlit run app.py
    ```

5.  Your web browser will automatically open with the Iris flower prediction app running.
   
