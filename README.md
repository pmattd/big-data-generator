# Big Data Generator 

Application to generate fake files containing data in a configurable structure.
It can be customized to generate files periodically and or write lines into a file periodically to simulate streaming.
configuration is done in the config.json or a specified json file given in the command line parameters

## Configuration

an example configuration is provided in config.json
below is a description of the values in the configuration

Parameter | Description
------------ | -------------
base-filename | The filename to generate, will be appended with _n
max-files | Limit to the number of files that can be generated
max-data-size-in-bytes | Limit to the amount of data to write (-1 if no limit) 
file-write-interval-in-seconds | The time between each file being writer (0 if none) 
line-write-interval-in-seconds | The delay between writing each line in the file (0 if none)
path | Path to write the files
value-separator | Separator to use between values in the csv
fields | Definition of each column see below

### Columns

Column | Description
------------ | -------------
identity | Generates a uuid value
random-value | Generates a random integer value between the given min and max
enumeration | Generates a randomly selected value between the given possibilities

## Running
python app.py

### Command line params 

* --verbose : verbose logging to the command line
* --config : path to the configuration file, defaults to the given configuration files in the data_generator directory
