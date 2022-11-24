import view, model


FILENAME_DATA = 'employees.txt'

def main():
    while True:
        data = view.show_main_menu()
        if not data or data == 9: break

        if data == 1:
            surname = view.show_surname()
            name = view.show_name()
            group = view.show_group()
            record = model.create_record(surname, name, group)
            model.add_record(FILENAME_DATA, record)

        if data == 5:
            filename_import = view.show_filename()
            model.import_csv_id(filename_import, FILENAME_DATA)

        if data == 6:
            filename_import = view.show_filename()
            model.import_csv(filename_import, FILENAME_DATA)

        if data in [2, 3, 4]:  
            employees = model.get_all_entries(FILENAME_DATA)
            id_employ = view.show_id()
            record = model.find_record_by_id(employees, id_employ)
            if not record:
                view.show_no_record()
                continue
            else:
                view.show_record(record)
            if data == 3:
                view.show_message_new_record()
                new_record = model.create_record_id(id_employ, view.show_surname(), view.show_name(), view.show_group())
                new_employees = model.delete_record_by_id(employees, id_employ)
                model.rewrite_to_file(FILENAME_DATA, new_employees)
                model.add_record(FILENAME_DATA, new_record)
            if data == 4:
                new_employees = model.delete_record_by_id(employees, id_employ)
                model.rewrite_to_file(FILENAME_DATA, new_employees)
                view.show_message_delete_record()

        if data == 7:
            employees = model.get_all_entries(FILENAME_DATA)
            surname = view.show_surname()
            records = model.select_records_by_surname(employees, surname)
            if not records:
                view.show_no_record()
            else:
                for record in records:
                    view.show_record(model.parse_record(record))

        if data == 8:
            employees = model.get_all_entries(FILENAME_DATA)
            group = view.show_group()
            records = model.select_records_by_group(employees, group)
            if not records:
                view.show_no_record()
            else:
                for record in records:
                    view.show_record(model.parse_record(record))