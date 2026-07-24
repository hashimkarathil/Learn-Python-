tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Marks task as done")
    print("4. Exit")


    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"task": task, "status": "pending"})

    elif choice == '2':
        if tasks == []:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["task"], "-", tasks[i]["status"])

    elif choice == '3':
        num = int(input("enter task number: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "done"
            print("Task completed.")
        else:
            print("Invalid task number.")


    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")


# output:

# 1. Add Task
# 2. View Tasks
# 3. Marks task as done
# 4. Exit
# Enter choice: 1
# Enter task: Buy groceries

# 1. Add Task
# 2. View Tasks
# 3. Marks task as done
# 4. Exit
# Enter choice: 1
# Enter task: Finish assignment 

# 1. Add Task
# 2. View Tasks
# 3. Marks task as done
# 4. Exit
# Enter choice: 2
# 1 - Buy groceries - pending
# 2 - Finish assignment - pending

# 1. Add Task
# 2. View Tasks
# 3. Marks task as done
# 4. Exit
# Enter choice: 3
# enter task number: 2
# Task completed.

# 1. Add Task
# 2. View Tasks
# 3. Marks task as done
# 4. Exit
# Enter choice: 4
# Exiting...