import threading
import time
from collections import deque
from gemini_api import generate_response

class SMSProcessor:
    def __init__(self, port='COM3', baud=9600):
        self.port = port
        self.baud = baud
        self.running = False
        self.thread = None
        self.logs = deque(maxlen=100)  # Store up to 100 logs
        self.events = []  # Store SMS events for graphing
    
    def start(self):
        """Start the SMS processing thread."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
            self.logs.append("SMS processor started.")
    
    def stop(self):
        """Stop the SMS processing thread."""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
        self.logs.append("SMS processor stopped.")
    
    def run(self):
        """Simulate SMS processing (no modem required)."""
        self.logs.append("Simulating SMS processing (no modem connected)...")
        while self.running:
            try:
                # Simulate receiving an SMS
                simulated_message = {'index': '1', 'sender': '+1234567890', 'text': 'Hello, this is a test!'}
                self.logs.append(f"Simulated SMS from {simulated_message['sender']}: {simulated_message['text']}")
                self.events.append({'time': time.time(), 'type': 'received'})
                
                # Generate and "send" response
                response_text = generate_response(simulated_message['text'])
                self.logs.append(f"Simulated SMS sent to {simulated_message['sender']}: {response_text}")
                self.events.append({'time': time.time(), 'type': 'sent'})
                
                # Simulate deleting the message
                self.logs.append(f"Simulated deletion of message index {simulated_message['index']}")
            except Exception as e:
                self.logs.append(f"Error in simulation: {e}")
            time.sleep(10)  # Simulate checking every 10 seconds