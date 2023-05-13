Running file_renamer.py:

Prerequisites: Verify python 3.10 or above is installed. Follow Getting Python below if missing. 

Step 1: Navigate to the directory where file_renamer.py is located

Step 2: Right click in directory and select "Open in Terminal" for Windows 11 or "Open command window here" for Windows 10 

Step 3: In the Command Prompt type the following:

	python.exe .\file_renamer.py

Step 4: Select search criteria which will be executed on the selected files. This can be changed at any point. 

Step 5: Select the source and destination directory. Name.txt directory is made up of files and directories containing Name.txt files. Name.cfg directory is the directory made up of files and directories containing Name.cfg files. The output directories will create a new directory with the current timestamp when the output directory is selected. 

NOTE: The user does not have to select all four directory, but each pair needs to be chosen.

Step 6: Click on the Rename Button in each respective section. 

NOTE: If you didn't select a source and destination, the button will show an Error.

Step 7: Check the counter to verify how many files were succesfully processesed. Check the output.log in the directory where file_renamer.py exists to identify the unnamed files.
<br>
<br>
<br>
Adding a search criteria:

Step 1: Line 69 has the criteria option, add your new criteria seperate by a comma and enclosed in a single quote. 

	Default: options = ['host-name name1;', 'hostname "name2"', 'host-name "name3"', 'hostname name4']
	
	Example with a new criteria: options = ['host-name name1;', 'hostname "name2"', 'host-name "name3"', 'hostname name4', 'search5 name5']
	
Step 2: Add the new match criteria in the rename_txt_files and rename_cfg_files definitions. Use the tools in the note below to create your search criteria. 
   
	Default:         
	if selected_value == 'host-name name1;':
            selected_search = r'host-name\s+(\S+);'
        elif selected_value == 'hostname "name2"':
            selected_search = r'hostname\s+"(\S+)"'
        elif selected_value == 'host-name "name3"':
            selected_search = r'host-name\s+"(\S+)"'           
        elif selected_value == 'hostname name4':
            selected_search = r'hostname\s+\"?(\S+?)\"'
   
	Example with new criteria: 	
	if selected_value == 'host-name name1;':
            selected_search = r'host-name\s+(\S+);'
        elif selected_value == 'hostname "name2"':
            selected_search = r'hostname\s+"(\S+)"'
        elif selected_value == 'host-name "name3"':
            selected_search = r'host-name\s+"(\S+)"'           
        elif selected_value == 'hostname name4':
            selected_search = r'hostname\s+\"?(\S+?)\"'
        elif selected_value == 'search5 name5':
            selected_search = r'search5\s+(\S+)'
	
	
NOTE: Use https://www.dataquest.io/blog/regex-cheatsheet/ to help you choose the correct regular expression and test it with https://regex101.com/
<br>
<br>
<br>
Getting Python:

Step 1: Install Python from the Microsoft Store

To download Python from the Microsoft Store, follow these steps:

    Open the Microsoft Store app on your Windows machine.
    Search for "Python" in the search bar at the top right corner of the app.
    Select the desired version of Python from the search results and click on "Get."
    Once the download and installation process is complete, click on "Launch" to start Python.

Step 2: Open the Command Prompt

To execute Python on a Windows machine, you need to use the Command Prompt. To open the Command Prompt, follow these steps:

    Open the Start menu and search for "Command Prompt."
    Click on "Command Prompt" to open it.

Step 3: Verify Your Python Installation

To verify that Python is installed and working correctly, type the following command in the Command Prompt:

    python --version 

This should display the version number of Python that you installed.
Step 4: Execute a Python Script

To execute a Python script, navigate to the directory where the script is located using the cd command. Once in the directory, type the following command:

    python scriptname.py

Replace scriptname.py with the name of your Python script.

