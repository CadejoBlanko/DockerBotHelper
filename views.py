from abc import ABC, abstractmethod

class BaseView(ABC):

    @abstractmethod
    def show_menu(self, commands):
        pass

    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def get_user_input(self, prompt):
        pass


class ConsoleView(BaseView):

    def show_menu(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))

    def show_contacts(self, contacts):
        for contact in contacts:
            print(contact)

    def show_message(self, message):
        print(message)

    def get_user_input(self, prompt):
        return input(prompt).strip().lower()