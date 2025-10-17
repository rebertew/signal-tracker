import json
import time
from utils.signal_generator import generate_signal

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    config = load_config()
    print("🚀 Starting Crypto Signal Tracker...\n")
    while True:
        for coin in config["coins"]:
            signal = generate_signal(coin)
            print(signal)
        time.sleep(config["signal_interval"])

if __name__ == "__main__":
    main()
