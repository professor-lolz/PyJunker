# -*- coding: utf-8 -*-
# https://github.com/professor-lolz/PyJunker ( v1.0 )
import argparse
import random
import string
import sys
import re
import os

def generate_name(length: int = 16) -> str:
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_function() -> str:
    function_name = generate_name()
    return_value = generate_random_return_value()
    return f'def {function_name}() -> {return_value[0]}:\n    return {return_value[1]}\n\n'

def generate_random_return_value() -> list[str, str]:
    return_value_types = ['int', 'str', 'bool']
    return_value_type = random.choice(return_value_types)

    if return_value_type == 'int':
        return [return_value_type, random.randint(1, 2000000000)]
    elif return_value_type == 'str':
        return [return_value_type, f"'{''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10,100)))}'"]
    else:
        return [return_value_type, random.choice([True, False])]

def work(input_file: str, output_file: str, count: int) -> None:

    with open(input_file, 'r') as file:
        content = file.read()
        functions = re.findall(r'(?:^|\n)\s*def\s+(\w+)\(', content)

    new_names = {function: generate_name() for function in functions}
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()

    down_count = random.randint(9, count)
    temp_name = f'@temp_{generate_name()}.tmp'

    with open(temp_name, 'w') as temp_file:
        for line in lines:
            for old_name, new_name in new_names.items():
                line = line.replace(old_name + '(', new_name + '(')
            temp_file.write(line)

        temp_file.write('\n\n')
        for junk_function in [generate_function() for _ in range(down_count)]:
            temp_file.write(junk_function)

    with open(temp_name, 'r') as temp_file:
        temp_total = temp_file.read()

    with open(output_file, 'w') as output_file:
        for junk_function in [generate_function() for _ in range(count-down_count)]:
            output_file.write(junk_function)
        output_file.write(temp_total)

    os.remove(temp_name)

    print("=== Junk completed successfully. ===")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input_file", help="input file", required=True)
    parser.add_argument("-o", "--output_file", help="output file", required=True)
    parser.add_argument("-c", "--count", help="count junk functions", type=int, required=True)
    args = parser.parse_args()
    print('Developed by https://github.com/professor-lolz (tg: @professor_contact)')

    if len(sys.argv) != 7:
        print("Error: Expected exactly 6 arguments, but received", len(sys.argv) - 1)
        print("Usage: python3 PyJunker.py -f [input_file] -o [output_file] -c [count]")
        return

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        return
    
    if args.count < 100:
        print("Error: Count junk-functions must be at least 100.")
        return

    work(args.input_file, args.output_file, args.count)

if __name__ == '__main__':
    main()