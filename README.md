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
![root](https://github.com/SepNmoon/Auger_Software/blob/master/image/root_window.JPG)
Open the SpeedyAuger, user can see the root window.


* Auger Transition for Each Element
To calculate the Auger energies for each element, just click the corresponding element button. 
For example: 5 B
![click_element](https://github.com/SepNmoon/Auger_Software/blob/master/image/click_element.JPG)
Then, a new window pops up
![Auger_transition](https://github.com/SepNmoon/Auger_Software/blob/master/image/Auger_transition.JPG)
The right table shows all possible Auger transitions and energies for B.  
The Auger transitions are calculated using the methods outlined by W. A. Coghlan and R.E. Clausing [1].


* Convert Kinetic Energy to Binding Energy
User can select or enter photon energy to convert kinetic energy of Auger transition to binding energy. Export button helps user to export the table to a txt file. 
![convert_function](https://github.com/SepNmoon/Auger_Software/blob/master/image/convert_function.JPG)
![export_auger_table](https://github.com/SepNmoon/Auger_Software/blob/master/image/export_auger_table.JPG)


* Show Core Energy for Each Element
To get the core state binding energies for each element, click the corresponding element. 
For example: 5 B
The left table shows the core energies for each subshell of B. 
![core_energies](https://github.com/SepNmoon/Auger_Software/blob/master/image/core_energies.JPG)


* Search Function
Go back the the root window, user can search Auger transitions and core energies in a specified range. 
   - Search Auger Transition
![search_auger](https://github.com/SepNmoon/Auger_Software/blob/master/image/search_auger.JPG)
Enter the search range firstly, then select Auger transitions option. User can select search from all elements or some specified elements as well.
![select_elements](https://github.com/SepNmoon/Auger_Software/blob/master/image/select_elements.JPG)
The combobx and entry pop up for user to select or enter photon energy when select search by binding energy. Finally, click search button.

    - Search Core State Energies
![search_core](https://github.com/SepNmoon/Auger_Software/blob/master/image/search_core.JPG)
Enter the search range firstly, then select Auger transitions option. User can select search from all elements or some specified elements as well.
The combobx and entry pop up for user to select or enter photon energy when select search by kinetic energy. Finally, click search button.

    - Search Auger and Core Energy Together
![search_both](https://github.com/SepNmoon/Auger_Software/blob/master/image/search_both.JPG)
As shown in the figure, user selects 'Both' for the first option, then select elements and photon energy. Finally, click search button.

    - Search Window
After clicking the search button, the program opens a new window which contains a table. 
![search_window](https://github.com/SepNmoon/Auger_Software/blob/master/image/search_window.JPG)
The table shows Auger or core energies in the search range. Three buttons provide three ways to sort table data. Export button helps user to import the table to txt file.


* Plot Function
    - Plot Auger and Core Lines for Each Element
The program can plot Auger lines and core lines with energies and normalized intensity.
![plot_each](https://github.com/SepNmoon/Auger_Software/blob/master/image/plot_each.JPG)
For example: 5 B
User can select the value of photon energy and x axis (BE vs KE). Finally, click plot button.
![plot_figure1](https://github.com/SepNmoon/Auger_Software/blob/master/image/plot_figure1.JPG)  
Auger line intensities were calculated using the 'normalized multiplicity" method outlined by W. A. Coghlan and R.E. Clausing [1].  
Core line intensities are scaled according to their photoionisation cross section value at the given photon energy. The implemented photoionisation cross section data was taken from the digitised version of the Scofield Cross Section tabulated data [2,3].

    - Plot Imported Dataset
Go back to the root window, the program allows user to import dataset they measured, and plot the data and reference lines.
 ![plot_data](https://github.com/SepNmoon/Auger_Software/blob/master/image/plot_data.JPG)
 User needs to import data file, select photon energy and elements, and the range of x axis.
 ![plot_figure2](https://github.com/SepNmoon/Auger_Software/blob/master/image/plot_figure2.JPG)
     
     - Plot Reference Lines for a Number of Selected Elements
Go back to the root window, user selects elements and photon energy, click plot button directly without import files.

#### 5. Information of Developing Group
Group: Applied X-ray Spectroscopy (https://a-x-s.org/group/)
Author: Lu Liu
Supervisor: Anna Regoutz, Curran Kalha
Institution: University College London
Contact: Liulu199807@hotmail.com

version: 1.0 26/08/2021


#### References
[1] W.A. Coghlan, R.E. Clausing. Auger catalog calculated transition energies listed by energy and element. Atomic Data and Nuclear Data Tables. Volume 5, Issue 4,
1973, Pages 317-469.  
[2] C. Kalha, N. K. Fernando, A. Regoutz, Digitisation of Scofield Photoionisation Cross Section Tabulated Data, 2020, figshare, Dataset, https://doi.org/10.6084/m9.figshare.12967079.v1.  
[3] J.H. Scofield, Theoretical photoionization cross sections from 1 to 1500 keV, Technical Report UCRL-51326, Lawrence Livermore Laboratory, 1973, https://doi.org/10.2172/4545040.








 