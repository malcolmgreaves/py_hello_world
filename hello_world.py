import os
import time

if __name__ == "__main__":
    print("Hello world!")
    
    wait_s = int(os.environ.get("WAIT_S", "0"))
    print(f"[WAIT_S] Waiting for {wait_s} seconds")
    
    time.sleep(wait_s)

