# Python Program to Download Graduation Photos
This Python program is designed to download a set of graduation photos, simplifying the selection process. It reads a handmade CSV file to determine which photos to fetch.

 ## Python Libraries
 Ensure you have the following Python libraries installed:
 
 - `urllib`
 - `csv`
 - `os`

 You can install them using:

 ```bash
 pip install urllib
 pip install csv
 pip install os
 ```

 ## URL Code
 - The code provided by the photographers is the "40140". 
 - The letter "S" following the above number represents the set of photos depending on the date and time of the graduation. It is not standard and this has to change manually.
 - Modify the URL accordingly for your specific needs.

 ## CSV Structure
 The CSV file must adhere to this structure for the program to work:

 1. **First Column:** Total photos in the set (e.g., from number 001 to number 010, there are 10 photos).
 2. **Second Column:** Name of the first photo of the set as shown on the original website.
 3. **Third Column (Optional):** Last 2 digits of the name of the last photo from the current set for checking purposes only; not used by the program.

 Here is an example structure:
 | Total Photos | First Photo Name     | Last Photo's Last Digits     |
 |--------------|----------------------|----------------------------|
 | 11           | 40140-S-00250        | 60                         |
 | 6            | 40140-S-00626        | 31                         |
 | 1            | 40140-S-00821        |                            |
