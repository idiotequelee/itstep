from messages import Messages
from base import engine, Session, Base
from datetime import date as d


class Treatment:
    def __init__(self) -> None:
        Base.metadata.create_all(engine)
        self.session = Session()

    def save_user(self, message):
        record = Messages(message)
        self.session.add(record)
        self.session.commit()

    def del_user(self, message):
        self.session.query(Messages).where(
            Messages.user_id == message.from_user.id).delete()
        self.session.commit()

    def update_message(self, message):
        if self.session.query(Messages).where(
                Messages.user_id == message.from_user.id,
                Messages.date == d.fromtimestamp(
                    message.date)).count() > 0:

            self.session.query(Messages).filter(
                Messages.user_id == message.from_user.id,
                Messages.date == d.fromtimestamp(message.date)).update(
                {'text': message.text}
            )
            self.session.commit()
        else:
            self.save_user(message)

    def if_user_exists(self, message) -> bool:
        result = self.session.query(Messages).where(
            Messages.user_id == message.from_user.id).count() > 0
        return result

    def user_statistic(self, message):
        result = self.session.query(Messages).where(
            Messages.user_id == message.from_user.id)
        return '\n'.join(
            [str(i.date) + "  opinion  " + str(i.text) for i in result])

    message = {
        'faq':
            " \nBot collects information" + 
            "about your mood during the day" +
            "\nPlese rate your day from 1 to 5",
        'stop': "Goodby!\nSee you later!",
        'invalid':
            "\n/start to start\n/week to view results\n/stop to stop"
    }

    def start(self, message):
        if self.if_user_exists(message):
            return f'Dear {message.from_user.first_name},'\
                f' you are already registered!'\
                f"{self.message['invalid']}"
        else:
            self.save_user(message)
            return f"Dear {message.from_user.first_name}"\
                f"{self.message['faq']}"\
                f"{self.message['invalid']}"

    def week(self, message):
        if self.if_user_exists(message):
            return self.user_statistic(message)
        else:
            return f'Dear {message.from_user.first_name},'\
                f' you are not registered!'\
                f"{self.message['invalid']}"

    def stop(self, message):
        self.del_user(message)
        return f'Dear {message.from_user.first_name},'\
            f' you are already deleted from base!'\
            f"{self.message['invalid']}"

    def text(self, message):
        if self.if_user_exists(message):
            if message.text in ('1', '2', '3', '4', '5'):
                self.update_message(message)
                return f'Dear {message.from_user.first_name},'\
                    f' your opinion registered!'
            else:
                return f'Dear {message.from_user.first_name},'\
                    f' you made mistake, enter 1, 2, 3, 4 or 5!'\
                    f" or {self.message['invalid']}"
        else:
            return f'Dear {message.from_user.first_name},'\
                f' you are not registered!'\
                f"{self.message['invalid']}"