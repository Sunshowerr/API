import tkinter
import customtkinter
from customtkinter import *
import os
import shutil
import tkinter.messagebox
import time
import socket

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.checkbox_checked=[False]*10
       
        # configure window
        self.title("Tracking")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        #logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        #creat newproject
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="New", command=self.new_project_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        #open project
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Open",command=self.open_project_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        #Save project
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Save",command=self.save_project_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Setting",command=lambda:self.update_file("Setting.txt","1"))
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        #theme 
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=30, pady=(10, 20))
        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("90%")
        
    def show_button(self):
        # create scaling_object_menu  frame
        self.object_menu = customtkinter.CTkFrame(self,width=90, corner_radius=10)
        self.object_menu.grid(row=0, column=3, rowspan=3, sticky="nsew")
        # create start button
        self.start_button_1 = customtkinter.CTkButton(master=self,text="start", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.start_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.change_state(self.start_button_1,0)
        
        #create logo in object menu frame
        self.logo_label = customtkinter.CTkLabel(self.object_menu, text="Add object", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=(60,0),  pady=(20, 10))

        self.scaling_object_menu = customtkinter.CTkOptionMenu(self.object_menu, values=["1", "2", "3", "4", "5","6", "7", "8", "9", "10"],
                                                            command=self.change_object_event)
        self.scaling_object_menu.grid(row=1, column=0, padx=(60,0), pady=(20,10))
        self.scaling_object_menu.set("1")
        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def change_object_event(self, new_value,*args):
        print(new_value)
        message = new_value
        directory_path = r"D:\fixVal"
        self.file_name ="temporary record.txt"
        # Create the directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)

        # Define the complete file path
        file_path = os.path.join(directory_path,self.file_name )

        # Write data to the file
        with open(file_path, "w") as file:
            file.write(message)
            
        # Remove all previous objects
        for widget in self.object_menu.winfo_children()[2:]:
            widget.destroy()
        # Create new objects based on the selected value
        for i in range(int(new_value)):
            button = customtkinter.CTkButton(
                master = self.object_menu, 
                text=f"Object {i+1}", 
                command=lambda obj_num=i+1: self.update_file(f"add.txt",str(obj_num))
            )
            button.grid(row=i+2, column=0, padx=(10,0), pady=0)

            checkbox = customtkinter.CTkCheckBox(
                master=self.object_menu,
                text="",
                command=lambda button = button , idx = i: self.change_state(button,idx) 
            )
            checkbox.grid(row=i+2, column=1, padx=(0,0), pady=5)
        
        self.checkbox_checked=[False]*int(new_value)
    
    def change_state(self, widget, idx):
        #chackbox check    
        self.start_button_1.configure(state=tkinter.DISABLED)   
        if widget.cget("state") == tkinter.NORMAL:
            widget.configure(state=tkinter.DISABLED)
            self.checkbox_checked[idx] = True
                      
        elif widget.cget("state") == tkinter.DISABLED:
            widget.configure(state=tkinter.NORMAL)
            self.checkbox_checked[idx] = False
            
        if False in self.checkbox_checked:
            self.start_button_1.configure(state=tkinter.DISABLED)
        else:
            self.start_button_1.configure(state=tkinter.NORMAL)

    def new_project_event(self):
        print("newproject")
        # create folder as newproject
        self.folder_path = r"D:"
        # get the folder name from the user
        self.folder_name = customtkinter.CTkInputDialog(text="insert name of New Project", title="New Project")

        # create the new folder
        self.project_name = self.folder_name.get_input()
        self.new_folder_path = os.path.join(self.folder_path, self.project_name)
        os.makedirs(self.new_folder_path)

        # show a message to the user
        message = f"Folder '{self.project_name}' created in {self.folder_path}/{self.project_name}"
        print(f"{message}")
        self.title(f"{self.folder_path}/{self.project_name} -Tracking")

        # save the project name to a text file
        save_path = os.path.join(self.new_folder_path, f"project_name Save.txt")
        with open(save_path, "w") as file:
            file.write(self.project_name)

        # copy/clone original file
        og = r"D:\fixVal\test1.robo"
        tg = os.path.join(self.new_folder_path, f"#{self.project_name}#.robo")
        #shutil.copyfile(og, tg)

        self.show_button()

        
    def update_file(self,filename, message):
        # Define the directory path
        directory_path = r"D:\fixVal"
        # Create the directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)
        # Define the complete file path
        file_path = os.path.join(directory_path, filename)
        # Write data to the file
        with open(file_path, "w") as file:
            file.write(message)
        # Read data from the file and manipulate it
        time.sleep(0.9)
        with open(file_path, "r") as file:
            re_message = file.read()
        new_message = re_message.replace(message, "0")
        with open(file_path, "w") as file:
            file.write(new_message)
        print(f"file{filename}has up to date {message}")
        
    def open_project_event(self):
        print("openproject")
        self.open_folder = customtkinter.filedialog.askdirectory()
        print(f"{self.open_folder}")
        
        # read the project name from the text file
        with open(f"{self.open_folder}/project_name Save.txt", "r") as file:
            self.project_name = file.read()
        select_path = os.path.join(self.open_folder, f"select {self.project_name} Save.txt")
        with open(select_path, "r") as file:
            self.project_selected = file.read()

        self.title(self.project_name +"-Tracking")
        self.show_button()
        self.scaling_object_menu.set(self.project_selected)
        self.change_object_event(self.project_selected)
        self.scaling_object_menu.configure(state=tkinter.DISABLED)
       

        
    def save_project_event(self):
        response = tkinter.messagebox.askyesnocancel(title="Save", message="If this file has saved, can't be able change again\nDo you wish to proceed? ",)
        # og = r"D:\fixVal\temporary record"
        # tg = os.path.join(self.new_folder_path, f"{self.project_name} Save.txt")
        # shutil.copyfile(og, tg)
        
        if response is None:
            # If the user clicked Cancel, do nothing
            return
        elif response:
        # If the user clicked Yes, proceed with saving
        # Save the file here
            self.scaling_object_menu.configure(state=tkinter.DISABLED)
            og = r"D:\fixVal\temporary record.txt"
            tg = os.path.join(self.new_folder_path, f"select {self.project_name} Save.txt")
            shutil.copyfile(og, tg)
            print("File saved.")
        else:
            # If the user clicked No, do not save the file
            print("File not saved.")
            return

    def button_command_enent(self,val):
        print(f"Button {val} clicked!")
        
    def sidebar_button_event(self):
        print("sidebar_button click")

   

if __name__ == "__main__":
    app = App()
    app.mainloop()