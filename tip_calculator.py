print("Enter the bill ")
bill=input()
bill_as_int=int(bill)
print("Enter the tip percentage")
tip_percentage=input()
tip_percentge_as_int=int(tip_percentage)
total=0
match tip_percentge_as_int:
    case 10:
        total=((10/100)*bill_as_int)+bill_as_int
        print(f"The total is {total}")
    case 12:
         total = ((12 / 100) * bill_as_int) + bill_as_int
         print(f"The total is {total}")
    case 12:
        total = ((15 / 100) * bill_as_int) + bill_as_int
        print(f"The total is {total}")
print("The no of persons you want to spit the bill with ")
no_of_persons=input()
no_of_persons_as_int=int(no_of_persons)
print(f"Per person will pay {round(total/no_of_persons_as_int,2)}")

pi=3.14