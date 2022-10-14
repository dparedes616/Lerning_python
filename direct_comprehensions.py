def run():
    my_dict = {}
    
    for i in range(1, 101):
        if i %3 !=0:
            my_dict[i] = i**3

    print(my_dict)


    my_dict2 = {i: i**3 for i in range(1, 101) if i %3 !=0}
    print(my_dict2)

    my_dict3 = {i: i**0.5 for i in range(1, 10)}
    print(my_dict3)









if __name__ == "__main__":
    run()