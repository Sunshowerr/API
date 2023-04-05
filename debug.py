import time
import os
while True :
    start = "00"
    while start == "00":
        logic =str(input("select path"))
        #Define the directory path
        directory_path = r"D:\Main\Fix_val"
        filename = "debug01.txt"
        # Create the directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)

        # Define the complete file path
        file_path = os.path.join(directory_path, filename)

        # Write data to the file
        with open(file_path, "w") as file:
            file.write(logic)
        start = str(input("press 99 to start"))
                
    while start=="99" :
        message = str(input("select yor number press 88 to exit"))
        # Define the directory path
        directory_path = r"D:\Main\Fix_val"
        filename = "debug02.txt"
        # Create the directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)

        # Define the complete file path
        file_path = os.path.join(directory_path, filename)

        # Write data to the file
        with open(file_path, "w") as file:
            file.write(message)
        # Read data from the file and manipulate it
        time.sleep(1)
        with open(file_path, "r") as file:
            re_message = file.read()
            new_message = re_message.replace(message, "0")
        with open(file_path, "w") as file:
            file.write(new_message)
        if message == "88":
            start = "00"
           
            #Reset val
            if start == "00" :
                directory_path = r"D:\Main\Fix_val"
                filename = "debug01.txt"
                # Create the directory if it doesn't exist
                os.makedirs(directory_path, exist_ok=True)

                # Define the complete file path
                file_path = os.path.join(directory_path, filename)
                
                # Write data to the file
                with open(file_path, "w") as file:
                    file.write(logic)
                # Read data from the file and manipulate it
                with open(file_path, "r") as file:
                    re_message = file.read()
                    new_message = re_message.replace(logic, "0")
                with open(file_path, "w") as file:
                    file.write(new_message)   

    
        

        
