def show_responses_notification(request):
    if request.user.is_authenticated:
        if request.user.type_user == 'employment':
            responses = []
            for job in request.user.jobs.all():
                for resume in job.resume_user.all():
                    responses.append(resume)
            context = {}
            context['responses_notification'] = len(responses)
            return context
        else: 
            return {'responses_notification': None}
    else:
        return {'responses_notification': 'No authenticated'}
