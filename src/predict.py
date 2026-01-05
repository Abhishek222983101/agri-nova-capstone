import pickle
import os
from flask import Flask, request, jsonify
from pydantic import ValidationError

# --- IMPORT FIX ---
# This allows the code to work both for Tests (from root) and Docker (from src)
try:
    from src.schema import CropInput
except ImportError:
    from schema import CropInput
# ------------------

# Dynamic path setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.bin')

# Load the model
with open(MODEL_PATH, 'rb') as f_in:
    model, id_to_label = pickle.load(f_in)

app = Flask('crop_recommendation')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        valid_data = CropInput(**data)
        
        features = [
            valid_data.N, valid_data.P, valid_data.K,
            valid_data.temperature, valid_data.humidity,
            valid_data.ph, valid_data.rainfall
        ]

        pred_idx = model.predict([features])[0]
        result = {
            'recommended_crop': id_to_label[pred_idx],
            'status': 'success'
        }
        return jsonify(result)

    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)