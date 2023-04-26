import time

while True:

    #time.sleep(1)

    with open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/image-service.txt", "r") as img_serv:
        number = img_serv.readline()

    if number != '':

        number = int(number)
        image_number = number % 8
        
        with  open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/image-service.txt", "w") as img_serv:
            img_serv.write("/Users/peterorndoff/Desktop/CS361/A2Microservices/images/"+str(image_number)+".jpg")

        time.sleep(5)

        with  open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/image-service.txt", "w") as img_serv:    
            img_serv.write('')
