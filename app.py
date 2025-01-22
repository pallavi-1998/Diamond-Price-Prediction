import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from src.components.model_trainer import ModelTrainer

st.title("Diamond Price Prediction")
# Function to display the dataset
def show_dataset():
    # Load your dataset here
    df = pd.read_csv(r"D:\Diamond_Price_Prediction\notebooks\data\gemstone.csv")  
    st.write(df)

# Function to take inputs and show output
def take_inputs_and_predict():
    st.header("Input Form")
    
    carat = st.number_input("Carat", min_value=0.0, step=0.01)  # range = 0.1 to 10 cr
    depth = st.number_input("Depth", min_value=0.0, step=0.01)  # range = 40 to 70%
    table = st.number_input("Table", min_value=0.0, step=0.01)  # range = 50 to 70%
    x = st.number_input("X", min_value=0.0, step=0.01)          
    y = st.number_input("Y", min_value=0.0, step=0.01)          # x, y, z dimention depends on diamond shape and size 
    z = st.number_input("Z", min_value=0.0, step=0.01)
    cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2"])
    
    if st.button("Predict"):
        data = CustomData(
            carat=carat,
            depth=depth,
            table=table,
            x=x,
            y=y,
            z=z,
            cut=cut,
            color=color,
            clarity=clarity
        )
        
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        results = round(pred[0], 2)
        
        st.success(f"The predicted value is {results}")

# Function to show evaluation metrics
def show_evaluation_metrics():
    # Dummy data for demonstration; replace with actual metrics
    metrics = {
        "Algorithm": ["Model 1", "Model 2", "Model 3"],
        "Accuracy": [0.85, 0.90, 0.80],
        "Precision": [0.80, 0.88, 0.78],
        "Recall": [0.82, 0.86, 0.75]
    }
    df = pd.DataFrame(metrics)
    
    st.write(df)
    
    best_model = df.loc[df['Accuracy'].idxmax()]
    st.write(f"Best Model: {best_model['Algorithm']} with Accuracy: {best_model['Accuracy']}")

# Streamlit layout
st.sidebar.title("Dashboard")
selection = st.sidebar.radio("Go to", ["Show Dataset", "Predict"])   #["Show Dataset", "Predict", "Evaluation Metrics"]

if selection == "Show Dataset":
    show_dataset()
elif selection == "Predict":
    take_inputs_and_predict()
else:
    show_evaluation_metrics()
































# from flask import Flask, render_template, request
# from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

# application  = Flask(__name__)

# app = application

# @app.route('/')
# def home_page():
#     return render_template('index.html')


# @app.route('/predict', methods= ['GET','POST'])

# def predict_datapoint():
#     if request.method=='GET':
#         return render_template('form.html')
    
#     else:
#         data=CustomData(
#             carat=float(request.form.get('carat')),
#             depth = float(request.form.get('depth')),
#             table = float(request.form.get('table')),
#             x = float(request.form.get('x')),
#             y = float(request.form.get('y')),
#             z = float(request.form.get('z')),
#             cut = request.form.get('cut'),
#             color= request.form.get('color'),
#             clarity = request.form.get('clarity')
#         )

#         final_new_data = data.get_data_as_dataframe()
#         predict_pipeline = PredictPipeline()
#         pred = predict_pipeline.predict(final_new_data)

#         results = round(pred[0], 2)

#         return render_template('results.html',final_result = results)
    

# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True)