GETTING STARTED:

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







RUNNGIN juniper_renamer.py:

Step1: Navigate to the directory where juniper_renamer.py is located

Step2: Right click in directory and select "Open in Terminal" for Windows 11 or "Open command window here" for Windows 10 

Step3: In the Command Prompt type the following:
	  python .\juniper_renamer.py
Step4: Select the source and destination directory. Customer directory is made up of additional directory containing running.txt files. Name.txt directory is the directory with multiple NAMES.txt files.

NOTE: The user does not have to select all four directory, but each pair needs to be chosen.

Step5: Click on the Rename Customer Files or Rename Name.txt Files button.
NOTE: If you didn't select a source and destination, the button will show an Error.

Step6: Check the counter to verify how many files were succesfully processesed. Check the output.log in the directory where juniper_renamer.py exists to identify the unnamed files.