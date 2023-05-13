import os
import re
import tkinter as tk
from tkinter import filedialog
import logging
import datetime
import subprocess

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Create a file handler to output logs to a file
log_file = "output.log"
file_handler = logging.FileHandler(log_file, mode='w')
# Create a formatter to format log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# Add the file handler to the logger
logger.addHandler(file_handler)
# Create a stream handler to output logs to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
# Use the logger to log messages
logger.info("Program started")

class FileRenamer:
    def browse_sourcerunning_dir(self):
        self.sourcerunning_dir = filedialog.askdirectory()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, self.sourcerunning_dir)      
    def browse_destrunning_dir(self):
        destrunning_dir = filedialog.askdirectory()
        today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        self.destrunning_dir = os.path.join(destrunning_dir, today)
        os.makedirs(self.destrunning_dir, exist_ok=True)
        self.dest_entry.delete(0, tk.END)
        self.dest_entry.insert(0, self.destrunning_dir)         
    def browse_sourcenames_dir(self):
        self.sourcenames_dir = filedialog.askdirectory()
        self.names_entry.delete(0, tk.END)
        self.names_entry.insert(0, self.sourcenames_dir)
    def browse_destname_dir(self):
        destname_dir = filedialog.askdirectory()
        today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        self.destname_dir = os.path.join(destname_dir, today)
        os.makedirs(self.destname_dir, exist_ok=True)
        self.destname_entry.delete(0, tk.END)
        self.destname_entry.insert(0, self.destname_dir)
                
    def compare_directories(self, directory1, directory2):
        winmerge_path = "C:/Program Files/WinMerge/WinMergeU.exe"        # change the path to match the location of WinMerge on your system
        command = f"{winmerge_path} {directory1} {directory2}"
        subprocess.Popen(command)
        
    def regex_selector(self):
        option_menu = tk.OptionMenu(self.master, self.selected_option, *self.options)
        option_menu.grid (row=1, column=1, padx=5, pady=5)   
        
    def __init__(self, master):
        self.master = master
        master.title("File Renamer")
        #Create directories variable
        self.sourcerunning_dir = ''
        self.sourcenames_dir = ''
        self.destrunning_dir = ''
        self.destname_dir = ''
        options = ['host-name name1;', 'hostname "name2"', 'host-name "name3"', 'hostname name4']

        #Create counter variables
        self.RunningRenamedCounter = 0
        self.RunningTotalCounter=0
        self.TxtRenamedCounter = 0
        self.TxtTotalCounter=0
        
        #Create selector label
        self.searchcrit = tk.Label(self.master, text="Select search criteria" )
        self.searchcrit.grid(row=0, column=1, ipadx=5, pady=5)  
               
        #Create Directory selectors
        #Create Name.txt directory and button 
        self.source_label = tk.Label(master, text="Name.txt Directory:", fg='blue')
        self.source_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.source_entry = tk.Entry(master, width=50)
        self.source_entry.grid(row=2, column=1, padx=5, pady=5)
        self.source_button = tk.Button(master, text="Browse", command=self.browse_sourcerunning_dir, fg='blue')
        self.source_button.grid(row=2, column=2, padx=5, pady=5)
        
        self.dest_label = tk.Label(master, text="Output Name.txt Directory:", fg='blue')
        self.dest_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.dest_entry = tk.Entry(master, width=50)
        self.dest_entry.grid(row=3, column=1, padx=5, pady=5)
        self.dest_button = tk.Button(master, text="Browse", command=self.browse_destrunning_dir, fg='blue')
        self.dest_button.grid(row=3, column=2, padx=5, pady=5)
        
        self.rename_button = tk.Button(master, text="Rename Name.txt Files", command=self.rename_running_files, fg='blue')
        self.rename_button.grid(row=4, column=1, padx=5, pady=5)
        
        # Create a label widget to display the counter for Name.txt renamed
        self.countlabel = tk.Label(self.master, text="Renamed Name.txt Files", fg='blue' )
        self.countlabel.grid(row=5, column=0, ipadx=5, pady=5, sticky='w') 
        self.label = tk.Label(self.master, text=f"{self.RunningRenamedCounter} out of {self.RunningTotalCounter}", fg='blue')
        self.label.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        
        #Create Names directory and button 
        self.names_label = tk.Label(master, text="Name.cfg Directory:", fg='red')
        self.names_label.grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.names_entry = tk.Entry(master, width=50)
        self.names_entry.grid(row=6, column=1, padx=5, pady=5)
        self.names_button = tk.Button(master, text="Browse", command=self.browse_sourcenames_dir, fg='red')
        self.names_button.grid(row=6, column=2, padx=5, pady=5)
        
        self.destname_label = tk.Label(master, text="Output Name.cfg Directory:", fg='red')
        self.destname_label.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.destname_entry = tk.Entry(master, width=50)
        self.destname_entry.grid(row=7, column=1, padx=5, pady=5)
        self.destname_button = tk.Button(master, text="Browse", command=self.browse_destname_dir, fg='red')
        self.destname_button.grid(row=7, column=2, padx=5, pady=5)
        
        self.rename_buttonNAMES = tk.Button(master, text="Rename Name.cfg Files", command=self.rename_txt_files, fg='red')
        self.rename_buttonNAMES.grid(row=8, column=1, padx=5, pady=5)
        
        # Create a label widget to display the counter for Names Directory
        self.countlabelNAMES = tk.Label(self.master, text="Renamed Name.cfg Files" , fg='red')
        self.countlabelNAMES.grid(row=9, column=0, ipadx=5, pady=5, sticky='w') 
        self.labelNAMES = tk.Label(self.master, text=f"{self.TxtRenamedCounter} out of {self.TxtTotalCounter}", fg='red')
        self.labelNAMES.grid(row=9, column=1, padx=5, pady=5, sticky='w')
        
        #Create winmerge button 
        self.winmerge_button = tk.Button(master, text="Compare Destinations in WinMerge", command=self.launch_winmerge, fg='black')
        self.winmerge_button.grid(row=10, column=1, padx=5, pady=5)       
        
        
        #Create regex options
        self.options = options
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])
        self.regex_selector()

           
    def rename_running_files(self):
        renamed = False
        self.RunningRenamedCounter=0
        self.RunningTotalCounter=0   
        selected_value = self.selected_option.get()
        if selected_value == 'host-name name1;':
            selected_search = r'host-name\s+(\S+);'
        elif selected_value == 'hostname "name2"':
            selected_search = r'hostname\s+"(\S+)"'
        elif selected_value == 'host-name "name3"':
            selected_search = r'host-name\s+"(\S+)"'           
        elif selected_value == 'hostname name4':
            selected_search = r'hostname\s+\"?(\S+?)\"'
        if  self.sourcerunning_dir and self.destrunning_dir:
            # Loop through all the subdirectories in the source directory
            for subdir, dirs, files in os.walk(self.sourcerunning_dir):
                for filename in files:
                    if filename.endswith('.txt'):
                        # Extract the hostname from the file
                        with open(os.path.join(subdir, filename), 'r') as f:
                            config = f.read()
                        hostname_pattern = selected_search
                        hostname_match = re.search(hostname_pattern, config)
                        self.RunningTotalCounter +=1
                        if hostname_match:
                            hostname = hostname_match.group(1)
                            self.RunningRenamedCounter +=1  
                            # Make a copy of the file with the new hostname and move it to the destination directory
                            new_filename = f"{hostname}.txt"
                            source_path = os.path.join(subdir, filename)
                            dest_path = os.path.join(self.destrunning_dir, new_filename)
                            with open(source_path, 'r') as f:
                                config = f.read()
                            with open(dest_path, 'w') as f:
                                f.write(config)
                            logger.info(f"Renamed {source_path} to {dest_path}")
                            renamed = True
                        else:
                            source_path = os.path.join(subdir, filename)
                            logger.info(f"Didn't change {source_path}")  
            #Show in log
            logger.info(f"Total Files in directory {self.RunningTotalCounter}")
            logger.info(f"Renamed Files {self.RunningRenamedCounter}")
            #Display number of processed files in GUI
            self.label.config(text=f"{self.RunningRenamedCounter} out of {self.RunningTotalCounter}")
            # Display a message when done
            self.rename_button.config(text="Files renamed successfully!")
        else:
            # Display an error message if source or destination directory is not selected
            self.rename_button.config(text="Error: Please select source and destination directories.")
            
    def rename_txt_files(self):      
        renamed = False       
        self.TxtRenamedCounter=0
        self.TxtTotalCounter=0
        today = datetime.date.today().strftime("%Y-%m-%d")
        directory_path = os.path.join(self.destname_dir, today)
        selected_value = self.selected_option.get()
        if selected_value == 'host-name name1;':
            selected_search = r'host-name\s+(\S+);'
        elif selected_value == 'hostname "name2"':
            selected_search = r'hostname\s+"(\S+)"'
        elif selected_value == 'host-name "name3"':
            selected_search = r'host-name\s+"(\S+)"'           
        elif selected_value == 'hostname name4':
            selected_search = r'hostname\s+\"?(\S+?)\"'
        if self.sourcenames_dir and self.destname_dir:
            # Loop through all the subdirectories in the source directory
            for subdir, dirs, files in os.walk(self.sourcenames_dir):
                for filename in files:
                    if filename.endswith('.cfg'):
                        # Extract the hostname from the file
                        with open(os.path.join(subdir, filename), 'r') as f:
                            config = f.read()
                        hostname_pattern = selected_search
                        hostname_match = re.search(hostname_pattern, config)
                        self.TxtTotalCounter +=1
                        if hostname_match:
                            hostname = hostname_match.group(1)   
                            self.TxtRenamedCounter +=1                       
                            # Make a copy of the file with the new hostname and move it to the destination directory
                            new_filename = f"{hostname}.txt"
                            source_path = os.path.join(subdir, filename)
                            dest_path = os.path.join(self.destname_dir, new_filename)
                            with open(source_path, 'r') as f:
                                config = f.read()
                            with open(dest_path, 'w') as f:
                                f.write(config)
                            logger.info(f"Renamed {source_path} to {dest_path}")
                            renamed = True
                        else:
                            source_path = os.path.join(subdir, filename)
                            logger.info(f"Didn't change {source_path}") 
            #Show in log
            logger.info(f"Total Files in directory {self.TxtTotalCounter}")
            logger.info(f"Renamed Files {self.TxtRenamedCounter}")
            #Display number of processed files in GUI
            self.labelNAMES.config(text=f"{self.TxtRenamedCounter} out of {self.TxtTotalCounter}")
            # Display a message when done
            self.rename_buttonNAMES.config(text="Files renamed successfully!")
        else:
            # Display an error message if source or destination directory is not selected
            self.rename_buttonNAMES.config(text="Error: Please select source and destination directories.") 
            
    def launch_winmerge(self): 
        if self.destrunning_dir and self.destname_dir:
            directory1 = self.destrunning_dir
            directory2 = self.destname_dir
            self.compare_directories(directory1, directory2)
            self.winmerge_button .config(text="WinMerge opened!")
            logger.info("Winmerge opened")
        else:
            # Display an error message if source or destination directory is not selected
            self.winmerge_button .config(text="Error: Please select two destination directories.")
            logger.info("WinMerge missing directories to compare")
            
root = tk.Tk()
renamer = FileRenamer(root)
root.mainloop()
