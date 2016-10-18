import difflib
text1 = """text1:
This module provides classes and funtions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
and string
abc
"""

text1_lines = text1.splitlines()
text2 = """text2:
This module provides classes and funtions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
abc
"""
text2_lines = text2.splitlines()
d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print '\n'.join(list(diff))
