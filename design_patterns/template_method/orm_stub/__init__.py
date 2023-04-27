class Group:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name, group = None):
        self.name = name
        if group:
            assert isinstance(group, Group)
            self.group = group
        else:
            self.group = None

group_a = Group('A')
group_b = Group('B')

user_a = User('a')
user_b = User('b', group_a)
user_c = User('c', group_a)
user_d = User('d', group_b)

def find_group_by_name(group_name):
    if group_name == 'A': return group_a
    elif group_name =='B': return group_b
    else: return None

def find_user_by_name(user_name):
    if user_name == 'a': return user_a
    elif user_name == 'b': return user_b
    elif user_name == 'c': return user_d
    elif user_name == 'd': return user_d
    else: return None
    