# patient-data
This is a quick data challenge project

### Table of Contents
[1. Dependencies](#dependencies)  
[2. Project Tree](#project-tree)  
[3. How to run the extractor](#run-the-extractor)  
[4. How to run test cases](#run-tests)  
[5. Source data analysis](#source-data-analysis)  
[6. Final Statistics Results](#final-statistics-results)  

### Dependencies
This is project use `python 2.7.12`  
Our tests are run by `pytest`  
This project is tested on `Ubuntu 16.04`

### Project Tree
```bash
├── data  
│   ├── demo.psv  
│   └── events.psv  
├── objs  
│   ├── __init__.py  
│   ├── event.py  
│   └── patient.py  
├── results 
├── tests
│   ├── __init__.py  
│   ├── test_agg.py  
│   ├── test_event.py
│   ├── test_lib.py    
│   └── test_patient.py  
├── analyser.py
├── const.py
├── extractor.py
├── lib.py 
├── LICENSE  
└── README.md  
```
The `data` folder contains the source data of this coding challenge  
  
The `objs` folder contains two classes, `Event` and `Patient`. Within each event and patient module, rows read from data files are parsed and used to create objects. 

The `results` folder is created on the fly and serves as the location to store patient JSON results. 

The `tests` folder includes all tests cases.  
&nbsp;&nbsp;&nbsp;&nbsp;`test_agg.py` tests aggregated event results in each `patient` object   
&nbsp;&nbsp;&nbsp;&nbsp;`test_event.py` tests the `Event` class  
&nbsp;&nbsp;&nbsp;&nbsp;`test_lib.py` tests methods in `lib.py`  
&nbsp;&nbsp;&nbsp;&nbsp;`test_patient.py` tests the `Patient` class  

The `analyser.py` scripts generates an alternative report on the features of given data set. Details are in [Source data analysis](#source-data-analysis) section  

The `const.py` stores all constants

The `lib.py` contains generic methods, such as calculating years between two given date, and finding median of a list of number.   

The `extractor.py` is the main script of this project.  

### Run the extractor
To run the extraction, we can simply `cd` to the root directory of this project and run `python extractor.py`.  

To run the extraction in debug mode: `python extractor.py -v`  
  
### Run tests
22 test cases are created to ensure the correctness of this project. To run these test cases, we can `cd` to the root directory of the `test` directory and run `pytest`. For more detailed output, we can run `pytest -v`

### Source data analysis
The  `analyser.py` is a standalone script to provide additional insights on the dataset. It helps cross-validate our extractor. 

```bash
event stats: {'empty_date': 0, 'empty_fields': 4318, 'missing_fields': 0, 'rows': 7562, 'wrong_date': 0, 'empty_id': 0, 'empty_code': 4318, 'uniq_events': 3244, 'versions': set(['9', '10']), 'empty_version': 0}
patient stats: {'empty_fields': 0, 'missing_fields': 0, 'rows': 1248, 'empty_birth_date': 0, 'empty_id': 0, 'genders': set(['M', 'F']), 'wrong_birth_date': 0, 'uniq_patients': 1248, 'empty_gender': 0}
patients with no events: 896
valid patients: 352
events with no patients: 420

```

Features in the events dataset:   
1. Total rows: 7562  
2. Rows with empty fields: 4318  
3. All empty fields are the empty `code` fields  
4. All events are unique
5. A patient can have multiple events on one day.   
  
Features in the patients dataset:   
1. All patients are unique

Features derived from both data sets:   
1. Patients with no matching events: 896  
2. Valid patients (patients with at least one event): 352  
3. Events with no matching patients: 420  


### Final Statistics Results
```json
{
    "females": 190, 
    "males": 162, 
    "max_last_event_age": "92 years", 
    "max_timeline": "984 days", 
    "median_last_event_age": "62 years", 
    "median_timeline": "0 days", 
    "min_last_event_age": "2 years", 
    "min_timeline": "0 days", 
    "patients": 352
}
```
Statistics are only calculated from valid patients. 