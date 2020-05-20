"""
Take an input number from user
- Check if this number is divisble by 5 and 11 both, display divisible both.
- Check this number is divisble by 5 only, display divisible by 5 only.
- Check if this number is divisible by 11 only, display divisible by 11 only
- Check if this number is not divisble by 5 and 11 both, display not divisble by eithr 5 or 11

"""
print("DIVISIBILITY CHECK WITH 5 AND 11")
number = int(input("Enter a number ---> "))

if(number%5 == 0  and number%11 == 0 ):
    print(f"{number} is divisble by both 5 and 11.")
elif(number%5 == 0):
    print(f"{number} is divisble by 5 but not by 11")
elif(number%11 == 0):
    print(f"{number} is divisble by 11 but not by 5.")
else:
    print(f"{number} is not divisble by either 5 or 11")