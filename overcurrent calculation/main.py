import os

os.system(functions.py)         

def main():
    curves = ["A", "B", "C", "D"] 
   
   

    while True:
        x = float(input("psm: ")) 
        y = float(input("tms: "))
        curve = input("Please enter curve type (option from 'A' to 'D')").upper()
        
        if curve in curves:
            break
        else:
            print("Invalid input")



    if curve == "A":
        print(float(standard_inverse(x,y)))
    if curve == "B":
        print(float(very_inverse(x,y)))
    if curve == "C":
        print(float(extremely_inverse(x,y)))
    if curve == "D":
        print(float(long_time_inverse(x,y)))
     
if __name__=="__main__":
    main()















