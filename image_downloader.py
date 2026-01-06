import requests
import time
import uuid
import threading

start = time.perf_counter()

class ImageDownloaderByURL(threading.Thread):

    def __init__(self, url):

        self.url = url
        threading.Thread.__init__(self)

    def run(self):
        
        print(f'Thread name is {threading.current_thread().name} with ID {threading.get_ident()}')

        image = requests.get(self.url).content
        image_name = f'images/{str(uuid.uuid4())}.jpg'

        with open(image_name, "wb") as image_file:
            image_file.write(image)
            print('Image Downloaded!!!')


if __name__ =='__main__':
    urls =[
        "https://images.pexels.com/photos/2002719/pexels-photo-2002719.jpeg",
        "https://images.pexels.com/photos/1292241/pexels-photo-1292241.jpeg",
        "https://images.pexels.com/photos/36487/above-adventure-aerial-air.jpg",
        "https://images.pexels.com/photos/2559941/pexels-photo-2559941.jpeg",
        "https://images.pexels.com/photos/844297/pexels-photo-844297.jpeg",
        "https://images.pexels.com/photos/1646178/pexels-photo-1646178.jpeg",
        "https://images.pexels.com/photos/1323550/pexels-photo-1323550.jpeg",
        "https://images.pexels.com/photos/325185/pexels-photo-325185.jpeg",
        "https://images.pexels.com/photos/2915997/pexels-photo-2915997.jpeg",
        "https://images.pexels.com/photos/66997/pexels-photo-66997.jpeg",
        "https://images.pexels.com/photos/1933319/pexels-photo-1933319.jpeg",
        "https://images.pexels.com/photos/1146134/pexels-photo-1146134.jpeg",
        "https://images.pexels.com/photos/1194420/pexels-photo-1194420.jpeg",
        "https://images.pexels.com/photos/414144/pexels-photo-414144.jpeg"
    ]

    threads = []
    for url in urls:
        thread = ImageDownloaderByURL(url)
        thread.start()

        threads.append(thread)
    
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'\nFinished in {round(finish-start,2)}')
    