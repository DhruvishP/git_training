from utils.calculator import add_nums, subtract_nums

if __name__ == "__main__":
    result = add_nums(5, 10)
    print(f"The result of adding 5 and 10 is: {result}")
    print(f"The result of subtracting 10 from 5 is: {subtract_nums(5, 10)}")