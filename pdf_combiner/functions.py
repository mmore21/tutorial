'''
---------------------------------------------
|   Author  :   Maz                         |
|   Created :   September 11, 2018          |
|   Program :   PDF Combiner                |
---------------------------------------------
'''

import os.path

'''
---------------------------------------------------------------------------------
|   [FUNCTION] validPDF:                                                        |
|   -return type    : bool                                                      |
|   -description    : checks if a file name is present in current directory     |
---------------------------------------------------------------------------------
'''
def validPDF(file):
    return True if (os.path.exists(file)) else False