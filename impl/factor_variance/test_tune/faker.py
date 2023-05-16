import csv
import random
from ml.constant import test_data as td
from faker import Faker

def make_fake(path_to_write):
  fake = Faker()

  with open(path_to_write, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'email', 'department', 'sale_type', 'cancel'])
    
    for index in range(3000):
      email = _define_email(fake)
      cancel = random.choice(td['cancel'])
      sale_type = random.choice(td['sale_type'])

      writer.writerow([index + 1, email, _department(sale_type), sale_type, cancel])
      repeat_max = _repeat_count(sale_type)
      for _ in range(repeat_max):
        if _need_stop():
          break
        writer.writerow([index + 1, email, _department(sale_type), sale_type, cancel])

def _define_email(fake):
  address = fake.name().lower().replace(' ', '-').replace('.', '')
  domain = random.choice(td['email_domain'])
  return address + domain

def _need_stop():
  return random.choice([True, False])

def _repeat_count(sale_type):
  if sale_type is None:
    return len(td['department'])
  else:
    return 0

def _department(sale_type):
  if sale_type is None:
    return random.choice(td['department'])
  else:
    return None