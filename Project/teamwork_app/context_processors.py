from django.contrib import messages


def flash_messages(request):
    if messages.get_messages(request):
        return {'flash_messages': messages.get_messages(request)}
    return {}
