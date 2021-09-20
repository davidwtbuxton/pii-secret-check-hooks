from pii_secret_check_hooks.check_file.ner import CheckForNER


def create_check():
    check_for_ner = CheckForNER(
        excluded_file_list=None,
        excluded_ner_entity_list=None,
        log_path="tests/assets/log_file_unchanged.json",
    )
    check_for_ner.current_file = "tests/assets/test.txt"
    return check_for_ner


def test_generate_exclude_file():
    check_for_ner = CheckForNER(
        excluded_file_list=None,
        excluded_ner_entity_list=None,
        exclude_output_file="test_exclude_output_file.txt",
        log_path="tests/assets/log_file_unchanged.json",
    )
    check_for_ner.entity_list = [
        "",
    ]
    check_for_ner._generate_exclude_file()
