def prime_test(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print(num,"It is not a prime number.");
                break
        else:
            print(num,"It is a prime number. ");
    else:
        print(num,"number entered only positive. ");

num = int(input("Enter to check prime number or not. "))
prime_test(num)        
