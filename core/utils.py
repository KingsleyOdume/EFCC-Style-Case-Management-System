from .models import ActivityLog

def log_activity(user, case, action, details=''):
    ActivityLog.objects.create(
        user=user,
        case=case,
        action=action,
        details=details
    )



def role_redirect(user):
    role_routes = {
        'admin': 'admin_dashboard',
        'investigator': 'investigator_dashboard',
        'legal': 'legal_dashboard',
        'analyst': 'analyst_dashboard',
    }
    return role_routes.get(user.role, 'dashboard')
