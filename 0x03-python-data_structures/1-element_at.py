#!/usr/bin/python
def element_at(my_list, idx):
    if idx > len(my_list)-1 or idx < 0:
        None
    else:
        print("Element at index {} is {}".format(idx, my_list[idx]))
