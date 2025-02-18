import csv
import os
import time

# CSV file ko list mein read karna
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data_list = list(reader)

# CSV mein se package name nikalna (assume karte hain pehla column package name ka hai)
package_names = [row[0] for row in data_list]

# User se start aur end input lena
start_index = int(input(f"Enter Start app :-")) 
end_index = int(input(f"Enter End app :- "))

# User se sleep time ka input lena (milliseconds mein)
sleep_time = int(input("Kitna time baad app ko open karna hai (in seconds): "))

# Loop chalana aur app open karna
for i in range(start_index, end_index + 1):
    try:
        package_name = package_names[i-1]
        print(f"Opening app with package name: {package_name}")
        
        # App ko open karna
        os.system(f'am start -n {package_name}/org.cocos2dx.javascript.AppActivity')
        
        # Sleep time
        time.sleep(sleep_time)
    except:
        pass

print("Process complete.")
