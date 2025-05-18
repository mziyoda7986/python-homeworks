def convert_cel_to_far(cel):
    return round(cel*9/5+32, 2)

def convert_far_to_cel(far):
    return round((far-32)*5/9, 2)

x = float(input("Enter a temperature in degrees F: "))
ans = convert_far_to_cel(x)
print(f"{x} degrees F = {ans} degrees C")
x = float(input("Enter a temperature in degrees C: "))
ans = convert_cel_to_far(x)
print(f"{x} degrees C = {ans} degrees F")