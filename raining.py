def go_outside():
    print("Go outside")


print("Start")
is_raining = input("Is raining?")
if is_raining.lower() == "yes":
    have_umbrella = input("Have umbrella?")
    if have_umbrella.lower() == "yes":
        go_outside()
    elif have_umbrella.lower() == "no":
        while is_raining.lower() == "yes":
            print("Wait a while")
            is_raining = input("Is raining?")
            if is_raining.lower() == "no":
                go_outside()
                break
elif is_raining.lower() == "no":
    go_outside()















