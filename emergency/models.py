"""
emergency models.
"""
from django.db.models import fields
from opal.core import lookuplists
from opal import models
from opal.core.fields import ForeignKeyOrFreeText

class ManchesterTriageScore(lookuplists.LookupList): pass

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass

class PatientConsultation(models.PatientConsultation):
    plan = fields.TextField(blank=True, null=True)

class EmergencyDepartmentTriage(models.EpisodeSubrecord):
    _is_singleton = True
    reason = fields.TextField(blank=True, null=True, verbose_name="Reason For Attendance")
    mts_score = ForeignKeyOrFreeText(ManchesterTriageScore, verbose_name="Manchester Triage Score")



# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass
