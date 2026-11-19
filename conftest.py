
import pytest
import logparser


@pytest.fixture
def log_data():

    # Clear previous data before execution
    logparser.log_contents.clear()
    logparser.error_messages.clear()
    logparser.result.clear()

    # Step 1: Read YAML and log files
    logparser.input_file_reader()

    # Step 2: Extract error messages
    logparser.message_extractor()

    # Step 3: Count error messages
    logparser.count_error_message()

    # Step 4: Return results
    return {
        "log_contents": logparser.log_contents,
        "error_messages": logparser.error_messages,
        "result": logparser.result
    }
