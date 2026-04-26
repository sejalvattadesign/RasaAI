from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from src.phase2.mapper import map_web_form_to_preferences
from src.phase2.validation import PreferenceValidationError, validate_preferences


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.post("/submit-preferences")
    def submit_preferences():
        mapped = map_web_form_to_preferences(request.form)
        try:
            validated = validate_preferences(mapped)
        except PreferenceValidationError as err:
            return jsonify({"ok": False, "errors": err.errors, "payload": mapped}), 400
        return jsonify({"ok": True, "preferences": validated})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

