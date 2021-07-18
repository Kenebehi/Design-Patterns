from api.user import register_new_user, password_forgotten
from api.plan import upgrade plan
from api.slack_listener import setup_slack_event_handlers
from api.log_listener import setup_logs_event_handlers

# initialize event structure
setup_logs_event_handlers()
setup_slack_event_handlers()

#register a new
register_new_user("kenneth", "password", "kenneth@email.com")

#send password reset message
password_forgotten("kenneth@email.com")

#upgrade the plan
upgrade_plan("kenneth@email.com")
