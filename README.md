# AnonymizeFileNames
Create anonymized filenames based on defined alias mappings. 

## Format of mappings
*Store these mappings in a CSV-formatted file with the first column containing the Original Name and the second column containing the Anonymized Name.*

**Default:** mappings.csv

**Format:** You may find it easiest to create a table (see example below) in your favorite spreadsheet program like the one below. Then export as CSV. **Ensure there is a header line.** Ensure that each Anonymized Name is unique.

*Table version*

| Original Name | Anonymized Name |
| :------------ | :-------------- |
| 2022-03-15_S_Holmes.OBJ | Scan_57831864.OBJ |
| 2022-03-17_J_Watson.OBJ | Scan_57815615.OBJ |

*CSV version*

```text
Original Name,Anonymized Name
2022-03-15_S_Holmes.OBJ,Scan_57831864.OBJ
2022-03-17_J_Watson.OBJ,Scan_57815615.OBJ
```

## Format of input folder
*All files to be anonymized should be within this folder. If you wish to have a subfolder structure, then please add the paths to the "Original Name" and "Anonymized Name" fields in the mappings CSV (see examples below).*

**Default:** to_anonymize/

**Example mappings with subfolders:**

*Table version*

| Original Name | Anonymized Name |
| :------------ | :-------------- |
| subfolder/2022-05-10_J_Watson.OBJ | subfolder/Scan_56585612.OBJ |
| subfolder_to_drop/2022-06-11_M_Moriarti.OBJ | Scan_51235613.OBJ |

*CSV version*

```text
Original Name,Anonymized Name
subfolder/2022-05-10_J_Watson.OBJ,subfolder/Scan_56585612.OBJ
subfolder_to_drop/2022-06-11_M_Moriarti.OBJ,Scan_51235613.OBJ
```

In this example, the J. Watson file will be put into a subfolder when anonymized (e.g., anonymized/subfolder/Scan_56585612.OBJ). By contrast, the M. Moriarti file will be anonymized into the base output folder (e.g., anonymized/Scan_51235613.OBJ).


## Format of the output folder
*To prevent accidental overwriting of original files. You must specify a folder that does __not__ currently exist. All anonymized files will be copied into that folder.*

**Default:** anonymized/


## Example version
*This repository contains an `Example/` folder with a `mappings.csv` and `to_anonymize/` folder. You may try out the tool by navigating to that `Example/` folder and typing the following:*

```python
python3 ../anonymize_file_names.py
```

OR

```python
python3 ../anonymize_file_names.py --mappings=mappings.csv --files=to_anonymize --output=anonymized
```

After you run, you will observe a new folder called `anonymized/` with your new anonymized filenames.
