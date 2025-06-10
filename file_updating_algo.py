# Assign the file name to the variable import_file
import_file = "allow_list.txt"

# Assign a list of IP addresses that should be removed to the variable remove_list
remove_list = ["192.168.0.1", "10.0.0.2"]

# Open the file that contains the allow list
with open(import_file, "r") as file:
    # Read the file contents and assign to the variable ip_addresses
    ip_addresses = file.read()

# Convert the string into a list
ip_addresses = ip_addresses.split()

# Iterate through the remove list
for element in remove_list:
    # If element is in ip_addresses, remove it
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert the list back into a string with each IP on a new line
ip_addresses = "\n".join(ip_addresses)

# Write the updated list back to the file
with open(import_file, "w") as file:
    file.write(ip_addresses)
