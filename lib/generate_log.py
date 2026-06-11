
from datetime import datetime

def generate_log(data):
    # 1. Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # 2. Timestamped filename (STRICT FORMAT)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # 3. Write file in expected format
    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")

    # 4. REQUIRED confirmation message (must include filename)
    print(f"Log file created: {filename}")

    return filename