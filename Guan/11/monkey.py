class Monkey:
    """
        name - monkey's name.
        starting item - indicates how the worry level of the money starts.
        operation - the operation of worry level as the monkey holds the items.
        test - the test that the monkey want to divide by.
        true senario - the senario that if true, will happen to the monkey name.
        false senario - the senario that if false, will happen to the monkey name.
    """
    def __init__(self, name, starting_items, operation, test, true_senario, false_senario) -> None:
        self.name  = name
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.true_senario = true_senario
        self.false_senario = false_senario
    
    def get_true_senario(self):
        return self.true_senario
    
    def get_false_senario(self):
        return self.false_senario

    # Replace the old starting items list.
    def update_starting_item(self, new_starting_item):
        self.starting_items = new_starting_item

    # append to the new starting items list.
    def append_starting_item(self, new_starting_item):
        self.starting_items.append(new_starting_item)
    
    # Should pop the front and append it to other monkeys.
    def pop_starting_item(self):
        self.starting_items.pop(0)

    # test if things works.
    def inspect_worry_level(self,item):
        if (self.operation == "+"):
            return item + self.value
        elif (self.operation == "-"):
            return item - self.value
        elif (self.operation == "squared"):
            return item ** 2
        elif (self.operation == "*"):
            return item * self.value
        elif (self.operation == '/'):
            return item / self.value
        else:
            KeyError


