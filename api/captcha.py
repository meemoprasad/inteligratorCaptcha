from flask import Blueprint, request, jsonify, session

captcha_bp = Blueprint('captcha', __name__)

@captcha_bp.route('/submit', methods=['POST'])
def submit_captcha():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    if data.get("passed"):
        session['captcha_verified'] = True  # Mark user as human
        return jsonify({"status": "success", "message": "CAPTCHA passed!"})
    else:
        return jsonify({"status": "fail", "message": "CAPTCHA not completed."}), 403
