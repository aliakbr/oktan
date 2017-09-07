from .models import Account

class OktanBackend(object):
    def authenticate(self, request, email=None, password=None):
        # Check the email/password and return an account.
        try:
            print ("a")
            acc = Account.objects.get(email=email)
            if acc.password == password:
                return acc
            else:
                return None
        except Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
