from multiprocessing.sharedctypes import Value


def run():
    my:list = [1, "Hello", True, 4.5]
    my_dic = {"firstname": "Antonio", "lastname": "Coca"}

    super_list = [
        {"firstname": "Marcos", "lastname": "Awia"},
        {"firstname": "Eyou", "lastname": "tva"},
        {"firstname": "Asadsdsdio", "lastname": "Casdsad"},
        {"firstname": "Atunionio", "lastname": "Mariaa"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, value)



if __name__ == '__main__':
    run()