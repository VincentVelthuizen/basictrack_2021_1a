table_size = 12
line_prefix = " " * 5
line_format = ""

for i in range(table_size):
    line_format += "{:>4}"

first_line = (line_prefix + line_format).format(*range(1, table_size + 1))
second_line = "  :" + "-" * (len(first_line) - 3)

print(first_line)
print(second_line)

line_format = "{:>2}:  " + line_format
for table in range(1, table_size + 1):
    # [table * i for i in range(1, table_size + 1)] this is a special way of generating a list in line.
    # this is the short way of generating the list below
    table_list = []
    for i in range(1, table_size + 1):
        table_list.append(table * i)
    print(line_format.format(table, *table_list))
