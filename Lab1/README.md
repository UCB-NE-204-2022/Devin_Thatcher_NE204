Dependencies: numpy, matplotlib, scipy, h5py

HDF5 data files are in the HPGe folder of this Google Drive: https://drive.google.com/drive/folders/1lt_kLttrRhQ91nO9xtgCLip4QcroTRs7

The separate programs in this repository allows a user to:
1. View the pulses from the HDF5 files
2. Create a .npy file that contains an array the pulse heights recorded
3. Plot a histogram using that .npy file that indicates where the peaks are
4. Calibrate the histogram using a calibration file created by specifying energies for those indicated peaks

## Description of each program

### ViewPulses.py: 
Asks for HDF5 file location, then plots the first 10000 data points for the first 500 pulses. Fits an exponential to each pulse, and plots the exponential.

### ViewFilteredPulses.py: 
Asks for HDF5 file location, then for the first 500 pulses: subtracts from the pulse the average of the pre-trigger delay, then fits an exponential. If the parameters popt[0, 1, 2] found for the exponential fit are greater than zero: uses a trapezoid filter (d = v(j) - v(j - risetime) - v(j - risetime - flattop) + v(j - 2*risetime - flattop)), integrates with pole-zero correction (1+popt[1]), then plots filtered pulse. Rise time is set for 350, flat top is set for 200 (1.4 uS and 0.8 uS).

### CreateBasicSpectra.py: 
Asks for HDF5 file location, then calculates the difference between the maximum of the first 2000 data points and the average of the pre-trigger delay for each pulse. An array of the differences for each pulse is saved to a .npy file.

### CreateBetterSpectra.py: 
Asks for HDF5 file location, then for the first 120000 pulses: subtracts from the pulse the average of the pre-trigger delay, then fits an exponential. If the parameters found for the exponential fit are greater than zero: uses a trapezoid filter and integrates with pole-zero correction. An array of the average of each flat top is saved to a .npy file. Program also prints how many pulses have been processed successfully, since it takes a while to run.

Used to create .npy files for Co60, Eu152, Cs137, Na22, and Ba133 in SampleSpectra folder, using a rise time of 350 and flat top of 200 for each (1.4 uS and 0.8 uS).

### EnergyCalibration.py: 
Asks for .npy file location and the rise time used to create that file, then plots a histogram. Peaks are indicated on the histogram, and the program prints the channel, heights, and full width half max of those peaks. Enter the energies one by one (in keV) of a few of the highest peaks indicated, and the program will match the energies with the channel of those peaks, appending that data to calibrationdata.txt. The text file can be checked to see that the energies are matched with the correct peaks. This program will loop until no .npy file location is given.

If \*n\* energies are specified, they must correspond with the highest \*n\* peaks.

Rise time needs to be specified since it is directly proportional to trapezoid heights. A histogram of a set of pulse heights with a rise time of 500 will have peaks that are twice as far away from the origin as a histogram of a set of pulse heights with rise time of 250. That factor is calculated when the rise time is specified in order to compare peak locations and full width half maxima on the same spectra scale.

calibrationdata.txt with data for Co60, Eu152, Cs137, Na22, and Ba133 has already been provided.

### ViewHistogram.py: 
First asks for location of calibrationdata.txt.

If nothing is entered, the program will ask for .npy file locations and the rise times used to create those files in a loop, creating histogram data for each file and printing the channel, height, and full width half max of the peaks for each set of histogram data. The average FWHM is also printed. When the user is done entering .npy file locations, the program will plot all histograms with peaks indicated on the same plot, and indicate the average FWHM of all peaks.

If calibrationdata.txt is provided, the program calculates a calibration factor by taking the average ratio of each channel and energy. The same process as above will then occur, but prints energy instead of channel for each peak, and the x-axis is scaled for energy.

## How to use
1. Run CreateBetterSpectra.py
   - Copy and paste path to HDF5 file
   - When prompted, enter name you want .npy file saved as
2. Run EnergyCalibration.py
   - Copy and paste path to .npy file
   - Specify rise time for that .npy file
   - Enter energies one by one for the highest peaks
     - If \*n\* energies are specified, they must correspond with the highest \*n\* peaks.
   - Program will create calibrationdata.txt and save channel/energy data to it (appends if calibrationdata.txt exists already)
   - Can repeat for multiple .npy files
3. Run ViewHistogram.py
   - Copy and paste path to calibrationdata.txt, or press enter to use without energy calibration
   - Copy and paste path to .npy file
   - Specify rise time for that .npy file
   - Repeat for multiple .npy files
   - Press enter to plot histogram(s)