import uuid


def create_record(surname: str, name: str, group: str) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "surname": surname,
        "name": name,
        "group": group,
    }


def create_record_id(id_employee: str, surname: str, name: str, group: str) -> dict:
    return {
        "id": id_employee,
        "surname": surname,
        "name": name,
        "group": group,
    }


def add_record(filename, record: dict):
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(f'{str(record)}\n')


def rewrite_to_file(filename, employees: list):
    with open(filename, mode='w', encoding="utf-8") as f:
        for employ in employees:
            f.write(f'{str(employ)}\n')


def get_all_entries(filename) -> list:
    result = []
    with open(filename, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline().strip()
            if not line: break
            else:
                result.append(line)
    return result


def import_csv(filename_import, filename_employees_data):
    entries = get_all_entries(filename_import)
    for entry in entries:
        surname, name, group = entry.split('#')
        employee = create_record(surname, name, group)
        add_record(filename_employees_data, employee)


def import_csv_id(filename_import, filename_employees_data):
    entries = get_all_entries(filename_import)
    for entry in entries:
        id_employee, surname, name, group = entry.split('#')
        employee = create_record_id(id_employee, surname, name, group)
        add_record(filename_employees_data, employee)


def parse_record(entry: str) -> dict:
    entry1 = entry[1:-1]
    result = {}
    contact = entry1.split(',')
    for item in contact:
        key, value = item.split(':')
        result[key.strip()[1:-1]] = value.strip()[1:-1]
    return result


def find_record_by_id(employees: list, id_record: str) -> dict:
    for employ in employees:
        record = parse_record(employ)
        if record["id"] == id_record:
            return record


def delete_record_by_id(employees: list, id_record: str) -> list:
    return [employ for employ in employees if parse_record(employ)["id"] != id_record]


def select_records_by_surname(employees: list, surname: str) -> list:
    return [employ for  employ in employees if parse_record(employ)["surname"] == surname]


def select_records_by_group(employees: list, group: str) -> list:
    return [employ for  employ in employees if parse_record(employ)["group"] == group]