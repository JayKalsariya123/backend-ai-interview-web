from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from video_processor import process_video
from audio_processor import process_audio
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'video' not in request.files:
        return jsonify({"error": "No video file uploaded"}), 400

    file = request.files['video']
    question_text = request.form.get('questionText', '')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            print("Starting video processing")
            video_result = process_video(file_path)
            print("Finished video processing")

            print("Starting audio processing")
            audio_result = process_audio(file_path, question_text)
            print("Finished audio processing")

            audio_score = audio_result["score"]
            video_score = video_result["score"]
            
            total_score = (0.7 * audio_score) + (0.3 * video_score) + 3
            weighted_score = min(total_score, 10)

            response = {
                "question": question_text,
                "finalScore": round(weighted_score, 2),
                "bodyLanguage": video_result["feedback"],
                "answerQuality": audio_result["feedback"],
            }
            print(response)
            return jsonify(response), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    else:
        return jsonify({"error": "Invalid file type. Allowed types: mp4, avi, mov"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render assigns this dynamically
    app.run(host="0.0.0.0", port=port, debug=True)
