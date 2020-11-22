from datetime import datetime

from how_to_think.chapter_11.section_1_12.sms_store import SMS_store

my_inbox = SMS_store()

# should be 0
print(my_inbox.message_count())

my_inbox.add_new_arrival(1234567890, datetime.now(), "New phone, who dis?")
my_inbox.add_new_arrival(1234567890, datetime.now(), "Good afternoon, how might I help you?")

# should be 2
print(my_inbox.message_count())
# should be [0, 1]
print(my_inbox.get_unread_indexes())

from_number, time_arrived, message = my_inbox.get_message(0)
print("   from: {}\n"
      "     at: {}\n"
      "message: {}".format(from_number, time_arrived, message))

# should be [1]
print(my_inbox.get_unread_indexes())

my_inbox.delete(1)

# should be []
print(my_inbox.get_unread_indexes())

my_inbox.clear()

# should be 0 again
print(my_inbox.message_count())
