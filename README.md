# Make Blank Docs

>Create blank .docx files using a list of records in CSV format.

A blank document will be created for each 'FALSE' value in each row.
The documents will be named `[degree_id]-[category].docx`. If 
degree # 204 has a false "skills" value, the document will be named
`204-skills.docx`.  

## Usage:  
```bash
$ python3 make_blank_docs.py [INPUT] [OUTPUT]
```

    INPUT
        Path to a .csv file containing columns:
            degree_id   - (int) ID of a single degree program
            skills      - (str) one of 'TRUE', 'FALSE'
            mission     - (str) one of 'TRUE', 'FALSE'
            courses     - (str) one of 'TRUE', 'FALSE'

    OUTPUT
        Path to a directory where the documents will be stored.
