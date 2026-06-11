from datetime import datetime
import os

def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # Create filename in required format
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write file in current working directory
    with open(filename, "w") as file:
        for item in data:
            file.write(str(item) + "\n")

    # Confirmation message (tests expect this)
    print(f"Log file created: {filename}")

    return filename
