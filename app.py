from flask import Flask, request, render_template, url_for
from PIL import Image
import os
import google.generativeai as genai
from detector import process_image
import json
import re
# Gemini Setup
GOOGLE_API_KEY = 'APT KEY'  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Flask Setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['CROPPED_FOLDER'] = 'static/cropped_mask'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['CROPPED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files or request.files['image'].filename == '':
        return "No image uploaded", 400

    image_file = request.files['image']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
    image_file.save(image_path)

    cropped_paths, segment_output = process_image(image_path)

    analysis_results = []
    prompt = """
    You are a Indian nutrition analysis AI. Given this image of a Indian food item, identify the food and return the result strictly in JSON format.
    names: ["biryani","bread Halwa","tandoori-chicken","chicken fry", "chicken 65","Egg","Sambar","raitha","chutney", "dosa", "idli"] detect from these names. 
    {
      "name": "Food Item Name",
      "calories": 123,
      "carbohydrates": 20,
      "proteins": 10,
      "fats": 5
    }
    """

    for path in cropped_paths :
        try:
            img = Image.open(path)
            response = model.generate_content([prompt, img])
            result_json = response.text.strip()

            # Clean up and load JSON
            cleaned = re.sub(r'```json|```', '', result_json).strip()
            parsed_json = json.loads(cleaned)

            analysis_results.append({
                "image": path.replace("static/", "").replace("\\", "/"),
                "data": parsed_json  # send parsed JSON as a dict
            })
        except Exception as e:
            analysis_results.append({
                "image": path.replace("static/", "").replace("\\", "/"),
                "data": {"name": "Error", "calories": 0, "carbohydrates": 0, "proteins": 0, "fats": 0, "error": str(e)}
            })
    print(analysis_results)
    return render_template('index1.html', results=analysis_results, segment_image=segment_output.replace("static/", ""))
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0" ,port=9510)
