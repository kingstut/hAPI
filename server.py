from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/send-haptic', methods=['POST'])
def send_haptic():
    try:
        # Extracting the pattern from the request
        pattern = request.json

        # Send pattern to the iPhone app (assuming it has an endpoint listening for this)
        iphone_app_url = "http://<IP_ADDRESS>:<PORT>/trigger-haptic" 
        response = requests.post(iphone_app_url, json=pattern)

        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Haptic pattern sent successfully!"}), 200
        else:
            return jsonify({"status": "error", "message": "Failed to send pattern to iPhone."}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
