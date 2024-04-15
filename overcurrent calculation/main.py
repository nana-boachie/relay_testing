import functions       

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
        print(float(functions.standard_inverse(x,y)))
    if curve == "B":
        print(float(functions.very_inverse(x,y)))
    if curve == "C":
        print(float(functions.extremely_inverse(x,y)))
    if curve == "D":
        print(float(functions.long_time_inverse(x,y)))
     
if __name__=="__main__":
    main()















