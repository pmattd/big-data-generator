# Big Data Generator 

Application to generate fake files containing data in a configurable structure.
It can be customized to generate files periodically and or write lines into a file periodically to simulate streaming.
configuration is done in the config.json or a specified json file given in the command line parameters

## Configuration

an example configuration is provided in config.json
below is a description of the values in the configuration

Parameter | Description
------------ | -------------
base-filename | The filename to generate. It will be appended with _n where n is a sequential number starting from 1
max-files | Limit to the number of files that can be generated
max-data-size-in-bytes | Limit to the amount of data to write (-1 if no limit)
file-write-interval-in-seconds | The time to pause between the end of one file and the start of the next (0 if none)
line-write-interval-in-seconds | The delay between writing each line in the file (0 if none)
path | Path to write the files
value-separator | Separator to use between values in the csv
columns | Definition of each column see below
header | add a header row to the beginning of the data, mainly for csv type files, uses the name of each column

### Columns

Column | Description
------------ | -------------
identity | Generates a uuid value
random-value | Generates a random integer value between the given min and max
enumeration | Generates a randomly selected value between the given possibilities
date-time | Generates a utc date-time using on the current time, randomized between the upper and lower bounds i.e. values of lower: -3600 and upper: 3600 will give a range of current time minus 1 hr and plus 1 hr

## Running
python app.py
or use the supplied .bat file

### Command line params 

* --verbose : verbose logging to the command line
* --config : path to the configuration file, defaults to the given configuration files in the data_generator directory
