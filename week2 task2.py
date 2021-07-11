def main():
    
    value = 2000
    loss = 0.1
    my_function(value, loss)

def my_function(val, los):
    year = 0

    while val > 1000:
        year = year + 1
        val = val - (val * los)
        print("For year", year, "the cost of the bike is: ", val)

main()
