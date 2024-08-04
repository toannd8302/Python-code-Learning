
def main():
    #Initialize the number to calculate the factorial 4! = 4*3*2*1
    num = 4 
    result = 1
    #Calculate the factorial
    for i in range(1,5):
        result = result * i
    print(result)
if __name__== "__main__": main()