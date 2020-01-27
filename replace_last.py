def replace_last(source_string, replace_what, replace_with):
    """used to replace the last occurence of something in a string."""
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail