# WAP to conver name to title case

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

def title_case(first, last):
    full_name = first + " " + last
    title_name = full_name.title()
    return title_name

print(title_case(first = f_name, last = l_name))