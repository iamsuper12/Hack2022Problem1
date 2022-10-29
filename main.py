
print("Shelter 1 information")
print("Input your city below")
city = input()
print("Input your shelter name below")
sheltername = str(input())
print("Input your shelter's zipcode below")
shelterzipcode = input()
print("Input your shelter's address below")
shelteraddress = input()
print("Input your shelters phone number below")
shelterphonenumber = input()
print("Input the capacity in your shelter")
sheltercapacity = input()

print("Shelter 2 information")
print("Input your city below")
city2 = input()
print("Input your shelter name below")
sheltername2 = input()
print("Input your shelter's zipcode below")
shelterzipcode2 = input()
print("Input your shelter's address below")
shelteraddress2 = input()
print("Input your shelters phone number below")
shelterphonenumber2 = input()
print("Input the capacity in your shelter")
sheltercapacity2 = input()



print("If you are an evacuee, please enter your first and last name")
name = input()
print("Input your zipcode below")
zipcode = input()
print("Input the amount of people in your group")
people = input()
print("Input your phone number so we can contact you below")
phonenum = input()

if zipcode == shelterzipcode:
  print("Shelter " + sheltername + " is available")
if zipcode == shelterzipcode2:
  print("Shelter " + sheltername2 + " is available")
if zipcode !=shelterzipcode and zipcode != shelterzipcode2:
  print("There are no shelters available near you")


