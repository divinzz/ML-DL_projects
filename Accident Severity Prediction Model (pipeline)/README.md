# Accident Severity Prediction Model

The Accident Severity Prediction Model aims to classify traffic accidents into different severity levels using various contributing factors. By accurately predicting the severity, this model can aid resource allocation, emergency response planning, and safety improvements.

### Key Features:
- **Predict Accident Severity**: The model predicts whether an accident will result in a slight injury, serious injury, or fatal injury.
- **Data Features**: The dataset contains information such as:
  - Driver’s age and gender
  - Vehicle type and condition
  - Road conditions (wet, dry, icy)
  - Weather conditions at the time of the accident
  - Time of day and other environmental factors
- **Model Type**: A **RandomForestClassifier** is employed for training the model, optimized with feature selection techniques for improved performance.
- **Data Preprocessing**: Data is preprocessed to handle missing values, encode categorical variables, and balance the dataset for fairness.

## Problem Statement

Accident severity prediction plays a crucial role in preventing accidents and saving lives. By predicting accident severity, traffic authorities can better identify high-risk areas or conditions and take targeted actions to reduce risks. It also helps emergency responders prioritize their resources based on predicted severity.

## Dataset Description

The dataset used for this project contains historical traffic accident data with various features:
- **Driver Information**: Age, experience, and type of vehicle.
- **Weather and Road Conditions**: Weather conditions, road surface conditions, and visibility at the time of the accident.
- **Casualty Information**: Injury details and fatalities resulting from the accident.

The dataset undergoes cleaning and preprocessing steps, such as imputation of missing values, one-hot encoding of categorical features, and splitting into training and testing sets for evaluation.

## Model Development

The process for building the model follows these key steps:
1. **Data Preprocessing**: Clean the dataset by handling missing data, encoding categorical variables, and splitting into features (X) and target (y).
2. **Model Selection**: A **RandomForestClassifier** is chosen for its ability to handle both numerical and categorical data effectively and its robustness in classification tasks.
3. **Model Training and Optimization**: The model is trained using the data, and feature selection is applied to improve predictive performance.
4. **Model Evaluation**: The model is evaluated using classification metrics such as accuracy, precision, recall, and F1-score.

## Use Cases

- **Traffic Authorities**: Authorities can use the model to predict accident severity and deploy resources efficiently.
- **Emergency Responders**: The model can assist in assessing the severity of accidents and prioritizing response times.
- **Transportation Safety**: Insights from the model can guide road safety campaigns and infrastructure planning.

## Conclusion

The Accident Severity Prediction Model represents a significant step forward in leveraging machine learning to predict and mitigate the impacts of road traffic accidents. By predicting accident severity, the model can assist in saving lives, improving resource allocation, and enhancing traffic safety. This project is an example of how data-driven solutions can have a tangible impact on public safety and the optimization of transportation systems.


## Future Work

- **Improving Model Accuracy**: Experimenting with algorithms like XGBoost or Neural Networks for better performance.
- **Real-Time Predictions**: Implementing the model into real-time systems to predict accident severity proactively.
- **Incorporating Additional Data**: Adding data like traffic volume or real-time weather data could further improve model accuracy.

## Conclusion

The Accident Severity Prediction Model represents a significant step forward in leveraging machine learning to predict and mitigate the impacts of road traffic accidents. By predicting accident severity, the model can assist in saving lives, improving resource allocation, and enhancing traffic safety. This project is an example of how data-driven solutions can have a tangible impact on public safety and the optimization of transportation systems.

# OUTPUT OF THE TASK

<img width="910" height="681" alt="Image" src="https://github.com/user-attachments/assets/56b822c4-7727-476a-8862-58e19213c3ca" />
