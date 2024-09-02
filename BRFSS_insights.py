import joblib

reg = joblib.load('Logistic_model_BRFSS.pkl')

print('green')


def survey_input():
    features = [
             'children', 'employ', 'HighBP', 'HighChol', 'BMI', 'Smoker',
        'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'HvyAlcoholConsump',
        'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age',
        'Education', 'Income'
    ]
    
    
    responses = []

    print("Please answer the following questions (Type your response and press Enter):")
    
    for feature in features:
        response = int(input(f"{feature.replace('_', ' ')}: "))
        responses.append(response)
    
    return responses

# Example usage
user_data = survey_input()
print("\nCollected Data:", user_data)
import pandas as pd

# Example list


# Convert to DataFrame
df = pd.DataFrame(user_data, columns=['Column1'])

h = reg.predict(df)
c = bool(h)

print(f"Diabetes Predictor : {c}")

dt_pred_cc= int(input("Type 1 if the Predictor gave right result "))
user_data.insert(dt_pred_cc , 0)



# Storeing User Data to the database for further inhansment

from sqlalchemy import create_engine

# Set connection string

connection = create_engine(f'mysql+mysqlconnector://root:****@localhost:3306/Krankenhaus')
cursor = connection.cursor()
cursor.execute("INSERT INTO diabetes_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , user_data)







