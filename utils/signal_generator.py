import random
import datetime

def generate_signal(coin):
    actions = ["BUY", "SELL", "HOLD"]
    price = round(random.uniform(100, 70000), 2)
    signal = random.choice(actions)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"[{timestamp}] {coin}: {signal} at ${price}"
