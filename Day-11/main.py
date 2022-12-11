import re

def initialise_monkey(instruction_set):
    monkey = {}
    monkey["handled"] = 0
    monkey['items'] = [int(item) for item in re.findall(r'[0-9]+', instruction_set[1])]
    monkey['operation'] = re.findall(r'old.*', instruction_set[2])[0]
    monkey['test'] = int(re.findall(r'[0-9]+', instruction_set[3])[0])
    monkey['true'] = int(re.findall(r'[0-9]+', instruction_set[4])[0])
    monkey['false'] = int(re.findall(r'[0-9]+', instruction_set[5])[0])

    return monkey


def monkey_handler(monkey_list, monkey, i):
    
    current_monkey = monkey_list[monkey]
    
    while len(current_monkey['items']) > 0:
        worry = current_monkey['items'].pop()

        operation_split = current_monkey['operation'].split()

        value_one = worry if operation_split[0] == "old" else int(operation_split[0])
        value_two = worry if operation_split[2] == 'old' else int(operation_split[2])

        match operation_split[1]:
            case '+':
                worry = value_one + value_two
            case '/':
                worry = value_one / value_two
            case '*':
                worry = value_one * value_two
            case '-':
                worry = value_one - value_two

        if worry > 9699690:
            worry = worry % 9699690

        test_success = worry % current_monkey['test'] == 0

        if test_success:
            #worry = worry // current_monkey['test']
            monkey_list[current_monkey['true']]['items'].append(worry)
        
        else:
            monkey_list[current_monkey['false']]['items'].append(worry)    

        current_monkey['handled'] +=1

    return monkey_list


def main():

    file_content = ""
    with open("input.txt", "r") as fh:
        file_content = fh.read()
    
    monkey_instruction_set = file_content.split('\n\n')
    monkey_instruction_set_split = [instruction.split("\n") for instruction in monkey_instruction_set]

    monkey_list = [initialise_monkey(instruction_set) for instruction_set in monkey_instruction_set_split]

    for i in range(10000):
        print(f'Round: {i}')
        for monkey in range(len(monkey_list)):
            monkey_list = monkey_handler(monkey_list, monkey, i)
    
    handled_count_list = [monkey['handled'] for monkey in monkey_list]
    handled_count_list.sort(reverse=True)

    print(handled_count_list[0] * handled_count_list[1])
    

if __name__ == '__main__':
    main()