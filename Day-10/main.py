def draw(sprite_pos, cycle_count, cycle_string):

    if abs(sprite_pos - cycle_count) <= 1:
        cycle_string += "#"
    else:
        cycle_string += "."
    
    return cycle_string


def main():

    sprite_pos = 1
    cycle_count = 0
    cycle_string = ''

    with open ("input.txt", "r") as fh:

        for line in fh.readlines():

            line_split = line.strip().split()

            match line_split[0]:
                case "noop":
                    cycle_string = draw(sprite_pos, cycle_count, cycle_string)
                    cycle_count+=1
                case "addx":
                    cycle_string = draw(sprite_pos, cycle_count, cycle_string)
                    cycle_count+=1

                    if cycle_count % 40 == 0:
                        print(cycle_string)
                        cycle_string = ""
                        cycle_count=0
                    
                    cycle_string = draw(sprite_pos, cycle_count, cycle_string)
                    cycle_count+=1

                    sprite_pos += int(line_split[1])
            
            if cycle_count % 40 == 0:
                    print(cycle_string)
                    cycle_string = ""
                    cycle_count=0



if __name__ == '__main__':
    main()