"""
Defining OPAL PatientLists
"""
from opal import core
from opal.models import Episode
from obs.models import Observation
from emergency import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self):
        return Episode.objects.all()

class PatientsForTriageList(core.patient_lists.TaggedPatientList):
    display_name = 'Patients For Triage'

    tag = 'triage'

    template_name = 'triage_list.html'

    schema = [
        models.Demographics,
        models.Location,
        Observation,
        models.EmergencyDepartmentTriage
    ]

class PatientsWaitingToBeSeen(core.patient_lists.TaggedPatientList):
    display_name = 'Patients Waiting To Be Seen'

    tag = 'waiting'
    template_name = 'waiting_list.html'

    schema = [
        core.patient_lists.Column(name='hooray', title='Boo', template_path='hello.html'),
        models.Demographics,
        models.Location,
        Observation,
        models.EmergencyDepartmentTriage
    ]
