from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model once at the start
model_file = 'airbnb-model.bin'
with open(model_file, 'rb') as f_in:
    model_data = pickle.load(f_in)

w0 = model_data['w0']
w = model_data['w']
base_line = model_data['baseline']
categorical = model_data['categorical']

# --- Function to prepare input data ---
def prepare_X(df):
    df = df.copy()
    features = base_line + ['latitude', 'longitude']
    
    for v in ['manhattan', 'brooklyn', 'queens']: 
        feature = f'is_neighbourhood_{v}'
        df[feature] = (df['neighbourhood_group'] == v).astype(int)
        features.append(feature)
    
    for name, values in categorical.items():
        for value in values: 
            col = f'{name}_{value}'
            df[col] = (df[name] == value).astype(int)
            features.append(col)

    df_new = df[features].fillna(0)
    return df_new.values

# --- Utility to clean strings ---
string_columns = ['neighbourhood_group', 'neighbourhood', 'room_type']
def clean_listing(listing):
    for col in string_columns:
        val = listing.get(col, 'unk')
        if isinstance(val, list):
            val = val[0]
        listing[col] = str(val).lower().replace(' ', '_')
    return listing

# --- Prediction route ---
@app.route('/predict', methods=['POST'])
def predict():
    try:
        listing = request.get_json()
        listing = clean_listing(listing)
        df = pd.DataFrame([listing])
        X = prepare_X(df)
        y_pred = w0 + X.dot(w)
        return jsonify({'price': float(np.exp(y_pred[0]))})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
