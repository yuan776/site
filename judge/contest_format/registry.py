import six

formats = {}


def register_contest_format(name):
    def register_class(contest_format_class):
        assert name not in formats
        formats[name] = contest_format_class
        return contest_format_class

    return register_class


def choices():
    result = []
    for key, value in sorted(six.iteritems(formats)):
        result.append((key, value.name))
