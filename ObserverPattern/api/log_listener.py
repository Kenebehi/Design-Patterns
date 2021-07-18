from lib.log import log
from .event import subscribers


# Event Handlers
def handle_user_registered_event(user):
    log(f"{user.name} has registered with email address {user.email}")


def handle_user_password_forgotten_event(user):
    log(f"user with email address {user.email} requested a password reset.")


def setup_logs_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
