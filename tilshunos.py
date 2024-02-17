import requests
import threading

def html_code(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(response.text)
            print("HTML kodi tayyor!!!")
    else:
        print("Xatolik")

def save_hrml_code():

    threads = []

    for n in range(1, 11):
        url = f"https://tilshunos.com/sinonims/?page={n}"
        file_name = f"index_{n}.html"
        thread = threading.Thread(target=html_code, args=(url, file_name))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

save_hrml_code()
