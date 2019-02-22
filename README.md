# pyreqs
Easily build requirements.txt files automatically

## Usage
Install the package
```
pip install git+https://github.com/csteinmetz1/pyreqs
```
Navigate to a python project directory and call the program
```
pyreqs

Found 2 python scripts in /Users/username/project
Found 7 modules in total and 3 external modules.
0 numpy
1 librosa
2 soundfile

Importing external python modules...
Created new requirements.txt file.
```
Check out the new requirements.txt file
```
cat requirements.txt

numpy==1.14.2
soundfile==0.9.0
librosa==0.5.1
```

## Note
Have not thoroughly tested the parsing code so it may not work for all cases...