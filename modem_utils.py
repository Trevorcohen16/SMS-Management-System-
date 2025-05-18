import time

def send_at_command(ser, command):
    """Send an AT command to the modem and return its response."""
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read(ser.in_waiting).decode(errors='ignore')
    return response

def parse_messages(response):
    """Parse the modem's response to extract SMS details."""
    messages = []
    lines = response.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].startswith('+CMGL:'):
            parts = lines[i].split(',')
            index = parts[0].split(':')[1].strip()
            sender = parts[2].strip('"')
            if i + 1 < len(lines):
                text = lines[i + 1].strip()
                messages.append({'index': index, 'sender': sender, 'text': text})
            i += 2
        else:
            i += 1
    return messages

def send_sms(ser, number, message):
    """Send an SMS to the specified number."""
    ser.write('AT+CMGF=1\r\n'.encode())
    time.sleep(0.5)
    ser.write(f'AT+CMGS="{number}"\r\n'.encode())
    time.sleep(0.5)
    ser.write((message + chr(26)).encode())
    time.sleep(1)
    response = ser.read(ser.in_waiting).decode(errors='ignore')
    return '+CMGS:' in response or 'OK' in response

def delete_message(ser, index):
    """Delete the SMS at the specified index."""
    ser.write(f'AT+CMGD={index}\r\n'.encode())
    time.sleep(0.5)
    response = ser.read(ser.in_waiting).decode(errors='ignore')
    return 'OK' in response