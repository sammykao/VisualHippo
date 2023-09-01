#Optional file for analyzing two images based off Cosine Similarity
import numpy as np 
from PIL import Image
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO
import requests

vgg16 = VGG16(weights='imagenet', include_top=False, 
              pooling='max', input_shape=(224, 224, 3))

# print the summary of the model's architecture.
vgg16.summary()

for model_layer in vgg16.layers:
  model_layer.trainable = False


def load_image(link):

    response = requests.get(link)
    image_data = response.content
    input_image = Image.open(BytesIO(image_data))
    resized_image = input_image.resize((224, 224))

    return resized_image, input_image

def get_image_embeddings(object_image : image):

    image_array = np.expand_dims(image.img_to_array(object_image), axis = 0)
    image_embedding = vgg16.predict(image_array)

    return image_embedding


def get_similarity_score(link, control_image : Image):

    first_image, saved_image = load_image(link)
    second_image = control_image.resize((224, 224))

    first_image_vector = get_image_embeddings(first_image)
    second_image_vector = get_image_embeddings(second_image)
    
    similarity_score = cosine_similarity(first_image_vector, second_image_vector).reshape(1,)

    return similarity_score, saved_image