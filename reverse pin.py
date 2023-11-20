import requests
from tqdm import tqdm
from multiprocessing import Pool
for n in range(10):
    url = "https://www.guessthepin.com/prg.php"

    def guess(num):
        pin = f"{num:04d}"
        try:
            r = requests.post(url, data={"guess": str(pin)})
            return num, r.url
        except requests.exceptions.ConnectionError:
            print(f"ConnectionError occurred for pin {pin}. Retrying...")
            return None, None

    if __name__ == "__main__":
        last_successful_num = 9999
        with Pool(42) as pool:
            for num, url in pool.imap_unordered(guess, tqdm(range(last_successful_num, -1, -1))):
                if num is not None and url is not None and url != "https://www.guessthepin.com/":
                    print(f"Number: {num:04d}, URL: {url}")
                    last_successful_num = num - 1
                    break
