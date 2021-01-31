# tech-test

## installation
```
python setup.py install
```
To avoid any package drama in unit tests.
No requirements - all done with Python's (pretty great) standard library.

## usage
```
run.py [option]
```
Commands available:
```
--task1 --task2 --task3 --task4
```
Can be used in any configuration, e.g.
```
run.py --task2 --task1
```
Will execute task2 and task1 in that order.
If no command line arguments supplied, all tasks will be executed.

## testing
cd into the test directory and execute
```
python -m unittest test_mastutil.py
```

##general remarks
Dataset is tiny and queries don't require any complex relationship modelling so a DB was not necessary. My first instinct would've been to make it a web API with something like FastAPI/Flask/Django, but the spec didn't ask for it. It did, however, ask to avoid any extra requirements and stick to it as closely as possible, so I did.
I've used some default arguments as I generally like some flexibility, but didn't elaborate on them, as - at the end of the day - that was not requested. 

