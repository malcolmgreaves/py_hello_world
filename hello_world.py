import sys
import time


def convert(a: str) -> float | int:
    try:
        wait_s = int(a)
    except:
        try:
            wait_s = float(a)
        except:
            print(f'UNRECOGNIZED wait_s: "{a}" -- no waiting!')
            wait_s = None
    return wait_s


def main(wait_s: float | int) -> dict[str, float | int]:
    print("Hello world!")
    
    if wait_s is not None and not isinstance(wait_s, (float, int)):
        wait_s = convert(wait_s)

    if wait_s is not None and isinstance(wait_s, (float, int)) and wait_s >= 0:
        print(f"Waiting for {wait_s} seconds...")
        if wait_s < 1:
            time.sleep(wait_s)
        else:
            i = 1
            while wait_s > 0:
                print(f"\t[{i}] hello world :) ({wait_s}s remaining)")
                wait_s -= 1
                i += 1
                time.sleep(1)
    return {"wait_s": wait_s}


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        wait_s = convert(sys.argv[1])
    else:
        wait_s = 60
    main(wait_s)
