Dependencies: numpy, matplotlib, scipy

The separate programs in this repository allows a user to:
1. View the pulses from the HDF5 files
2. Create a .npy file that contains an array of all the pulse heights recorded
3. Plot a histogram using that .npy file that indicates where the peaks are
4. Calibrate the histogram using a calibration file created by specifying energies for those indicated peaks

## Description of each program

### ViewPulses.py: 
Asks for HDF5 file location, then plots the first 3000 data points for the first 100 pulses.

### ViewFilteredPulses.py: 
Asks for HDF5 file location, then for each pulse: subtracts the average of the pre-trigger delay, uses a trapezoid filter (d = v(j) - v(j - risetime) - v(j - risetime - flattop) + v(j - 2*risetime - flattop)), integrates with basic pole-zero correction (1+1/decayconstant), then plots the first 3000 data points for the first 100 pulses. Rise time is set for 150, flat top is set for 300, and decay constant set for 10000.

### CreateBasicSpectra.py: 
Asks for HDF5 file location, then calculates the difference between the maximum of the first 3000 data points and the average of the pre-trigger delay for each pulse. An array of the differences for each pulse is saved to a .npy file.

### CreateBetterSpectra.py: 
Asks for HDF5 file location, then for each pulse: subtracts the average of the pre-trigger delay, uses a trapezoid filter, integrates with basic pole-zero correction, and finds the maximum of the first 3000 data points. An array of the maximum for each pulse is saved to a .npy file. Takes about 20 minutes for a 5 GB HDF5 file.

### EnergyCalibration.py: 
Asks for .npy file location then plots a histogram. Peaks are indicated on the histogram, and the program prints the channel, heights, and full width half max of those peaks. Enter the energies one by one (in keV) of a few of the highest peaks indicated, and the program will match the energies with the channel of those peaks, appending that data to calibrationdata.txt. The text file can be checked to see that the energies are matched with the correct peaks. This program will loop until no .npy file location is given.

If \*n\* energies are specified, they must correspond with the highest \*n\* peaks.

calibrationdata.txt with data for Co60, Eu152, Cs137, Na22, and Ba133 has already been provided.

### ViewHistogram.py: 
First asks for location of calibrationdata.txt.

If nothing is entered, the program will ask for .npy file locations in a loop, creating histogram data for each file and printing the channel, height, and full width half max of the peaks for each set of histogram data. The average FWHM is also printed. When the user is done entering .npy file locations, the program will plot all histograms with peaks indicated on the same plot, and indicate the average FWHM of all peaks.

If calibrationdata.txt is provided, the program calculates a calibration factor by taking the average ratio of each channel and energy. The same process as above will then occur, but prints energy instead of channel for each peak, and the x-axis is scaled for energy.

## How to use
1. Run CreateBetterSpectra.py
   - Copy and paste path to HDF5 file
   - When prompted, enter name you want .npy file saved as
2. Run EnergyCalibration.py
   - Copy and paste path to .npy file
   - Enter energies one by one for the highest peaks
     - If \*n\* energies are specified, they must correspond with the highest \*n\* peaks.
   - Program will create calibrationdata.txt and save channel/energy data to it (appends if calibrationdata.txt exists already)
   - Can repeat for multiple .npy files
3. Run ViewHistogram.py
   - Copy and paste path to calibrationdata.txt, or press enter to use without energy calibration
   - Copy and paste path to .npy file
   - Repeat for multiple .npy files
   - Press enter to plot histogram(s)