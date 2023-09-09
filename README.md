# hAPI
 interface for sending haptic patterns

This interface provides a unified way to send haptic feedback patterns to various devices eg, neosensory Buzz, iPhones.

## Start the Flask server:
python server.py

## Send haptic patterns
```python
from send_utils import send_pattern 
pattern = [{ "start": 0, "duration": 500, "intensity": 255 }]
send_pattern("iphone", pattern)
``````