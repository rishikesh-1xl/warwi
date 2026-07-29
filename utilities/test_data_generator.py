import uuid
import random
import string


class TestDataGenerator:


    @staticmethod
    def company():

        return {
            "company_name": TestDataGenerator.company_name(),
            "admin_name": TestDataGenerator.admin_name(),
            "admin_email": TestDataGenerator.email(),
            "admin_password": TestDataGenerator.password()
        }

    # @staticmethod
    # def company_name():

    #     return f"Automation_{uuid.uuid4().hex[:6]}"



    @staticmethod
    def company_name():
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return f"Automation{suffix}"

    @staticmethod
    def admin_name():

        return f"Admin_{uuid.uuid4().hex[:6]}"

    @staticmethod
    def email():

        return f"automation_{uuid.uuid4().hex[:6]}@gmail.com"

    @staticmethod
    def password():

        return "Test@123"

    @staticmethod
    def phone_number():

        return f"9{random.randint(100000000, 999999999)}"

    @staticmethod
    def random_text(length=10):

        return "".join(
            random.choices(string.ascii_letters, k=length)
        )

    @staticmethod
    def random_number(length=6):

        return "".join(
            random.choices(string.digits, k=length)
        )

    @staticmethod
    def random_alphanumeric(length=8):

        characters = string.ascii_letters + string.digits

        return "".join(
            random.choices(characters, k=length)
        )