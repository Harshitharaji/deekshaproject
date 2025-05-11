from django.contrib import admin
from deekshaapp.models import Question,Assessment,AssessmentResults,Profile,Certifications,AdvisorSupportTask
# Register your models here.

admin.site.register(Question)
admin.site.register(Assessment)
admin.site.register(AssessmentResults)
admin.site.register(Profile)
admin.site.register(AdvisorSupportTask)
admin.site.register(Certifications)