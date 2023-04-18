class Solution:

    def __init__(self, api):
        self.api = api

    def level_1_local_part_validation(self, local_part):
        import re
        valid_local_part_regex = r'^[a-zA-Z0-9\.\-_]+$'
        invalid_combinations_regex = '^\.|\.\.|\-\-|\.$'

        local_part_has_valid_length = len(local_part) <= 64
        has_no_invalid_combinations = re.search(invalid_combinations_regex, local_part) is None
        local_part_matches_regex = re.fullmatch(valid_local_part_regex, local_part) is not None

        return local_part_has_valid_length and \
            local_part_matches_regex and \
            has_no_invalid_combinations

    def level_2_email_validation(self, email_string, tlds):
        import re
        if email_string.count('@') != 1:
            return False

        local_part, domain_part = email_string.split('@')
        if not self.level_1_local_part_validation(local_part):
            return False

        valid_domain_label_regex = '^[a-zA-Z0-9\-_]+$'
        invalid_combinations_regex = '^\.\.|\-\-$'

        domain_length_is_valid = len(domain_part) <= 253
        domain_labels_are_valid = all(
            re.fullmatch(valid_domain_label_regex, label) is not None for label in domain_part.split('.'))
        local_part_is_valid = re.search(invalid_combinations_regex, local_part) is None
        last_label_is_in_list = domain_part.rsplit('.', 1)[-1].lower() in map(str.lower, tlds)

        return domain_length_is_valid and \
            domain_labels_are_valid and \
            local_part_is_valid and \
            last_label_is_in_list
