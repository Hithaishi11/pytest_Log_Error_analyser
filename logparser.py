import yaml

log_contents = {}

keywords = ("FAIL", "ERROR", "EXCEPTION")

error_messages = {}

result = {}


# STEP 1: Read YAML and log files

def input_file_reader():

    with open("input_log_file.yml", "r") as f:
        config = yaml.safe_load(f)

    print("YAML Configuration:")
    print(config)

    for key, filename in config["logfiles"].items():

        print(f"Reading {key}: {filename}")

        with open(filename, "r") as logfile:
            log_contents[key] = logfile.readlines()

    print("\nLog Contents:")
    print(log_contents)


# STEP 2: Extract error messages

def message_extractor():

    for filename, lines in log_contents.items():

        error_messages[filename] = []

        for line in lines:

            if any(keyword in line.upper()
                   for keyword in keywords):

                error_messages[filename].append(line.strip())

    print("\nExtracted Error Messages:")
    print(error_messages)


# STEP 3: Count error messages

def count_error_message():

    for file, lines in error_messages.items():

        result[file] = {
            "ERROR": 0,
            "FAIL": 0,
            "EXCEPTION": 0
        }

        for line in lines:

            for error_type in result[file]:

                if error_type in line.upper():

                    result[file][error_type] += 1

    print("\nError Count:")
    print(result)