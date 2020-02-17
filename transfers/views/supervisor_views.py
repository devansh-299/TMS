from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from transfers.constants import UserType
from transfers.models import PS2TSTransfer, UserProfile


class SupervisorHomeView(generic.TemplateView):
    template_name = 'transfers/common.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def get_supervisor_data(request):
    response = {}
    try:
        current_user = request.user
        # applications where approval is pending
        pending_applications_qs = PS2TSTransfer.objects.filter(
            hod_email = current_user.email,
            is_hod_approved = False
        ).values(
            'applicant__user__first_name', 'applicant__user__last_name',
            'cgpa', 'thesis_locale', 'supervisor_email',
            'thesis_subject', 'name_of_org', 'expected_deliverables'
        )
        pending_applications_list = list(pending_applications_qs)
        # approved applications
        approved_applications_qs = PS2TSTransfer.objects.filter(
            hod_email = current_user.email,
            is_hod_approved = True
        ).values(
            'applicant__user__first_name', 'applicant__user__last_name',
            'cgpa', 'thesis_locale', 'supervisor_email',
            'thesis_subject', 'name_of_org', 'expected_deliverables'
        )
        approved_applications_list = list(approved_applications_qs)
        response['error'] = False
        response['message'] = 'success'
        response['data'] = {}
        response['data']['student_pending_attributes'] = [
            {'display':'Student First Name','prop':'applicant__user__first_name'},
            {'display':'Student Last Name','prop':'applicant__user__last_name'},
            {'display':'CGPA','prop':'cgpa'},
            {'display': 'Supervisor (on-campus)', 'prop':'supervisor_email'},
            {'display':'Thesis Location','prop':'thesis_locale'},
            {'display':'Thesis Subject','prop':'thesis_subject'},
            {'display':'Organisation','prop':'name_of_org'},
            {'display':'Expected Deliverables','prop':'expected_deliverables'},
        ]
        response['data']['data_pending'] = [a for a in pending_applications_list]
        response['data']['data_approved']= [a for a in approved_applications_list]
    except Exception as e:
        response['data'] = {}
        response['error'] = True
        response['message'] = 'error'
    return JsonResponse(response, safe=False)
