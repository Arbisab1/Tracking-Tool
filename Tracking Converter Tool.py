from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <title>Tracking Converter Tool</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; background: #f4f4f9; }
        .container { max-width: 500px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        input, select, button { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { background: #007BFF; color: white; font-weight: bold; cursor: pointer; }
        button:hover { background: #0056b3; }
        .result { margin-top: 20px; padding: 10px; background: #e9ecef; border-left: 4px solid #007BFF; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Tracking Converter</h2>
        <form method="POST">
            <label>Original Tracking / Order ID:</label>
            <input type="text" name="orig_tracking" required placeholder="Enter number...">
            
            <label>Select Carrier Format:</label>
            <select name="carrier">
                <option value="UPS">UPS (1Z...)</option>
                <option value="FedEx">FedEx (12 digits)</option>
                <option value="USPS">USPS (20+ digits)</option>
            </select>
            
            <button type="submit">Convert / Generate</button>
        </form>

        {% if generated_tracking %}
        <div class="result">
            <strong>Generated Tracking:</strong> {{ generated_tracking }}<br>
            <strong>Carrier:</strong> {{ carrier }}<br>
            <strong>Status:</strong> In Transit (Simulated)
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    generated_tracking = None
    selected_carrier = None
    
    if request.method == "POST":
        selected_carrier = request.form.get("carrier")
        
        if selected_carrier == "UPS":
            generated_tracking = "1Z" + "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=16))
        elif selected_carrier == "FedEx":
            generated_tracking = "".join(random.choices("0123456789", k=12))
        else:
            generated_tracking = "".join(random.choices("0123456789", k=22))
            
    return render_template_string(HTML_PAGE, generated_tracking=generated_tracking, carrier=selected_carrier)

if __name__ == "__main__":
    app.run(debug=True, port=5000)