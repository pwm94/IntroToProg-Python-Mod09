# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Paul Mitchell,12/15/2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file is not meant to ran by itself")


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
lstTable =[]
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

# Show user a menu of options
while (True):
    Eio.print_menu_items()  # Shows menu
    strChoice = Eio.input_menu_options()  # Get user's menu option choice

    if strChoice.strip() == '1':      # Show user current data in the list of employee objects
        for row in lstTable:
            line = row.to_string()
            print(row.to_string())
        continue  # to show the menu

    elif strChoice == '2':  # Let user add data to the list of employee objects
        addEmp = Eio.input_employee_data()
        print(addEmp.first_name + " has been added")
        lstTable.append(addEmp)
        continue  # to show the menu

    elif strChoice == '3':   # let user save current data to file
        strChoice = Eio.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Fp.save_data_to_file("EmployeeData.txt", lstTable) #use write data function
        else:
            print("Save Cancelled!")
        continue  # to show the menu


    elif strChoice == '4':  # Let user exit program
        print("Goodbye!")
        break  # and Exit

    else:
        print("Error! Please input a menu option: [1] to [4]")

# Main Body of Script  ---------------------------------------------------- #
