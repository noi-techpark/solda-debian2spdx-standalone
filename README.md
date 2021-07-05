# solda-debian2spdx-standalone
debian2spdx is a tool to convert *.debian & *.orig files to a *.spdx file.  
It can be used in the command line.  

# dependencies
* Python3
* All librarys in requirements.txt
    * Can be easily installed with pip by running the followind command: pip install -r requirements.txt


# usage
execute the program in the command line with the following attributes:  

    required  
        [--orig] or [-o] to enter the path of the required .orig file  
        [--debian] or [-d] to enter the path of the required .debian file  

    optional  
        [--name] or [-n] to set a name for the output file  



