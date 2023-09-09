import asyncio
from bleak import BleakScanner, BleakClient

BUZZ_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
WRITE_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
NOTIFY_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

buzz_address = None

async def discover_buzz():
    global buzz_address
    devices = await BleakScanner.discover()
    for device in devices:
        if BUZZ_UUID.lower() in device.metadata["uuids"]:
            print(f"Found Buzz device: {device.name}, Address: {device.address}")
            buzz_address = device.address

async def control_buzz(address):
    async with BleakClient(address) as client:

        # Register for notifications (optional)
        def callback(sender: int, data: bytearray):
            print(f"Received: {data}")

        await client.start_notify(NOTIFY_UUID, callback)

        # Authorize developer access
        await client.write_gatt_char(WRITE_UUID, bytearray(b"auth as developer"))
        await asyncio.sleep(2)
        await client.write_gatt_char(WRITE_UUID, bytearray(b"accept"))

        # Example: Vibrate motor 0
        await client.write_gatt_char(WRITE_UUID, bytearray(b"motors vibrate /wAAAA=="))

        # Keep the script running to keep listening to notifications
        await asyncio.sleep(10)

        await client.stop_notify(NOTIFY_UUID)

async def main():
    await discover_buzz()
    if buzz_address:
        await control_buzz(buzz_address)
    else:
        print("No Buzz device found.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
