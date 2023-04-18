class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_break_into_lines(self, text, width):
        words = text.split(' ')
        formatted_text = None
        current_line = None
        for w in words:
            if current_line is None:
                current_line = w
            elif len(current_line) + len(w) + 1 <= width:
                current_line += ' ' + w
            else:
                if formatted_text is None:
                    formatted_text = current_line
                else:
                    formatted_text += '\n' + current_line
                current_line = w
        formatted_text += '\n' + current_line
        return formatted_text

    def level_2_break_into_lines(self, text, num_lines):
        text_width = 1
        current_num_lines = len(text)
        formatted_text = text

        while current_num_lines > num_lines:
            formatted_text = self.level_1_break_into_lines(text, text_width)
            current_num_lines = formatted_text.count('\n') + 1
            text_width += 1
        return formatted_text
