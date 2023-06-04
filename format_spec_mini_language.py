# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : format_spec_mini_language.py
# - author : yc0325lee
# - created : 2022-10-10 19:11:52 by lee2103
# - modified : 2022-10-10 19:11:52 by lee2103
# - description : 
# ----------------------------------------------------------------------------

# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# type(format_spec) -> str
