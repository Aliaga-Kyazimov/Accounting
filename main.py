import time

from Application.salary import calculate_salary
from Application.db.people import get_employees
from datetime import datetime
from tqdm import tqdm

if __name__ == "__main__":
    for i in tqdm(range(10)):
        time.sleep(0.5)
    calculate_salary()
    get_employees()
    print(datetime.now())