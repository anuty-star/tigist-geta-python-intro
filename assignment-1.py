#section 1
name = "Tigist"
age = 35
height = 5.3
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#section 2
name = input("please enter your name: ")
year_of_birth = input("please enter a year you were born: ")
conv_age = int(year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f"Hi {name}! you are approximately {age}.")

#section 3
number_1 = input("please enter number: ")
number_2 = input("please enter number: ")
new_number_1 = float(number_1)
new_number_2 = float(number_2)
total = new_number_1 * new_number_2
print(f"the product is {total}")

#section 4
item = "Jacket"
price = 60.09
quantity = 2
total = price * quantity

print("===========================")
print("         RECEIPT           ")
print("===========================")
print(f"item: {item}")
print(f"price: ${price:.2f}")
print(f"quantity: {quantity}")
print("---------------------------")
print(f"total: ${total:.2f}")
print("===========================")

#section 5
name = input("please enter your name: ")
hometown = input("please enter your hometown: ")
hobby = input("please enter your hobby: ")
fun_fact = input("please enter one fun fact about yourself: ")
birth_year = input("please enter your birth year: ")
conv_age = int(birth_year)
current_year = 2026
age = current_year - conv_age


print("___________________________")
print(f"    PROFILE: {name}   ")
print("___________________________")
print(f"Hometown: {hometown}")
print(f"Hobby:    {hobby}   ")
print(f"Fun fact: {fun_fact} ")
print(f"Age:      {age}      ")
