def safe_print_list(my_list=[],x=0):
    try:
        count = 0
        for i in range(0, x):
            print(my_list[i],end="")
            count+=1
        print("\nnb_print: {}".format(count))
    except:
        IndexError
