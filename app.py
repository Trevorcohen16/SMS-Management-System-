from flask import Flask, render_template, request, jsonify
from sms_processor import SMSProcessor
import logging

# Set up logging to debug issues
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Flask app
app = Flask(__name__)

# Initialize the SMS processor
processor = SMSProcessor()

# Route for the main dashboard
@app.route('/')
def index():
    logger.info("Rendering index page...")
    return render_template('index.html', status="Status: Stopped", logs="\n".join(processor.logs))

# Route to start the processor
@app.route('/start', methods=['POST'])
def start_processor():
    try:
        port = request.form.get('port', 'COM3')
        baud = request.form.get('baud', 9600)
        logger.info(f"Starting processor with port={port}, baud={baud}")
        processor.port = port
        processor.baud = baud
        processor.start()
        return jsonify({"status": "Status: Running", "logs": "\n".join(processor.logs)})
    except Exception as e:
        logger.error(f"Error starting processor: {e}")
        return jsonify({"status": f"Status: Error - {e}", "logs": "\n".join(processor.logs)})

# Route to stop the processor
@app.route('/stop', methods=['POST'])
def stop_processor():
    try:
        logger.info("Stopping processor...")
        processor.stop()
        return jsonify({"status": "Status: Stopped", "logs": "\n".join(processor.logs)})
    except Exception as e:
        logger.error(f"Error stopping processor: {e}")
        return jsonify({"status": f"Status: Error - {e}", "logs": "\n".join(processor.logs)})

# Route to update logs (AJAX polling)
@app.route('/update_logs')
def update_logs():
    return jsonify({"logs": "\n".join(processor.logs)})

# Route to update events for the graph
@app.route('/update_events')
def update_events():
    sent = sum(1 for e in processor.events if e['type'] == 'sent')
    received = sum(1 for e in processor.events if e['type'] == 'received')
    return jsonify({"sent": sent, "received": received})

if __name__ == '__main__':
    try:
        logger.info("Starting Flask app on 0.0.0.0:8050...")
        app.run(debug=True, host='0.0.0.0', port=8050)
    except Exception as e:
        logger.error(f"Failed to start Flask app: {e}")