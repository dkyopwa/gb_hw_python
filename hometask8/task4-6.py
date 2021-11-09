#!/usr/bin/env python
# nevl 2021

class Warehouse:

    def __init__(self, warehouse_data: dict):
        # warehouse_data: type: count
        self.data = warehouse_data
        self.in_department = dict()

    def put(self, type_of_equipment, count, department):
        try:
            count = int(count)
        except:
            return False

        if f'{type_of_equipment}-{department}' not in self.in_department:
            self.in_department[f'{type_of_equipment}-{department}'] = 0
        elif count > self.in_department[f'{type_of_equipment}-{department}']:
            return False
        else:
            self.in_department[f'{type_of_equipment}-{department}'] -= count

        if type_of_equipment not in self.data:
            self.data[type_of_equipment] = count
        else:
            self.data[type_of_equipment] += count

        return True

    def get(self, type_of_equipment, count, department):
        try:
            count = int(count)
        except:
            return False

        if type_of_equipment not in self.data:
            return False
        if count > self.data[type_of_equipment]:
            return False
        self.data[type_of_equipment] -= count
        if f'{type_of_equipment}-{department}' not in self.in_department:
            self.in_department[f'{type_of_equipment}-{department}'] = count
        else:
            self.in_department[f'{type_of_equipment}-{department}'] += count

        return True

    def get_count(self, type_of_equipment, department=''):
        """
        Return count of equipment in department or in warehouse if department not set
        :param type_of_equipment: string
        :param department: string
        :return: number
        """
        if not department:
            return self.data.get(type_of_equipment, 0)
        else:
            return self.in_department.get(f'{type_of_equipment}-{department}', 0)


class OfficeEquipment:

    def __init__(self, cost, size: tuple):
        self.cost = cost
        self.size = size


class Printer(OfficeEquipment):

    def __init__(self, cost, size: tuple, printer='hp'):
        super().__init__(cost, size)
        self.printer = printer


class Scanner(OfficeEquipment):

    def __init__(self, cost, size: tuple, scanner='hp'):
        super().__init__(cost, size)
        self.scanner = scanner


class Copier(OfficeEquipment):

    def __init__(self, cost, size: tuple, copier='xerox'):
        super().__init__(cost, size)
        self.copier = copier


if __name__ == '__main__':
    p = Printer(1000, (20, 30, 50), 'Samsung')
    s = Scanner(250, (10, 50, 40), 'Canon')
    c = Copier(2500, (100, 60, 70), 'HP')

    warehouse = Warehouse({p.__hash__(): 20,
                           s.__hash__(): 20,
                           c.__hash__(): 30})

    for dep in ['', 'dep1', 'dep2']:
        print('There are {} prints in the {}'.format(warehouse.get_count(p.__hash__(), dep),
                                                     'warehouse' if not dep else dep))

    if not warehouse.get(p.__hash__(), 10, 'dep1'):
        print('1. Something went wrong while get printer from warehouse in dep1')
    if not warehouse.get(p.__hash__(), 'ten', 'dep2'):
        print('2. Something went wrong while get printer from warehouse in dep2')
    if not warehouse.get(p.__hash__(), 11, 'dep2'):
        print('3. Something went wrong while get printer from warehouse in dep2')
    if not warehouse.get(p.__hash__(), 9, 'dep2'):
        print('4. Something went wrong while get printer from warehouse in dep2')

    for dep in ['', 'dep1', 'dep2']:
        print('There are {} prints in the {}'.format(warehouse.get_count(p.__hash__(), dep),
                                                     'warehouse' if not dep else dep))

    if not warehouse.put(p.__hash__(), 10, 'dep2'):
        print('5. Something went wrong while put printer to warehouse from dep2')
    if not warehouse.put(p.__hash__(), 9, 'dep2'):
        print('6. Something went wrong while put printer to warehouse from dep2')
    if not warehouse.put(p.__hash__(), 9, 'dep1'):
        print('7. Something went wrong while put printer to warehouse from dep2')
    if not warehouse.put(p.__hash__(), 9, 'dep1'):
        print('8. Something went wrong while put printer to warehouse from dep2')

    for dep in ['', 'dep1', 'dep2']:
        print('There are {} prints in the {}'.format(warehouse.get_count(p.__hash__(), dep),
                                                     'warehouse' if not dep else dep))
