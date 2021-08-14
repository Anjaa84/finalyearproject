import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('rice_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
image = Image.open('test/rice_brownspot.jpg')
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array
prediction = model.predict(data)
classes=["Rice_BrownSpot","Rice_Healthy","Rice_Hispa","Rice_LeafBlast"]
maxVal=max(prediction[0])
indexOfClass = np.where(prediction[0] == maxVal)
print(classes[indexOfClass[0][0]])