class SMS_store:

    def __init__(self):
        self.list_of_messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        self.list_of_messages.append((False, from_number, time_arrived, text_of_sms))

    def message_count(self):
        return len(self.list_of_messages)

    def get_unread_indexes(self):
        unread = []
        for index, (read, _, _, _) in enumerate(self.list_of_messages):
            if not read:
                unread.append(index)
        return unread

    def get_message(self, i):
        if i < 0 or i > len(self.list_of_messages):
            return None
        _, from_number, time_arrived, text_of_sms = self.list_of_messages[i]
        self.list_of_messages[i] = (True, from_number, time_arrived, text_of_sms)
        return from_number, time_arrived, text_of_sms

    def delete(self, i):
        del self.list_of_messages[i]

    def clear(self):
        self.list_of_messages.clear()
