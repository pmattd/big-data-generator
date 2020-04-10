from DataFile import DataLineGenerator
from FileGenerator import FileGenerator, SequentialFileName
from GeneratorConfiguration import ConfigReader, GeneratorConfiguration

if __name__ == '__main__':
    config: GeneratorConfiguration = ConfigReader().read_json("testjson")

    data_line_generator = DataLineGenerator(config.generators, ",")
    fw = FileGenerator(interval=config.interval_in_seconds,
                       lines=config.max_lines,
                       max_files=config.max_files,
                       path=config.path,
                       generator=data_line_generator,
                       file_name_generator=SequentialFileName("newfile"))
    fw.schedule()

    print(config.max_lines)

# no separator at the end of the line
# make into csv writer
# run from command line
# upload to github

# csv writer/avro writer/parquet writer
# max size in bytes
# clean up files
