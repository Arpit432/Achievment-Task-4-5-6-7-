import re


def tempconversion(temp,TU):
    if TU == 'c':
        R=((9*temp)/5+32)
    elif TU == 'f':
        R =((temp-32)*5/9)
    return R
def speedconversion(SP,SU):
    if SU == 'kmh':
        r=0.6214 * SP
    elif SU == 'mph':
        r=1.60934 * SP
    return r

def main():
    print("---------------Unit Convertion---------------")
    print("1: Temperature")
    print("2: Speed")
    option = int(input("What do you want to convert: "))
    if option ==1:
        t = float(input("Put the temperature you want to convert in there: "))
        TU = input("Type the temperature in the current unit: ")                  
        TU = TU.strip().lower()
        print("temperature after Conversion:: {:.2f}".format(tempconversion(t, TU)))
    elif option ==2:
        s = float(input("Put the speed you want to convert in there: "))
        SU = input("Type the speed in the current unit (kmh/mph): ")
        SU = SU.strip().lower()
        print("speed after conversion:: {:.3f}".format(speedconversion(s, SU)))
    else:
        print(" Opps ! Error")
main()


