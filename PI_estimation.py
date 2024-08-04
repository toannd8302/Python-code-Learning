def main():
    #Gregory-Leibniz Series
    n = 1000 #with n >1000, the result is more accurate
    PI = 0
    for i in range(1, n+1, 1):
        PI = PI + ( ((-1) ** (i+1)) / (2*i-1) )
    PI = 4 * PI
    print("Estimated PI is: ",PI) # ~3.140592653839794

    #Nilakantha Series
    
if __name__ == "__main__":main()