import numpy as np
from keras import models
from tensorflow.python.keras.models import Sequential

# Load model
model: Sequential =  models.load_model('birds.keras')

def predict_bird(image_array):
    """
    Takes an image array, preprocesses it, and predicts the bird species.
    """
    # Assuming the image array is already preprocessed to model's expected input
    predictions = model.predict(np.expand_dims(image_array, axis=0))
    predicted_class = np.argmax(predictions, axis=1)
    return predicted_class