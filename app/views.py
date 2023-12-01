"""
View to redirect to the API doc.
"""

from django.shortcuts import redirect

def redirect_to_api_docs(request):
    return redirect('/api/docs/')