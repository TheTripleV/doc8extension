from doc8.checks import LineCheck

class Formatter(LineCheck):

    def report_iter(self, line):
        if len(line) > 1000:
            yield("q", "w")