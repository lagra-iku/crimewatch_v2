# middleware.py
import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin

class AutoLogoutMiddleware(MiddlewareMixin):
    """logs out user after period of inactivity"""
    def process_request(self, request):
        if not request.user.is_authenticated:
            return

        # Get the current time
        current_time = datetime.datetime.now()

        # Get the last activity time from the session
        last_activity = request.session.get('last_activity')

        if last_activity:
            # Convert last activity time to a datetime object
            last_activity_time = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')
            
            # Calculate the time difference
            time_elapsed = (current_time - last_activity_time).total_seconds()
            
            # If the time elapsed exceeds the session timeout, log out the user
            if time_elapsed > settings.SESSION_COOKIE_AGE:
                logout(request)
                return

        # Update the last activity time in the session
        request.session['last_activity'] = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')