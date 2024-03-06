# Fetch Menu Data Script

This script fetches menu data from a JSON file obtained from a Swiggy API response and saves it to a CSV file.

#{Note, there are two scripts "working.py" and "original.py", please use working.py file and not original.py}
#(original.py file contain the code how the program should run but not able to find the swiggy api documentation)
#(working.py file is directly using the json file of swiggy API, not any request module)

### Instructions to Run the Script:
1. Make sure you have Python installed on your system.
2. Please create the virtual environment on Mac by running:
        ## Create a virtual environment named 'venv'
        python3 -m venv venv

        ## Activate the virtual environment
        source venv/bin/activate
    ## For creating on window 
        ## Create a virtual environment named 'venv'
        python -m venv venv

        ## Activate the virtual environment
        venv\Scripts\activate
3. Install the required packages by running: `pip install -r requirements.txt`.
4. Place the JSON file containing the Swiggy API response in the same directory as the script.
5. Run the script using the command: `python fetch_menu_data.py`.

### Script Functionality:
- The script loads the JSON file containing Swiggy API content.
- It extracts the menu details from the JSON file.
- The extracted data is converted into a CSV file using Pandas.

### Setup Steps:
- Ensure Python is installed on your system.
- Obtain the JSON file from the Swiggy API response.
- Install required packages using `pip install -r requirements.txt`.

### Evaluation Criteria:
- **Functionality:** The script successfully fetches and extracts menu data for a given JSON file.
- **Code Quality:** The code is well-structured, commented, and adheres to best practices.
- **Error Handling:** The script gracefully handles potential errors, such as invalid JSON format or missing data.
- **Output:** The CSV file is correctly formatted and contains all relevant menu data in an organized manner.
