from pathway import pathways
from emergency import models
from obs.models import Observation

class BookingIn(pathways.PagePathway):
    display_name = 'ED Booking In'
    slug = 'booking'
    steps = (models.Demographics,)

    def save(self, data, user):
        patient = super(BookingIn, self).save(data, user)
        episode = patient.episode_set.last()
        episode.set_tag_names(["triage"], None)
        return patient

    def redirect_url(self, patient):
        return "/#/list/triage"


class Triage(pathways.PagePathway):
    display_name = "Triage Entry"
    slug = "triage"
    steps = (models.Demographics, Observation, models.EmergencyDepartmentTriage,)

    def save(self, data, user):
        patient = super(Triage, self).save(data, user)
        episode = patient.episode_set.last()
        episode.set_tag_names(["waiting"], None)
        return patient

    def redirect_url(self, patient):
        return "/#/list/waiting"



class Examination(pathways.PagePathway):
    display_name = 'Exam'
    slug = 'exam'
    steps = (
        pathways.Step(template_url='templates/demographics_step.html',
                      icon='fa fa-user',
                      display_name='Demographics'),
        models.SymptomComplex,
        pathways.MultiSaveStep(template_url='/templates/pmh.html', model=models.PastMedicalHistory),
        models.PatientConsultation
    )

    def redirect_url(self, patient):
        return '/#/list/waiting'
