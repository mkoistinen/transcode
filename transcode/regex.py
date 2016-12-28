import re

multiline_re = re.compile(r'\r?\n(?:[ \t]*\r?\n)+')
multiline_splitter = multiline_re.split

url_re = re.compile(r'''
    (ht|f)tps?://                                           # Protocol
    (?:\w+:\w+@)?                                           # Username:Password
    ([-\w]+)(\.[-\w]+)*                                     # domain
    ([\d]{1,5})?                                            # Port
    (                                                       # Directories
        ((/([-\w~!$+|.,=]   |
        %[a-f\d]{2})+)+|/)+ |
        \?                  |
        [#]
    )?  
    (                                                       # Query
        (
            \?([-\w~!$+|.,*:]   |
            %[a-f\d{2}])+=
            ([-\w~!$+|.,*:=]|%[a-f\d]{2})*
        )
        (&
            ([-\w~!$+|.,*:]|%[a-f\d{2}])+
            =([-\w~!$+|.,*:=]|%[a-f\d]{2})*
        )*
    )*
    ([#](?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)?                  # Anchor
    ''',
    re.VERBOSE
)
