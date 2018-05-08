# Prettify JSON

This script, which takes the input to a file with arbitrary data in JSON format, and displays its content in the console in an easy-to-read form: adds line breaks, left indents and spaces.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py C:\bar.json
# Example '["foo", {"bar":["baz", null, 1.0, 2]}]'
 [
    "foo", 
    {
        "bar": [
            "baz", 
            null, 
            1.0, 
            2
        ]
    }
]

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
