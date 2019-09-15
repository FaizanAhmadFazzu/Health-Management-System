#Health Management System
client_list={1:"Raju",2:"Rohan",3:"Hammad"}#Dictionary for client list
work_list={1:"Exercise",2:"Food"}#Dictionary for work


def get_datetime():
    """"function returns date and time"""
    import datetime
    return datetime.datetime.now()

try:
    def choose_clients():
        """"function to choose clients"""
        print("Choose clients : ")
        for x in client_list:
            print("Press key ", x, " for ", client_list[x])
        x = int(input())
        client_name=client_list[x]
        print("Selected client : ", client_name)
        return client_name

    print("select options : ")
    print("Press key 1 for Log : ")
    print("Press key 2 for Retrieve: ")
    inp = int(input())
    print("Selected job")

    def get_work(x):
        """"function returns work_name"""
        work_name=work_list[x]
        return work_name
    def log_work():
        """"function to log work"""
        for x in work_list:
            print("Press ", x, " to log ", work_list[x])
        x = int(input())
        work_name=get_work(x)
        client_name = choose_clients()
        with open(client_name + "_" + work_name + ".txt", "a") as file:
            while (True):
                print("Enter " + work_name)
                mytext = input()
                file.write("[" + str(get_datetime()) + "] : " + mytext+"\n")
                k = input("ADD MORE ? Y/N : ")
                if k is "N" or k is "Y":
                    if k is "Y":
                        continue
                    elif (k is "N"):
                        break
                else:
                    print("Wrong input : \n try again")
                    break
        file.close()


    def ret_work():
        """"function to retrieve work"""
        for x in work_list:
            print("Press ", x, " to retrieve ", work_list[x])
        x = int(input())
        work_name=get_work(x)
        client_name = choose_clients()
        print(client_name+"-"+work_name+" Report : ",)
        with open(client_name + "_" + work_name + ".txt",) as file:
            contents=file.readlines()
            for x in contents:
                print(x)
            file.close()




    if inp is 1:
        log_work()

    if inp is 2:
        ret_work()
except Exception as e:
    print("Oops Something went wrong\ntry again")






