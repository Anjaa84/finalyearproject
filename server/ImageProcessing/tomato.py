import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('tomato_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
image = Image.open('test/tomato_leaf_mold.JPG')
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array
prediction = model.predict(data)
classes=["Bacterial_sp","Early_blight","healthy","Late_blight","Leaf_Mold","Septoria_lea","Spider","Target_Spot","mosaic_virus","Yellow_Leaf_"]
maxVal=max(prediction[0])
indexOfClass = np.where(prediction[0] == maxVal)
print(classes[indexOfClass[0][0]])
