import pywhatkit
from my_secrets import my_num

pywhatkit.sendwhatmsg(my_num, "I am sending u this message using Python. I could totes abuse it with a for loop of A N U S", 18, 38, 10, True, 2)
# Last two parameters will close the tab/window after 2 seconds but that causes issues if you have more than one tab with it open

# Groups

group_id = input("Enter group ID: ")
pywhatkit.sendwhatmsg_to_group(group_id, "Test group", 18, 45)