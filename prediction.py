import pickle
import numpy as np


with open('features.pkl', 'rb') as f:
    features = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


def heart_attack(age, restingBp, cholesterol, maxhr, sex, chest_pain_type, exercise_agna, st_slope, fasting_bs):
    pred_test = np.zeros(len(features.columns))

    chest_pain_type_index = np.where(features.columns == chest_pain_type)[0][0]
    sex_index = np.where(features.columns == sex)[0][0]
    exercise_agna_index = np.where(features.columns == exercise_agna)[0][0]
    st_slope_index = np.where(features.columns == st_slope)[0][0]
    fasting_bs_index = np.where(features.columns == fasting_bs)[0][0]

    pred_test[0] = age
    pred_test[1] = restingBp
    pred_test[2] = cholesterol
    pred_test[3] = maxhr
    pred_test[sex_index] = 1
    pred_test[chest_pain_type_index] = 1
    pred_test[exercise_agna_index] = 1
    pred_test[st_slope_index] = 1
    pred_test[fasting_bs_index] = 1

   
    scaled_prediction = scaler.transform([pred_test])

    return model.predict(scaled_prediction)


prediction = heart_attack(54, 140, 289, 172, 'F', 'ATA', 'N', 'Up', '0')

