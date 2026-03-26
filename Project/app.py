from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

reports = []
pending_data = None

model = MobileNet(weights='imagenet', include_top=False, pooling='avg')


def get_image_vector(path):
    img = image.load_img(path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return model.predict(img_array)


def is_near(lat1, lon1, lat2, lon2):
    return abs(lat1 - lat2) < 0.0005 and abs(lon1 - lon2) < 0.0005


@app.route('/', methods=['GET', 'POST'])
def index():
    global pending_data

    message = ""
    high_match = []
    medium_match = []
    low_match = []
    show_popup = False

    if request.method == 'POST':

        file = request.files['image']
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        category = request.form['category']

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        new_vec = get_image_vector(filepath)

        nearby_reports = []

        for report in reports:
            if is_near(lat, lon, report['lat'], report['lon']):
                nearby_reports.append(report)

        for report in nearby_reports:
            sim = cosine_similarity(new_vec, report['vec'])[0][0]

            if sim > 0.75 and category == report['category']:
                high_match.append((report, sim))
            elif category == report['category']:
                medium_match.append((report, sim))
            else:
                low_match.append((report, sim))

        # ✅ ADD THIS (sorting)
        high_match.sort(key=lambda x: x[1], reverse=True)
        medium_match.sort(key=lambda x: x[1], reverse=True)
        low_match.sort(key=lambda x: x[1], reverse=True)

        # Existing logic (unchanged)
        if high_match or medium_match or low_match:
            pending_data = {
                'lat': lat,
                'lon': lon,
                'vec': new_vec,
                'category': category,
                'img_path': filepath
            }

            show_popup = True
            message = "⚠️ Similar or nearby issue found. Confirm to submit."

        else:
            reports.append({
                'lat': lat,
                'lon': lon,
                'vec': new_vec,
                'category': category,
                'img_path': filepath
            })

            message = "✅ New issue saved successfully."

    return render_template(
        'index.html',
        message=message,
        high_match=high_match,
        medium_match=medium_match,
        low_match=low_match,
        show_popup=show_popup
    )


@app.route('/confirm')
def confirm():
    global pending_data

    if pending_data:
        reports.append(pending_data)
        pending_data = None

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)