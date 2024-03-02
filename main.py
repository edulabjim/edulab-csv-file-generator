import csv
import random
import os
import shutil
from faker import Faker

GROUPS = ['Freshman', 'Sophomore', 'Junior', 'Senior']
fake = Faker()

def generate_id():
    return random.randint(100000000, 999999999)

def generate_phone():
    return 1 * 10**9 + random.randint(100000000, 999999999)

def generate_name():
    return fake.first_name()

def generate_email(name):
    return f'{name.lower()}@hueg-24-university.edu'

def main():
    output_dir = 'output'
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    num_contacts = int(input('Enter the number of contacts to generate: '))
    with open(os.path.join(output_dir, 'contacts.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'phone', 'group', 'name', 'email'])
        for _ in range(num_contacts):
            id = generate_id()
            phone = generate_phone()
            group = random.choice(GROUPS)
            name = generate_name()
            email = generate_email(name)
            writer.writerow([id, phone, group, name, email])

if __name__ == '__main__':
    main()