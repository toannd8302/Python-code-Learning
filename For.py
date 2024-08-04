
def main():
    print("This is the for.py file.")
    #Looping through a range of numbers and dont care about the index
    for _ in range(5):
     print('hello')
    #Looping through a range of numbers and print the index
    #for i in range(5):
     #print(i) 
     
     # Using Break
     for i1 in range(10):
       if i1 == 5 :
         break
       print('Giá trị i là: ',i1)
    # Using Continue
    for i2 in range(10): 
       if i2 == 5 :
         continue
       print('Giá trị i là: ',i2)   # 0,1,2,3,4,6,7,8,9
       
if __name__ == "__main__": main()