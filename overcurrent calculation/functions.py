#Overcurrent
def long_time_inverse(PSM,TMS):# overcurrent
    operating_time= TMS*(120/(((PSM))-1))
    return operating_time

def standard_inverse(PSM,TMS):# overcurrent
    operating_time= TMS*(0.14/(((PSM)^0.02)-1))
    return operating_time

def very_inverse(PSM,TMS):# overcurrent
    operating_time= TMS*(13.5/((PSM)-1))
    return operating_time

def extremely_inverse(PSM,TMS):# C
    operating_time= TMS*(80/(((PSM)^2)-1))
    return operating_time


#Distance 

