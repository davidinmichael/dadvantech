from django.core.management.base import BaseCommand
from core.utils import send_email
from django.template.loader import render_to_string


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        context = {
			"name": "David",
		}
        template = render_to_string("core/community_welcome.html", context)
        send_email("davidinmichael@gmail.com", "Test Email", template)
        self.stdout.write(self.style.SUCCESS("Email Sent!"))
