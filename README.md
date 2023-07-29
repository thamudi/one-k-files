# one-k-files

This script will group files into sub-folders, each sub-folder to be named with its common language name.

Author: Tamim Hamoudi

## Directory tree

```bash
.
├── files
│   ├── arabic-1.txt
│   ├── arabic-10.txt
│   ├── arabic-100.txt
│   ├── ...
│   ├── ...
├── main.py
├── README.md
├── requirements.txt
├── test_big_o.py
└── tests
```

## Supported systems

- Unix (Linux, WSL, Mac)
- Windows (powershell, cmd)

## Usage

Prerequisites:

python 3.10 or up

You will only need to run the main.py

`python main.py`

Then the user will be promoted to enter a directory name of which the files will be grouped into.

## Testing

There is a test file called `test_big_o.py` which is used to run multiple instances of the program and then calculate and output the time complexity.

To run the test.py you will need first to install the `requirements.txt`

`pip install -r requirements.txt`

Or install the library directly

`pip install big-o`

After that just run the following command:

`python test_big_o.py`

And you should see an output with the best time complexity
