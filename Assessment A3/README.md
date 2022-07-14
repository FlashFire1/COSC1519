# Assessment A3 for the class Introduction to Programming at RMIT
## Introduction:
This is a take-home programming project that you will complete within 48 hours. Such assessments are different from the practical exercises as you are given a problem brief and you will have to devise a solution from a set of precise requirements and written guidance from this assessment description.

## Overview:
Assume that one of your parents' friends who has a small shop (you can decide what kind of shop) needs a software to manage their inventory but they cannot pay the price of well-known software. Proud of your newly acquired programming skills, you offer to make them a simple version of such a software.

### Functional requirements
As this is a programming assessment and not a software design one, here is a skeleton to guide you in the creative part.

Note that this is only a guide to help you; the marking will be done following the marking rubric available at the end of this page.

- At startup, the program will
  - read data from the selected file (see file details below)
  - Load the data from the file and  store it in memory (using relevant variables and data-structures)
  - Show a menu that present a list of interactions possible
- Menu - general behaviour
  - User will select which functionality by entering an integer 
  - If the user entry corresponds to:
    - the save-exit option -> the program save the data and shows that it is stopping and then stop "gracefully"
    - another available option -> the related code is executed, then the menu is shown again
    - not an available option or a wrong kind of entry -> an error message is shown and the menu is shown again (no crash)
- Required  functionalities
  - Look at the information of one item
     - User will be asked the item identifier
     - If that item exist, the related information will be shown
     - If not, the user will be informed that such an item does not exist
  - Look at the information of all items
     - Show all the information of all items in alphabetical order of the item identifier
     - To get full mark, it must re-used the function that shows one item information
  - Add or Update an item
     - User will be asked to enter all the information related to that item
     - The information to that item will be added to the variables/data-structures (in memory)
       - If the item already exist, the program 'does not care', it simply overwrite the information
       - Proper data type must be used; for example a name must be a string, a number of items an integer, the weight a float.
  - Compute the stock value
    - The user will be presented with a message stating the whole value of the stock
      - The value of stock is : the sum of (item's price multiplied by item's quantity) for all items
  - Save and exit
    - The stock information as contained in the variables/data-structures (in memory)) will be written to a different file.
    - A message informs the user the program is shutting down
    - The program stops 'gracefully' (i.e. not crashing)
- Optional (non graded) functionalities
  - Selecting filename (you can 'hardcode' in your program the name of the file)
  - Remove item
  - Exit without saving
  - Column titles and Items loaded are not required (but useful)
- File/data requirements
  - A stock is a collection of items
    - An item needs to have an identifier (name), a price, a quantity and at least 2 other informations of your choice (not a country and a color as in the example!)
  - File names
    - Original file must be named 'A3_s123456_stock.txt' (where s123456 is your student number)
    - Updated file must be named 'updated_A3_s123456_stock.txt' (where s123456 is your student number)
    - Program filename should be A3_s123456.py (added 22/10, no penalty would be applied if not followed)
  - File format must be:
    - first line must be the column title (in the example: item_name price quantity category1[country] category2[color])
    - each following line of this file must store the information related to one item
      - in a line each data must be separated by a comma to allow to have string of multiple words (like 'new zealand' country of origin in the example) 
    - You have to create this plain text file with a text editor of your choice
