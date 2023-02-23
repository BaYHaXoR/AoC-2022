
def main():
    with open ('test.txt', 'r') as fh:
        input_data = fh.read()
        input_data_split = input_data.strip().split('\n\n')

        print(input_data_split)

if __name__ == '__main__':
    main()