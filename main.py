from flask import Flask, render_template
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import config
from config import HERE_JS

# # Passing API KEY and URL to the Visual Recognition
authenticator = IAMAuthenticator(config.IBM_API_KEY)

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator)

visual_recognition.set_service_url(config.IBM_URL)

file_name = 'test'

# Running the Visual Recognition on test.img file
with open(f'{file_name}.jpg', 'rb') as image:
    classes = visual_recognition.classify(
        images_file=image, threshold='0.6', classifier_ids='food').get_result()

# print(json.dumps(classes, indent=2))
with open(f'results/{file_name}.json','w') as file:
    json.dump(classes, file, indent=2)
print("Results generated successfully")
print("Now,launching Flask app..")


output_query = classes['images'][0]['classifiers'][0]['classes'][1]['class']
# print(output_query)

# Passing 'pizza' to the HERE APIs using Python Flask

latitude = 22.462179
longitude = 88.381233

app = Flask(__name__)


@app.route('/')
def map_func():
    return render_template('map.html',
                           latitude=latitude,
                           longitude=longitude,
                           output_query=output_query,
                           apikey=HERE_JS
                           )


if __name__ == '__main__':
    app.run(debug=True)
