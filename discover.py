import os
from sys import platform

extensions = [
    'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # images
    # 'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
    # 'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies
    #
    # 'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
    # 'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
    # 'yml', 'yaml', 'json', 'xml', 'csv', # structured data
    # 'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images
    #
    # 'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
    # 'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
    # 'java', 'class', 'jar', # java source code
    # 'ps', 'bat', 'vb', # windows based scripts
    # 'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
    # 'go', 'py', 'pyc', 'bf', 'coffee', # other source code files
    #
    # 'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
]

drivers = [
    'a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def file_finder(root_path='/'):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            root_file = os.path.abspath(os.path.join(root, file))
            ext = root_file.split('.')[-1]
            if ext in extensions:
                yield root_file

def finall_discover():

    if 'win32' in platform:
        for driver in drivers:
            startdirs = ['{}:\\'.format(driver)]
            for currentDir in startdirs:
                for file in file_finder(currentDir):
                    yield file
    else:
        for file in file_finder():
            for file in file_finder('/home'):
                yield file

if __name__ == '__main__':
    finall_discover()

