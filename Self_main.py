import tkinter as tk
import os
from tkinter import*
from tkinter import filedialog
import shutil
import time

#from all_button import button_logic as bl

#from winlist import File_window 



class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title( "my_project"+ "-tracking")
        self.master.geometry("500x500+300+5")
        self.place()
        self.create_widgets()
    
    def create_widgets(self):
        # create a menu bar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # add a new project command to the file menu
        file_menu.add_command(label="New Project", command=self.new_project)
        # add a open command to the file menu
        file_menu.add_command(label="Open Projeect", command=self.open_project)
        # add a save command to the file menu
        file_menu.add_command(label="Save", command=self.save_project)    
        
    def new_project(self):
        #create folder as newproject
        folder_path = r"D:\Main"
        # get the folder name from the user
        folder_name = tk.simpledialog.askstring("New project Name", "Enter a name for the new project")
        

        # create the new folder
        if folder_path and folder_name:
            new_folder_path = os.path.join(folder_path, folder_name)
            os.makedirs(new_folder_path)

            # show a message to the user
            message = f"Folder '{folder_name}' created in {folder_path}"
            tk.messagebox.showinfo("Project Created", message)
            self.master.title( folder_name+ "-tracking")
            #add Lable
            Label(self.master,text="select an object").place(x=210,y=0)
         #create sub folder0-10
            for i in range(11): 
                subfolder_name = f"Object#{i}"
                subfolder_path = os.path.join(new_folder_path,subfolder_name)
                os.makedirs(subfolder_path)
        #copy/clone original file 
        og = r"D:\Main\Fix_val\test1.robo"
        tg = os.path.join(new_folder_path,f"#{folder_name}#.robo")
        shutil.copyfile(og, tg)
        os.startfile(f"{tg}")
        #show button command
        def show_button():
            selection = dropdown.get()
            if selection == "             1              " :
                button1.place(x=150,y=60)
                confirm_1.place(x=350,y=60)
                button_add1.place(x=200,y=60)
                button2.place_forget()
                button3.place_forget()
                button4.place_forget()
                button5.place_forget()
                button6.place_forget()
                button7.place_forget()
                button8.place_forget()
                button9.place_forget()
                button10.place_forget()
                button_add2.place_forget()
                button_add3.place_forget()
                button_add4.place_forget()
                button_add5.place_forget()
                button_add6.place_forget()
                button_add7.place_forget()
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()
                confirm_2.place_forget()
                confirm_3.place_forget()
                confirm_4.place_forget()
                confirm_5.place_forget()
                confirm_6.place_forget()
                confirm_7.place_forget()
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
            elif selection == "             2              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button3.place_forget()
                button4.place_forget()
                button5.place_forget()
                button6.place_forget()
                button7.place_forget()
                button8.place_forget()
                button9.place_forget()
                button_add3.place_forget()
                button_add4.place_forget()
                button_add5.place_forget()
                button_add6.place_forget()
                button_add7.place_forget()
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()
                button10.place_forget()
                confirm_3.place_forget()
                confirm_4.place_forget()
                confirm_5.place_forget()
                confirm_6.place_forget()
                confirm_7.place_forget()
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
            elif selection == "             3              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place_forget()
                button5.place_forget()
                button6.place_forget()
                button7.place_forget()
                button8.place_forget()
                button9.place_forget()
                button10.place_forget()
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place_forget()
                confirm_5.place_forget()
                confirm_6.place_forget()
                confirm_7.place_forget()
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place_forget()
                button_add5.place_forget()
                button_add6.place_forget()
                button_add7.place_forget()
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()
            elif selection == "             4              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place(x=150,y=180)
                button5.place_forget()
                button6.place_forget()
                button7.place_forget()
                button8.place_forget()
                button9.place_forget()
                button10.place_forget()
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place(x=350,y=180)
                confirm_5.place_forget()
                confirm_6.place_forget()
                confirm_7.place_forget()
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place(x=200,y=180)
                button_add5.place_forget()
                button_add6.place_forget()
                button_add7.place_forget()
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()
            elif selection == "             5              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place(x=150,y=180)
                button5.place(x=150,y=220)
                button6.place_forget()
                button7.place_forget()
                button8.place_forget()
                button9.place_forget()
                button10.place_forget()
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place(x=350,y=180)
                confirm_5.place(x=350,y=220)
                confirm_6.place_forget()
                confirm_7.place_forget()
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place(x=200,y=180)
                button_add5.place(x=200,y=220)
                button_add6.place_forget()
                button_add7.place_forget()
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()
            elif selection == "             6              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place(x=150,y=180)
                button5.place(x=150,y=220)
                button6.place(x=150,y=260)
                button7.place_forget()
                button8.place_forget()
                button9.place_forget()
                button10.place_forget()
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place(x=350,y=180)
                confirm_5.place(x=350,y=220)
                confirm_6.place(x=350,y=260)
                confirm_7.place_forget()
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place(x=200,y=180)
                button_add5.place(x=200,y=220)
                button_add6.place(x=200,y=260)
                button_add7.place_forget()
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()
            elif selection == "             7              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place(x=150,y=180)
                button5.place(x=150,y=220)
                button6.place(x=150,y=260)
                button7.place(x=150,y=300)
                button8.place_forget()
                button9.place_forget()
                button10.place_forget()
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place(x=350,y=180)
                confirm_5.place(x=350,y=220)
                confirm_6.place(x=350,y=260)
                confirm_7.place(x=350,y=300)
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place(x=200,y=180)
                button_add5.place(x=200,y=220)
                button_add6.place(x=200,y=260)
                button_add7.place(x=200,y=300)
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()
            elif selection == "             8              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place(x=150,y=180)
                button5.place(x=150,y=220)
                button6.place(x=150,y=260)
                button7.place(x=150,y=300)
                button8.place(x=150,y=340)
                button9.place_forget()
                button10.place_forget()
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place(x=350,y=180)
                confirm_5.place(x=350,y=220)
                confirm_6.place(x=350,y=260)
                confirm_7.place(x=350,y=300)
                confirm_8.place(x=350,y=340)
                confirm_9.place_forget()
                confirm_10.place_forget()
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place(x=200,y=180)
                button_add5.place(x=200,y=220)
                button_add6.place(x=200,y=260)
                button_add7.place(x=200,y=300)
                button_add8.place(x=200,y=340)
                button_add9.place_forget()
                button_add10.place_forget()
            elif selection == "             9              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place(x=150,y=180)
                button5.place(x=150,y=220)
                button6.place(x=150,y=260)
                button7.place(x=150,y=300)
                button8.place(x=150,y=340)
                button9.place(x=150,y=380)
                button10.place_forget()
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place(x=350,y=180)
                confirm_5.place(x=350,y=220)
                confirm_6.place(x=350,y=260)
                confirm_7.place(x=350,y=300)
                confirm_8.place(x=350,y=340)
                confirm_9.place(x=350,y=380)
                confirm_10.place_forget()
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place(x=200,y=180)
                button_add5.place(x=200,y=220)
                button_add6.place(x=200,y=260)
                button_add7.place(x=200,y=300)
                button_add8.place(x=200,y=340)
                button_add9.place(x=200,y=380)
                button_add10.place_forget()
                
            elif selection == "             10              ":
                button1.place(x=150,y=60)
                button2.place(x=150,y=100)
                button3.place(x=150,y=140)
                button4.place(x=150,y=180)
                button5.place(x=150,y=220)
                button6.place(x=150,y=260)
                button7.place(x=150,y=300)
                button8.place(x=150,y=340)
                button9.place(x=150,y=380)
                button10.place(x=150,y=420)
                button_add1.place(x=200,y=60)
                button_add2.place(x=200,y=100)
                button_add3.place(x=200,y=140)
                button_add4.place(x=200,y=180)
                button_add5.place(x=200,y=220)
                button_add6.place(x=200,y=260)
                button_add7.place(x=200,y=300)
                button_add8.place(x=200,y=340)
                button_add9.place(x=200,y=380)
                button_add10.place(x=200,y=420)
                confirm_1.place(x=350,y=60)
                confirm_2.place(x=350,y=100)
                confirm_3.place(x=350,y=140)
                confirm_4.place(x=350,y=180)
                confirm_5.place(x=350,y=220)
                confirm_6.place(x=350,y=260)
                confirm_7.place(x=350,y=300)
                confirm_8.place(x=350,y=340)
                confirm_9.place(x=350,y=380)
                confirm_10.place(x=350,y=420)
            else:
                button1.place_forget()
                button2.place_forget()
                button3.place_forget()
                button4.place_forget()
                button5.place_forget()
                button6.place_forget()
                button7.place_forget()
                button8.place_forget()
                button9.place_forget()
                button10.place_forget()
                confirm_1.place_forget()
                confirm_2.place_forget()
                confirm_3.place_forget()
                confirm_4.place_forget()
                confirm_5.place_forget()
                confirm_6.place_forget()
                confirm_7.place_forget()
                confirm_8.place_forget()
                confirm_9.place_forget()
                confirm_10.place_forget()
                button_add1.place_forget()
                button_add2.place_forget()
                button_add3.place_forget()
                button_add4.place_forget()
                button_add5.place_forget()
                button_add6.place_forget()
                button_add7.place_forget()
                button_add8.place_forget()
                button_add9.place_forget()
                button_add10.place_forget()

        #update for add button
        def update_file(filename,message):
            # Define the directory path
            directory_path = r"D:\Main\Fix_val"

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
          
    
        #"setting"button command        
        def bt1(): 
            update_file("add1.txt","1")
        def bt2():
            update_file("add2.txt","1")
        def bt3():
            update_file("add3.txt","1")
        def bt4():
            update_file("add4.txt","1")
        def bt5():
            update_file("add5.txt","1")
        def bt6():
            update_file("add6.txt","1")
        def bt7():
            update_file("add7.txt","1")
        def bt8():
            update_file("add8.txt","1")
        def bt9():
            update_file("add9.txt","1")
        def bt10():
            update_file("add10.txt","1") 

        #setting button command   
        def set_bt1():
            update_file("setting1.txt","1")  
        def set_bt2():
            update_file("setting2.txt","1")
        def set_bt3():
            update_file("setting3.txt","1")
        def set_bt4():
            update_file("setting4.txt","1")
        def set_bt5():
            update_file("setting5.txt","1")
        def set_bt6():
            update_file("setting6.txt","1")
        def set_bt7():
            update_file("setting7.txt","1")
        def set_bt8():
            update_file("setting8.txt","1")
        def set_bt9():
            update_file("setting9.txt","1")
        def set_bt10():
            update_file("setting10.txt","1")

        def start():
            update_file("Start.txt",1)

        def confirm1():
            print("add1"+"success")   
        def confirm2():
            print("add2"+"success")
        def confirm3():
            print("add3"+"success")
        def confirm4():
            print("add4"+"success")
        def confirm5():
            print("add1"+"success")     
        def confirm6():
            print("add2"+"success")
        def confirm7():
            print("add3"+"success")
        def confirm8():
            print("add4"+"success")
        def confirm9():
            print("add3"+"success")
        def confirm10():
            print("add4"+"success")
        
           
        dropdown = StringVar(self.master)
        dropdown.set("Select an option")
        options = ["             1              ", "             2              ", "             3              ", "             4              ","             5              ", "             6              ", "             7              ", "             8              ","             9              ", "             10              "]
        dropdown_menu = OptionMenu(self.master, dropdown, *options)
        dropdown_menu.place(x=185,y=20)
        #button command
        button1 = Button(self.master, text="setting",command=set_bt1)
        button2 = Button(self.master, text="setting",command=set_bt2)
        button3 = Button(self.master, text="setting",command=set_bt3)
        button4 = Button(self.master, text="setting",command=set_bt4)
        button5 = Button(self.master, text="setting",command=set_bt5)
        button6 = Button(self.master, text="setting",command=set_bt6)
        button7 = Button(self.master, text="setting",command=set_bt7)
        button8 = Button(self.master, text="setting",command=set_bt8)
        button9 = Button(self.master, text="setting",command=set_bt9)
        button10 = Button(self.master, text="setting",command=set_bt10)
        #add button command
        button_add1 = Button(self.master, text="add Obj1",command=bt1)
        button_add2 = Button(self.master, text="add Obj2",command=bt2)
        button_add3 = Button(self.master, text="add Obj3",command=bt3)
        button_add4 = Button(self.master, text="add Obj4",command=bt4)
        button_add5 = Button(self.master, text="add Obj5",command=bt5)
        button_add6 = Button(self.master, text="add Obj6",command=bt6)
        button_add7 = Button(self.master, text="add Obj7",command=bt7)
        button_add8 = Button(self.master, text="add Obj8",command=bt8)
        button_add9 = Button(self.master, text="add Obj9",command=bt9)
        button_add10 = Button(self.master, text="add Obj10",command=bt10)
        
        confirm_1= Button(self.master, text="ok",command=confirm1)
        confirm_2= Button(self.master, text="ok",command=confirm2)
        confirm_3= Button(self.master, text="ok",command=confirm3)
        confirm_4= Button(self.master, text="ok",command=confirm4)
        confirm_5= Button(self.master, text="ok",command=confirm5)
        confirm_6= Button(self.master, text="ok",command=confirm6)
        confirm_7= Button(self.master, text="ok",command=confirm7)
        confirm_8= Button(self.master, text="ok",command=confirm8)
        confirm_9= Button(self.master, text="ok",command=confirm9)
        confirm_10= Button(self.master, text="ok",command=confirm10)

        #ok button command
        ok_button = Button(self.master, text="OK", command=show_button,bg="brown")
        ok_button.place(x=320,y=23)

        #start button
        btn_strat = Button(self.master,text="Strat",command=start,bg="green")
        btn_strat.place(x=370,y=23)
            
       
    def open_project(self):
        # create a dialog to select a project folder
        folder_path = filedialog.askdirectory(title="Select Project Folder")

        # if a folder is selected
        if folder_path:
            # get the project name from the folder path
            project_name = os.path.basename(folder_path)

            # show a message to the user
            message = f"Opening project '{project_name}' from {folder_path}"
            tk.messagebox.showinfo("Open Project", message)

            # set the window title to the project name
            self.master.title(project_name + "-tracking")

            # add a label to the window
            Label(self.master, text="Select an object").place(x=210, y=0)
            for i in range(11):
                project_path = f"D:\Main\{project_name}\Object#1" 
                # define the folder to search and the item to find
                item_to_find = "add1.txt"

            # search for the item in the first subfolder
            subfolder_path = os.path.join(project_path)
            if item_to_find in os.listdir(subfolder_path):
                # create a button if the item is found
                tk.Button(self.master, text="Item Found!", command=lambda: print("Button Clicked!")).pack() 
        
        
        
    def save_project(self):
          # allow the user to select a folder
        print("This project has Save ")
   

