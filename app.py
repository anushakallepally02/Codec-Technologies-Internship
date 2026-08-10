from flask import Flask, render_template_string

app = Flask(__name__)

DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>API Performance Monitor Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: #333; margin-bottom: 30px; }
        .metric-card { background: #f9fbfd; border: 1px solid #e2e8f0; padding: 20px; margin-bottom: 25px; border-radius: 6px; }
        h3 { margin-top: 0; color: #2c3e50; }
        .bar-container { background-color: #e2e8f0; border-radius: 4px; margin-bottom: 10px; position: relative; height: 25px; }
        .bar { height: 100%; border-radius: 4px; text-align: right; line-height: 25px; color: white; padding-right: 10px; font-weight: bold; font-size: 12px; }
        .blue-bar { background-color: #3498db; }
        .green-bar { background-color: #2ecc71; width: 80%; }
        .red-bar { background-color: #e74c3c; width: 20%; }
        .label-text { display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 5px; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 API Performance Metrics Dashboard</h1>
        
        <div class="metric-card">
            <h3>📈 Response Time History (ms)</h3>
            <div class="label-text"><span>API Endpoint 1 (httpbin.org)</span> <span>210 ms</span></div>
            <div class="bar-container"><div class="bar blue-bar" style="width: 42%;"></div></div>
            
            <div class="label-text"><span>API Endpoint 2 (typicode.com)</span> <span>340 ms</span></div>
            <div class="bar-container"><div class="bar blue-bar" style="width: 68%;"></div></div>
            
            <div class="label-text"><span>API Endpoint 3 (google.com)</span> <span>150 ms</span></div>
            <div class="bar-container"><div class="bar blue-bar" style="width: 30%;"></div></div>
        </div>

        <div class="metric-card">
            <h3>📊 Response Status Distribution</h3>
            <div class="label-text"><span>SUCCESS (80%)</span></div>
            <div class="bar-container"><div class="bar green-bar">80%</div></div>
            
            <div class="label-text"><span>FAILED (20%)</span></div>
            <div class="bar-container"><div class="bar red-bar">20%</div></div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    return render_template_string(DASHBOARD_TEMPLATE)

if __name__ == "__main__":
    app.run(port=5000, debug=True)