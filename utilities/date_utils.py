from datetime import date, timedelta


class DateUtils:

    @staticmethod
    def today():

        return date.today().strftime("%Y-%m-%d")

    @staticmethod
    def days_before(days):

        return (
            date.today() - timedelta(days=days)
        ).strftime("%Y-%m-%d")

    @staticmethod
    def days_after(days):

        return (
            date.today() + timedelta(days=days)
        ).strftime("%Y-%m-%d")