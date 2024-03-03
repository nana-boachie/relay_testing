def standard_inverse(PSM,TMS):# A
    operating_time= TMS*(0.14/(((PSM)**0.02)-1))
    return operating_time

def very_inverse(PSM,TMS):# B
    operating_time= TMS*(13.5/((PSM)-1))
    return operating_time

def extremely_inverse(PSM,TMS):# C
    operating_time= TMS*(80/(((PSM)**2)-1))
    return operating_time

def long_time_inverse(psm,tms): #D
    operating_time=tms*(120/((psm)-1))
    return operating_time



def main():
    curves = [1,2,3,4]
    
    while True: 
        x = float(input("Enter PSM: "))
        y = float(input("Enter TMS: "))
        curve = int(input("Please enter curve type (option from 'A' to 'D'): "))
        
        if curve in curves:
            break
        else :
            return 0
       
    if curve == 1:
        print(float(standard_inverse(x, y)))
    elif curve == 2:
        print(float(very_inverse(x, y)))
    elif curve == 3:
        print(float(extremely_inverse(x, y)))
    elif curve == 4:
        print(float(long_time_inverse(x, y)))

if __name__ == "__main__":
    main()
