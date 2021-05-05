# from __future__ import absolute_import, unicode_literals
# from django.dispatch import Signal
from celery import shared_task
# from django.conf import settings


# @shared_task(bind=True)
# def debug_task(self):
# 	print ('^^^^^^^^^^^^^^^^^^^^^^')
# 	return True


# @shared_task
# def add(x,y):
# 	print('x=x & y=Y')
# 	return x + y



# from django.core import mail
# @shared_task
# emails = (
#     ('Hey Man', "I'm The Dude! So that's what you call me.", 'dude@aol.com', ['mr@lebowski.com']),
#     ('Dammit Walter', "Let's go bowlin'.", 'dude@aol.com', ['wsobchak@vfw.org']),
# )
# results = mail.send_mass_mail(emails)
# from celery.task import Task
from django.core.mail import send_mail
# from django.template import loader
# from django.utils.html import strip_tags
# from config.celery import app
# from config.settings import default


# class SendConfirmationEmail(Task):

#     def __init__(self, *args, **kwargs):
#         self.user_name = kwargs.get('username')
#         self.user_id = kwargs.get('id')
#         self.user_hash = kwargs.get('hash')
#         self.user_email = kwargs.get('email')

#     def send_email(self):
#         confirm_mail = loader.render_to_string('mail/confirmation.html',
#                                            {'user': self.user_name, 'id': self.user_id,
#                                             'hash': self.user_hash,
#                                             'domain': default.SITE_URL})
#         text_email = strip_tags(confirm_mail)
#         send_mail(
#             subject='Confirm Your E-mail',
#             message=text_email,
#             from_email='no-reply@mysite.com',
#             recipient_list=[self.user_email],
#             fail_silently=False,
#             html_message=confirm_mail
#         )

#      def run(self, *args, **kwargs):
#          self.send_email()

# app.register_task(SendConfirmationEmail())

@shared_task()
def check():
	# send_mail(
	# 	subject='Confirm Your E-mail',
	# 	message='text_email',
	# 	from_email='shivesh9795@gmail.com',
	# 	recipient_list=['shi@mailinator.com'],
	# 	fail_silently=False,
	# 	# html_message=confirm_mail
	# )

	# print('000000')
	# print (send_mail)
	# return True

	send_mail(
	    'Subject here',
	    'Here is the message.',
	    'shivesh9795@gmail.com',
	    ['to@example.com'],
	    fail_silently=False,)

	return True