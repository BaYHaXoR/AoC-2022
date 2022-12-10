def move_head(x, y, direction, distance):

    if direction == "U":
        y += distance
    elif direction == "D":
        y -= distance
    elif direction == "L":
        x -= distance
    else:
        x += distance
    return (x, y)

def move_tail(x_pos_tail, y_pos_tail, x_pos_head, y_pos_head, direction, visited_set, end_of_rope):

    # ignore moves that are less than one space apart
    if abs(x_pos_head - x_pos_tail) <= 1 and abs(y_pos_head - y_pos_tail) <= 1:
        return x_pos_tail, y_pos_tail, visited_set
        
    if direction == "U":
        if x_pos_head != x_pos_tail:
            x_pos_tail = x_pos_head

        while y_pos_tail != y_pos_head - 1:
            y_pos_tail += 1
            if end_of_rope:
                visited_set.add((x_pos_tail, y_pos_tail))
    elif direction == "D":
        if x_pos_head != x_pos_tail:
            x_pos_tail = x_pos_head

        while y_pos_tail != y_pos_head + 1:
            y_pos_tail -= 1
            if end_of_rope:
                visited_set.add((x_pos_tail, y_pos_tail))
    elif direction == "R":
        if y_pos_head != y_pos_tail:
            y_pos_tail = y_pos_head

        while x_pos_tail != x_pos_head - 1:
            x_pos_tail += 1
            if end_of_rope:
                visited_set.add((x_pos_tail, y_pos_tail))
    else:
        if y_pos_head != y_pos_tail:
            y_pos_tail = y_pos_head

        while x_pos_tail != x_pos_head + 1:
            x_pos_tail -= 1
            if end_of_rope:
                visited_set.add((x_pos_tail, y_pos_tail))

    return x_pos_tail, y_pos_tail, visited_set

def main():

    rope_dict = {0: (0,0)}

    for i in range(1, 10):
        rope_dict[i] = (0,0)

    visited_set = set((10000,10000))

    with open("test.txt", "r") as fh:
        for line in fh.readlines():
            direction, distance = line.strip().split()

            x_head, y_head = rope_dict[0]

            rope_dict[0] = move_head(x_head, y_head, direction, int(distance))

            for i in range(1, 10):
                new_x, new_y = rope_dict[i]
                end_of_rope = False
                if i == 9:
                    end_of_rope = True
                new_x, new_y, visited_set = move_tail(new_x, new_y, x_head, y_head, direction, visited_set, end_of_rope)
                rope_dict[i] = (new_x,new_y)

            rope_dict[0] = (x_head, y_head)

    print(len(visited_set))
    print(visited_set)
  

if __name__ == '__main__':
    main()


#Just create extra ropes and track them all!!!!