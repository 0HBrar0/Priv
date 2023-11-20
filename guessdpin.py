import requests
from tqdm import tqdm
from multiprocessing import Pool

url = "https://www.guessthepin.com/prg.php"

def guess(num):
    r = requests.post(url, data={"guess": f"{num:04d}"})
    return num, r.url

if __name__ == "__main__":
    with Pool(32) as pool:
        for num, url in pool.imap_unordered(guess, tqdm(range(2060, 10_000))):
            if url != "https://www.guessthepin.com/":
                print(f"Number: {num:04d}, URL: {url}")
                break
