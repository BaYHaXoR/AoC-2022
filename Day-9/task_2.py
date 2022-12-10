def move_head(x_head, y_head, direction):
    if direction == "U":
        y_head += 1
    if direction == "D":
        y_head -= 1
    if direction == "R":
        x_head += 1
    if direction == "L":
        x_head -= 1
    return x_head, y_head

def move_piece(x_current, y_current, x_last, y_last):

    if abs(x_last - x_current) <= 1 and abs(y_last - y_current) <= 1:
        return x_current, y_current
    
    if (y_last != y_current) and (x_last != x_current):
        if x_last > x_current:
            x_current+=1
        else:
            x_current-=1
        if y_last > y_current:
            y_current+=1
        else:
            y_current-=1
    else:
        if x_last > x_current:
            x_current+=1
        elif x_last < x_current:
            x_current-=1
        elif y_last > y_current:
            y_current+=1
        else:
            y_current-=1
    
    return x_current, y_current

def main():

    rope = []
    for i in range(0, 10):
        rope.append([0,0])

    visited_set = set()

    with open("test.txt", "r") as fh:
        for line in fh.readlines():

            direction, distance = line.strip().split()

            for i in range(int(distance)):
                rope[0][0], rope[0][1] = move_head(rope[0][0], rope[0][1], direction)
                for x in range(1, 10):
                    rope[x][0], rope[x][1] = move_piece(rope[x][0], rope[x][1], rope[x-1][0], rope[x-1][1])
            
                visited_set.add((rope[9][0], rope[9][1]))


    print(len(visited_set))
    #print(visited_set)

if __name__ == '__main__':
    main()
