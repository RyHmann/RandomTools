from pathlib import Path

def get_data(filepath):
    lines = []
    with open(filepath) as f:
        lines = f.read().splitlines()
    return clean_numbers(lines)

def write_to_file(number_list, filepath):
    with open(filepath, 'w') as f:
        counter = 0
        for number in number_list:
            counter += 1
            if counter < len(number_list):
                f.write(number + ',\n')
            else:
                f.write(number + '\n')

def clean_numbers(number_list):
    cleaned_numbers = []
    for number in number_list:
        if number.isdigit():
            cleaned_numbers.append(number.strip(','))
    return cleaned_numbers

def print_data(number_list):
    counter = 0
    for number in number_list:
        counter += 1
        if counter < len(number_list):
            print(f'{number},')
        else:
            print(f'{number}')

if __name__ == '__main__':

    file_path = Path(__file__).with_name('needcommas.txt')

    lines = get_data(file_path)
    write_to_file(lines, file_path)
    print_data(lines)
