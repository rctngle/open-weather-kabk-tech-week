import requests
import re
import os

def download_file_from_google_drive(url, destination_folder):
    file_id = get_file_id_from_url(url)
    if not file_id:
        print(f"Could not extract file ID from URL: {url}")
        return

    destination_path = os.path.join(destination_folder, f"{file_id}.png")
    URL = "https://drive.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination_path)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def get_file_id_from_url(url):
    # Updated regex to match the id parameter in the query string
    match = re.search(r'id=([\w-]+)', url)
    return match.group(1) if match else None

if __name__ == "__main__":
    # Directory to save the files
    destination_folder = 'files/'
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List of Google Drive URLs
    urls = [
        'https://drive.google.com/open?id=1ZZ3g6CEW5_MbpJaYyVgVa67ELUpn8vTc',
        'https://drive.google.com/open?id=1W4JKSMohxBUPKVT5almzT2DkO9OZZ32i',
        'https://drive.google.com/open?id=1RL4FjEzYRjp3ydcjxG6rG3jYbC6w1qlf',
        'https://drive.google.com/open?id=1zEKXqn9_pwyx6Glc6d1u8NO1B0f4_UTQ',
        'https://drive.google.com/open?id=19phquzjhMysTA3P1aMb6fwLmqkT8jFla',
        'https://drive.google.com/open?id=1lKI_ze3PfsnR2W_X3BQpLLGc21h6hlR8',
        'https://drive.google.com/open?id=15LlPkwKJS0pmllD_eQqR-a_ODuWyyaVU',
        'https://drive.google.com/open?id=1_9YF7sYtmmt_ljZGT5UJ6zVGsbuMh0h7',
        'https://drive.google.com/open?id=1PIGTM0mlV6aQI9x8IRdv9YCNMEw4bqHi',
        'https://drive.google.com/open?id=1ijfgS0voMksr_DaKMG8Zdsl_8O_TE0dd',
        'https://drive.google.com/open?id=1dmv32TRToUehIN3nIwR0TkGoSdaPKTO9',
        'https://drive.google.com/open?id=1FmWYYV5habU2p6w2G36eVTON-aF8v_5s',
        'https://drive.google.com/open?id=1tvFXdN6rjCBXm-hK4qIqWgEyWfszkE-o',
        'https://drive.google.com/open?id=1zC72EozjP__d9eMlLwH6ppQuGgu7yypH',
        'https://drive.google.com/open?id=1_s8K9FJcjk_LBQXFehkh5Omjidija2aB',
        'https://drive.google.com/open?id=1Rxkxq9A5wid1IZtDTeaprD81Fm2diLTu',
        'https://drive.google.com/open?id=1eQxs9AT9CqAu-SRgZoiCM79gU2nuKPaz',
        'https://drive.google.com/open?id=1QOAtBWGbkCBsTQ0E5v44ftcOhiLKhg91',
        'https://drive.google.com/open?id=1us5h-ePZUOK1xxCSTmHmAWNOb1TVGEwx',
        'https://drive.google.com/open?id=1sJERjkY-55eWNcQOpHUBtpKiHq8jT8SX',
        'https://drive.google.com/open?id=1m4rLWhS-xwvSLCucDs-jXPaSOXM1SmF1',
        'https://drive.google.com/open?id=1yt7Vu_JZioFfZmp8K1RhYslg0aVDEgsA',
        'https://drive.google.com/open?id=1WK5av8UsrwYTkEQqmNURXMt1LqcIOloq',
        'https://drive.google.com/open?id=1zgqU4WHjjAqK5F3dM4M12B5BOGOO2iJb',
        'https://drive.google.com/open?id=1ojGmzMw3Y8eGBYj_8Kd7R6467hGNTO2C',
        'https://drive.google.com/open?id=12nY6NwBluM8u99rdsS0Sxs8GtAm6a80P',
        'https://drive.google.com/open?id=1Zu37zZvX6seDwGrvhCW0xP_qIB3P3uys',
        'https://drive.google.com/open?id=1s-JKVibKbR-9tDWXNHxu4-SgUxohSKUE',
        'https://drive.google.com/open?id=1OHa8hMjhBcQHD_Jiy3tdzUu23_5cVpAZ',
        'https://drive.google.com/open?id=1Z71U0eVLsSOB3n5koJcCIgkmHTwOh63z',
        'https://drive.google.com/open?id=1lROYbaXfncmjGjgcht5EkqvXMOXZqkfx',
        'https://drive.google.com/open?id=1Rg1OSlJcttHf4wEuP0DxwjfkC334CEFL',
        'https://drive.google.com/open?id=1e6tFNl-faLQsa5sLp2QKuqf_qBsa_HBY',
        'https://drive.google.com/open?id=1Qaqs3u_NmdFF2zSJrY1UKoLFFkIJyzw9',
        'https://drive.google.com/open?id=1UpiQ69tpX5La1m8dnblmHeTx0uFwwxeZ',
        'https://drive.google.com/open?id=1N9kLu26WEux7qXbThwYPqzm3X0vKBGCV',
        'https://drive.google.com/open?id=1KsiOIQyAqVF1zP8ZAeemilF3BzuMGHKj',
        'https://drive.google.com/open?id=1LmcCWjMR9WvhAqvJx_-h37DG4y9dLMHc',
        'https://drive.google.com/open?id=1ewjgV2jfaZyDmYXmT6d9b2ahejQhWqlT',
        'https://drive.google.com/open?id=1adtbwnBIpi1lr5lqlUBY7Y1lsauIZwcy',
        'https://drive.google.com/open?id=1YRrXlZaZ2bVXQ5XwBV9seRkyY-OMUiRa',
        'https://drive.google.com/open?id=1y1kD-zG3J8JlW6hXvM-i1ZEkib9G94FK',
        'https://drive.google.com/open?id=1W7L3bcLF5kGjPvASnu6caCI1RvUaf398',
        'https://drive.google.com/open?id=1tRo-qDUvnzGSkwW80BgWzx-Hoj0XyQWg',
        'https://drive.google.com/open?id=1YsFbTFjBASDoN9eTR8iDYgj3k3xZqwnB',
        'https://drive.google.com/open?id=1GtWvNR3RmXGYiDLAP0qfWpAOc5tY-oW_',
        'https://drive.google.com/open?id=1p_eSGs51ArxpsdbGy0-BnKeCi0rKNiwF',
        'https://drive.google.com/open?id=12lINRFrBN3NG1pNUt4jwhb9Z5jR5rlKu',
        'https://drive.google.com/open?id=1Q5BOVyVZ1lRI_q4IHi2mAp1aV5BRhQGM',
        'https://drive.google.com/open?id=1Gk4oWjvO0fXIHmG07SVLMh9LWUxinkLO',
        'https://drive.google.com/open?id=139e2EzmwFSOKbeCl-9k7brnW-dTewl2P',
        'https://drive.google.com/open?id=1BOHw3J_bF1x5Sl2IC95QU68UHCQK1nvk',
        'https://drive.google.com/open?id=15HGotJzR2yAFnFXcrhpKvNSv4R-aSsSH',
        'https://drive.google.com/open?id=1V8MQNmFKlENoJg_7Bkn78E8sxqIOgTXq',
        'https://drive.google.com/open?id=1frrgLESYTmrz7K_fstX64kdjHGc6Kb_L',
        'https://drive.google.com/open?id=1_L2aj6Y7QSsJnxYHGSiZgGVakXKSdEv3',
        'https://drive.google.com/open?id=1sK-3CGqyfhEtOiOXAF4gLV5Znt1M_3TW',
        'https://drive.google.com/open?id=1qomUAG7n9Ct6B99QLo1lTZlwlQX_aZV6',
        'https://drive.google.com/open?id=1cEs3RNtoFoR3jzbscEO04-HR3vqtQ6wl',
        'https://drive.google.com/open?id=1rCMb8z3vX1APZfxE5G8qO2TVbtGWII_3',
        'https://drive.google.com/open?id=1apk6coWuRRN_jbD0XRIYu-Frz4Li6QFL',
        'https://drive.google.com/open?id=1LYn8WrD5IESbMFUTeQlYl94tmWBqTNy1',
        'https://drive.google.com/open?id=1bcMWEjPcVDNHi7q9pLFZu_YwnXWPZtp_',
        'https://drive.google.com/open?id=1383pKbIB7q5-GFcBB1UhczdRqUCQoTOg',
        'https://drive.google.com/open?id=1itiORqc9UcWwPL71Xo_E7_43NQB9_qZa',
        'https://drive.google.com/open?id=12Z1UaHXrmE_CrD6B9PZ1e2LU7gCFmz0v',
        'https://drive.google.com/open?id=1j46ku-w3aXbvGhFRTuTGzoapzLfJmwhz',
        'https://drive.google.com/open?id=1TAZVw3HuaUI6hxqve_uJqLqOB5Ylbj6D',
        'https://drive.google.com/open?id=1OmpSTGYRHkkMRR1PuW5clrwJqOcbaBiR',
        'https://drive.google.com/open?id=1_HZlAWgBwJTKf-yAbBEpR8RHjINg6Nfv',
        'https://drive.google.com/open?id=14d66mP2KvgqElwLGMiWpUe6fXZdr0yYi',
        'https://drive.google.com/open?id=1E432iHaZbiH0qvI6AFi-Tl0qfF2MNc_e',
        'https://drive.google.com/open?id=1xNl8yj4KAYpMakpl7knj1FBzZ0iYfZH7',
        'https://drive.google.com/open?id=1-kDRhzUQkKnHMN73ruH8ArvwbhmI-uJ2',
        'https://drive.google.com/open?id=16NUTqdTIGj0kvh4UNuZtsD7M5Mqsqj0B',
        'https://drive.google.com/open?id=1r2kmKmPJ_ZHNQx4_zyshRjR46gcUpC41',
        'https://drive.google.com/open?id=11OMosTuLqtjCRQCUckLfCFtu8w4QgUyJ',
        'https://drive.google.com/open?id=1z1aTasZcLNL20CBsthUQSaHMtnPS3KPP',
        'https://drive.google.com/open?id=1QNSf-dZPqFoggpcRaeJuPLEKmqohLXlZ',
        'https://drive.google.com/open?id=1sg2qsE8LsreyrGqWVGKnuEA06Jggr8a9',
        'https://drive.google.com/open?id=18VAMehvFu7DSQzmyet7kwF-BX8YHrWuw',
        'https://drive.google.com/open?id=1ayK1HAl5UO8tDzs_eLe1tpxe_n3OJO9z',
        'https://drive.google.com/open?id=1tpaetUncRdvRe_UDXOSJDz2JULwjkXv0',
        'https://drive.google.com/open?id=1Zx3uUabEMhpgb6q75s4S_T-Hm7Szql_v',
        'https://drive.google.com/open?id=1QzyWy021fc2XJOoDgnw_ICXMaMZI6j05',
        'https://drive.google.com/open?id=1aiGbzSuFC_QBB2wUsKq0kx9m2eYP_PSn',
        'https://drive.google.com/open?id=1b72Lk6lMXc4FZaMx2ra4n4yMPnKpG1vj',
        'https://drive.google.com/open?id=1S_95Lk3I9aZt_tUTNupAsObXl5zxF1ZS',
        'https://drive.google.com/open?id=1sx1yfRG0Xgx-v7ztnUYGl7RgfdnbRc-U',
        'https://drive.google.com/open?id=1F-F7mrYcDlLawGSu34uUMbhdpgzrbvLK',
        'https://drive.google.com/open?id=1cX0xPZRKJVwy960c6t0IOOw1YqqoWy_i',
        'https://drive.google.com/open?id=1B3YLACkCUw7VY5u8ND4l9hSv7v-fmk2d',
        'https://drive.google.com/open?id=15Ac8Cyc0bBbh4sJV8m-6Wyp2Knr12NzU',
        'https://drive.google.com/open?id=1drrX9Q6TMR1i1ll91gWtHyP-uO9dpYii',
        'https://drive.google.com/open?id=1Tiku5o3QG1H8HU-Z3mnhShtng38jb8BH',
        'https://drive.google.com/open?id=1XcZf034oBWuBo_BM0mfhPHPOfQra2T-R',
        'https://drive.google.com/open?id=1FFGWRmY-jbSo486TtrYPC-laPIghFKuT',
        'https://drive.google.com/open?id=1gpH8ZL0gnae5bPq6WyOFeJ4e-Tgxc4jb',
        'https://drive.google.com/open?id=1hVH1XOqBlNb2AUYXK-nNKXmKU5DGntSn',
        'https://drive.google.com/open?id=1jHAz2HsoL4dimXAEmdwyvGe1tNkcWJUv',
        'https://drive.google.com/open?id=1ib-Y0g-yQ1PMncjnnzBECGoTtjlAtAJq',
        'https://drive.google.com/open?id=1sJuPZswQ4bDyoC9skfkE5BIbu_qJX470'
    ]

    for url in urls:
        download_file_from_google_drive(url, destination_folder)


