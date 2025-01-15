class Parser:
    from parseLines import _parse_lines, _parse_line
    from parseComms import _parse_commands, _parse_command, _init_comms
    from parseSymbs import _parse_symbols, _parse_labels, _parse_variables, _init_symbols
    from parseMacro import _parse_macros, _parse_macro
    
    def __init__(self, filename):
        try:
            self._file = open(filename + ".asm", "r")
        except:
            Parser._error("File", -1, "Cannot open source file")
            return


        self._lines = []

        try:
            self._read_lines()
        except:
            Parser._error("File", -1, "Cannot read source file.")
            return

  
        self._flag = True 
        self._line = -1   
        self._errm = ""  

     
        self._parse_lines()
        if self._flag == False:
            Parser._error("PL", self._line, self._errm)
            return
 
        self._parse_macros()
        if self._flag == False:
            Parser._error("MACRO", self._line, self._errm)
            return
        
     
        self._parse_symbols()
        if self._flag == False:
            Parser._error("SYM", self._line, self._errm)
            return
        
        self._parse_commands()
        if self._flag == False:
            Parser._error("COM", self._line, self._errm)
            return
            
        try:
            self._outfile = open(filename + ".hack", "w")
        except:
            Parser._error("File", -1, "Cannot open output file")
            return

        try:
            self._write_file()
        except:
            Parser._error("File", -1, "Cannot write to output file")
            return   