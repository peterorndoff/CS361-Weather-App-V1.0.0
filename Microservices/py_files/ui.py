import time
from PIL import Image

while True:

    request = input("Input 1 to generate an image, 2 to exit: ")

    if request == str(1):
        
        with open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/prng-service.txt", "w") as prng_serv:
            prng_serv.write('run')
        
        time.sleep(3)

        with open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/prng-service.txt", "r") as prng_serv:
            ran_num = prng_serv.read()


        with open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/image-service.txt", "w") as img_serv:
            img_serv.write('')
            img_serv.write(ran_num)
        time.sleep(3)

        with open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/image-service.txt", "r") as img_serv:
            path = img_serv.read()
            copy_path = path

        print('Here is the Path: ', copy_path)

        prompt = input('Would you like to open the image?')
        
        if prompt == "yes":
            with open(copy_path) as image:
                Image.open(copy_path)

    if request == str(2):
        exit