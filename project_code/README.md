## User Guide of SpeedyAuger App

#### 1. Project Description
SpeedyAuger is a software helps experimenter to calculate Auger transitions for elements with atomic number 3 to 93. User can plot Auger and core lines with the dataset they provided, which aids surface elements identification in laboratory. The results are tabulated, and could be accessible in the form of tables and plots.

#### 2. How to run the program
* Development Environment
  SpeedyAuger can run on Windows system without any other configuration. The source code is written by Python.
* Package used in SpeedyAuger
  - tkinter
  - numpy
  - itertools
  - shlex
  - decimal
  - tabulate
  - webbrowser
  - matplotlib
* Run the software
  Double-click the SpeedyAuger.exe

#### 3. Catalog
├── README.md                   // user guide
├── SpeedyAuger.exe             // software
├── SpeedyAuger.py              // source code
├── EADL_database               // Auger data from EADL
│   ├── atom.txt                // atom number and atom name
│   ├── energies.txt            // core state energies of subshells for elements  
│   ├── energies_range.txt      // the maximum and minimum Auger values for each element
│   ├── notation.txt            // the relationship between barkla notation and orbital notation   
│   └── shell.txt               // electrons configuration of elements 
│              
├── Scofield_csv_database
│   ├── 3.csv                   // cross section of element with atomic number 3
│   ├── 4.csv                   // cross section of element with atomic number 4 
│   ├── ...
│   └── 93.csv                  // cross section of element with atomic number 4
├── Cu_ref_survey.txt           // reference
├── image                       // store image of README



#### 4. Introduce Fuunction

* Root Window
![root](\image\root_window.jpg)
Open the SpeedyAuger, user can see the root window.


* Auger Transition for Each Element
To calculate the Auger energies for each element, just click the corresponding element button. 
For example: 5 B
![click_element](\image\click_element.jpg)
Then, a new window pops up
![Auger_transition](\image\Auger_transition.jpg)
The right table shows all possible Auger transitions and energies for B.


* Convert Kinetic Energy to Binding Energy
User can select or enter photon energy to convert kinetic energy of Auger transition to binding energy. Export button helps user to export the table to a txt file. 
![convert_function](\image\convert_function.jpg)
![export_auger_table](\image\export_auger_table.jpg)


* Show Core Energy for Each Element
To get the core state binding energies for each element, click the corresponding element. 
For example: 5 B
The left table shows the core energies for each subshell of B. 
![core_energies](\image\core_energies.jpg)


* Search Function
Go back the the root window, user can search Auger transitions and core energies in a specified range. 
   - Search Auger Transition
![search_auger](\image\search_auger.jpg)
Enter the search range firstly, then select Auger transitions option. User can select search from all elements or some specified elements as well.
![select_elements](\image\select_elements.jpg)
The combobx and entry pop up for user to select or enter photon energy when select search by binding energy. Finally, click search button.

    - Search Core State Energies
![search_core](\image\search_core.jpg)
Enter the search range firstly, then select Auger transitions option. User can select search from all elements or some specified elements as well.
The combobx and entry pop up for user to select or enter photon energy when select search by kinetic energy. Finally, click search button.

    - Search Auger and Core Energy Together
![search_both](\image\search_both.jpg)
As shown in the figure, user selects 'Both' for the first option, then select elements and photon energy. Finally, click search button.

    - Search Window
After clicking the search button, the program opens a new window which contains a table. 
![search_window](\image\search_window.jpg)
The table shows Auger or core energies in the search range. Three buttons provide three ways to sort table data. Export button helps user to import the table to txt file.


* Plot Function
    - Plot Auger and Core Lines for Each Element
The program can plot Auger lines and core lines with energies and normalized intensity.
![plot_each](\image\plot_each.jpg)
For example: 5 B
User can select the value of photon energy and x axis (BE vs KE). Finally, click plot button.
![plot_figure1](\image\plot_figure1.jpg)

    - Plot Imported Dataset
Go back to the root window, the program allows user to import dataset they measured, and plot the data and reference lines.
 ![plot_data](\image\plot_data.jpg)
 User needs to import data file, select photon energy and elements, and the range of x axis.
 ![plot_figure2](\image\plot_figure2.jpg)
     
     - Plot Reference Lines for a Number of Selected Elements
Go back to the root window, user selects elements and photon energy, click plot button directly without import files.

#### 5. Information of Developing Group
Group: Applied X-ray Spectroscopy (https://a-x-s.org/group/)
Author: Lu Liu
Supervisor: Anna Regoutz, Curran Kalha
Institution: University College London
Contact: Liulu199807@hotmail.com








 