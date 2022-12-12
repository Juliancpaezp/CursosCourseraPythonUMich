def computepay(hours, rate):
    if hours > 40:
        extra = hours - 40
        payment = (40 * rate) + (extra * rate * 1.5)
    else:
        payment = hours * rate
    return payment

############################
hours = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Friend,  Mind your fingers!")
    quit()

pay = computepay(hours, rate)

print("Pay", pay)
