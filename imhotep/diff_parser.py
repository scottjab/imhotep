
class DiffContextParser:
    @staticmethod
    def should_skip_line(line):
        # "index oldsha..newsha permissions" line or..
        # "index 0000000..78ce7f6"
        if re.search(r'index \w+..\w+( \d)?', line):
        # --- /dev/null
        elif re.search('(-|\+){3} (a|b)?/.*', line):
            return True
        # "new file mode 100644" on new files
        elif re.search('new file mode.*', line):
            match = re.search(r'diff .*a/(?P<origin_filename>.*) '
                              r'b/(?P<result_filename>.*)', line)
                z = Entry(match.group('origin_filename'),
                          match.group('result_filename'))