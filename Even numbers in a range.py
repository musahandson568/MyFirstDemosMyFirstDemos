#define starting and ending numbers
start_number=int(input("Enter the starting number :"))
end_number=int(input("Enter the Ending number :"))
# #validate statement above
# start_number=int(input("Enter the starting number :"))
# end_number=int(input("Enter the Ending number :"))
#Using while loop to check if the condition is true
while start_number>=end_number:
     print("Error! The starting number must be less than the Ending number.")
for start_number in range(start_number,end_number):
  if start_number % 2==0:
   print(start_number, end=",")


