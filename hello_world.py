import sys
import time

def main(wait_s = None) -> None:
    print("Hello world!")
    
    if wait_s is not None and isinstance(wait_s, (float, int)) and wait_s >= 0:
        print(f"Waiting for {wait_s} seconds")
        time.sleep(wait_s)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        a = sys.argv[1]
        try:
            wait_s = int(a)
        except:
            try:
                wait_s = float(a)
            except:
                print(f'UNRECOGNIZED wait_s: "{a}" -- no waiting!')
                wait_s = None
    else:
        wait_s = None
    main(wait_s)
