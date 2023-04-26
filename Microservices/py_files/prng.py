import time
import random

while True:
        
    time.sleep(1)
    with open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/prng-service.txt", 'r') as prng:
        test = prng.read()
    
    if test == 'run':
        num = random.randint(0,500)
        with open("/Users/peterorndoff/Desktop/CS361/A2Microservices/text_docs/prng-service.txt", 'w') as doc:
            doc.write(str(num))

