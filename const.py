from datetime import datetime

IDX_ID = 0
IDX_DATE = 1
IDX_VERSION = 2
IDX_CODE = 3
EVENT_ROW_LENGH = 4

SYSTEM_9 = "http://hl7.org/fhir/sid/icd-9-cm"
SYSTEM_10 = "http://hl7.org/fhir/sid/icd-10"


IDX_BIRTH_DATE = 1
IDX_GENDER = 2
PATIENT_ROW_LENGH = 3

MAX_DATE = datetime.strptime("9999-12-31", '%Y-%m-%d')
MIN_DATE = datetime.strptime("0001-01-01", '%Y-%m-%d')