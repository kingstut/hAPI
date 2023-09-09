import base64
from bleak import BleakClient
import requests

BUZZ_ADDRESS = "XX:XX:XX:XX:XX:XX"  # Replace with your Buzz's BLE address

async def send_pattern_to_buzz(pattern):
    # Convert the pattern to bytes (this is a simple conversion, actual might vary)
    byte_pattern = [int(event["intensity"]) for event in pattern]
    
    # Convert bytes to Base64-encoded string
    encoded_pattern = base64.b64encode(bytearray(byte_pattern)).decode('utf-8')

    # Connect to the Buzz and send the pattern
    async with BleakClient(BUZZ_ADDRESS) as client:
        # Here you'd use the appropriate characteristic UUID and method to send the encoded pattern
        # For the sake of this example, I'm using placeholders
        CHARACTERISTIC_UUID = "xxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  
        await client.write_gatt_char(CHARACTERISTIC_UUID, encoded_pattern)


def send_pattern_to_iphone(pattern):
    # Convert the pattern to the format expected by your bridge/API
    # For the sake of this example, let's assume it accepts the same pattern format
    api_url = "http://localhost:5000/send-haptic"  # Replace with your API endpoint
    
    response = requests.post(api_url, json=pattern)
    
    if response.status_code != 200:
        print("Error sending pattern to iPhone:", response.text)

def send_pattern(device_type, pattern):
    if device_type == "iphone":
        send_pattern_to_iphone(pattern)
    elif device_type == "buzz":
        send_pattern_to_buzz(pattern)  # This is an async function, so in real-world, you'd need to run it in an event loop
    else:
        raise ValueError(f"Unknown device type: {device_type}")
