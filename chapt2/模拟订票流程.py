all_ticket = []
title_1 = ['车次','出发站-到达站','出发时间','到达时间']
ticket_1 = ['G1569','北京南-天津南','18：06','18：39']
ticket_2 = ['G1234','北京南-天津南','18：15','18：40']
ticket_3 = ['G329','北京南-天津南','18：30','17：09']
ticket_4 = ['G2048','北京南-天津南','18：41','17：15']
trains = ['G1569', 'G1234', 'G1234', 'G1234']

all_ticket.append(title_1)
all_ticket.append(ticket_1)
all_ticket.append(ticket_2)
all_ticket.append(ticket_3)
all_ticket.append(ticket_4)

print(all_ticket[1:])
train_tick_map = dict(zip(trains, all_ticket[1:]))
print(train_tick_map)


for ticket in all_ticket:
    for title in ticket:
        print(title, end='\t')
    print()
