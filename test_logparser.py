
import pytest


# TEST 1: Verify both log files are read

def test_log_file_reader(log_data):

    assert "file1" in log_data["log_contents"]
    assert "file2" in log_data["log_contents"]

    assert len(log_data["log_contents"]) == 2


# TEST 2: Verify error messages are extracted

def test_message_extractor(log_data):

    errors = log_data["error_messages"]

    assert len(errors["file1"]) > 0
    assert len(errors["file2"]) > 0


# TEST 3: Verify only expected keywords are extracted

def test_error_keywords(log_data):

    errors = log_data["error_messages"]

    keywords = ("FAIL", "ERROR", "EXCEPTION")

    for filename, lines in errors.items():

        for line in lines:

            assert any(
                keyword in line.upper()
                for keyword in keywords
            )


# TEST 4: Verify ERROR count

def test_error_count(log_data):

    counts = log_data["result"]

    for filename in counts:

        assert counts[filename]["ERROR"] >= 0


# TEST 5: Verify FAIL count

def test_fail_count(log_data):

    counts = log_data["result"]

    for filename in counts:

        assert counts[filename]["FAIL"] >= 0


# TEST 6: Verify EXCEPTION count

def test_exception_count(log_data):

    counts = log_data["result"]

    for filename in counts:

        assert counts[filename]["EXCEPTION"] >= 0


# TEST 7: Verify count dictionary structure

def test_error_count_structure(log_data):

    counts = log_data["result"]

    expected_keys = ["ERROR", "FAIL", "EXCEPTION"]

    for filename in counts:

        assert list(counts[filename].keys()) == expected_keys


# TEST 8: Verify extracted error count

def test_extracted_error_count(log_data):

    errors = log_data["error_messages"]
    counts = log_data["result"]

    for filename, lines in errors.items():

        total_count = sum(counts[filename].values())

        assert total_count >= len(lines)
