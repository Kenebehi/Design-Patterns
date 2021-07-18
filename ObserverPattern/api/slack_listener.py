from lib.slack import post_slack_message
from .event import subscribers


# Event Handler
def handle_user_registered_event(user):
    post_slack_message("sales", f"{user.name} has registered with email address {user.email}")


def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
