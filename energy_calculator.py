import math

# define speed of light (m/s)
c = 3.00E8
# define planck's constant (J*s)
h = 6.626E-34


def main():
    print('Enter a RH value')
    r_h = float_input()
    print('Enter the number of levels (n)')
    max_n = int_input()
    e_list = generate_energy_levels(r_h, max_n)
    print('Enter a final n value (or values as comma separated list) for deltaE calculations and wavelength')
    n_final_list = parse_csv_integer_input(max_n)
    run_delta_e_wavelength(e_list, n_final_list)


def run_delta_e_wavelength(e_list, n_final_list):
    for n_final in n_final_list:
        print("-----------------------DELTA-E (J)-----------------------")
        d_e_list = calculate_delta_e(e_list, n_final)
        print("---------------------WAVELENGTH (nm)---------------------")
        calculate_wavelength(d_e_list, n_final)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


# Function to parse a csv integer input and check that all entered values are both integers and in csv or single
# value format
def parse_csv_integer_input(max_int):
    try:
        csv = input().split(",")
        csv_int = []
        for num in csv:
            try:
                csv_int.append(int(num))
                if int(num) >= max_int:
                    msg = "{0} is greater than the allowed maximum number, {1}.".format(num, max_int)
                    raise ValueError(msg)
            except ValueError:
                print("Enter all integers and ensure you have not entered any integers greater than {0}.".format(
                    max_int - 1))
                return parse_csv_integer_input(max_int)
        return csv_int
    except TypeError:
        print("Please enter a comma separated list of integers")
        return parse_csv_integer_input(max_int)


# Convert input to float if possible, re-prompt otherwise
def float_input():
    try:
        return float(input())
    except ValueError:
        print("Enter a number!")
        return float_input()


# Convert input to int if possible, re-prompt otherwise
def int_input():
    try:
        return int(input())
    except ValueError:
        print("Enter an integer!")
        return int_input()


# Given an Rh value and a number of energy levels, create a list containing all En(j)
def generate_energy_levels(r_h, n):
    energy_list = []
    for i in range(1, n + 1):
        val = -float(r_h) / float(math.pow(i, 2))
        energy_list.append(val)
        print("n = {0} : En = {1}".format(i, val))
    return energy_list


# Given the list of energy levels, calculate all possible delta_E values
def calculate_delta_e(e_list, n_final):
    delta_e_list = []
    for i in range(len(e_list) - 1, n_final - 1, -1):
        val = e_list[n_final - 1] - e_list[i]
        delta_e_list.append(val)
        print(i + 1, "->", n_final, ":", val)
    return delta_e_list


# lambda = h*c / E
def calculate_wavelength(d_e_list, n_final):
    wavelength_list = []
    for i in range(0, len(d_e_list)):
        val = float((h * c) / d_e_list[i])
        wavelength_list.append(val)
        val *= -1E9
        print(len(d_e_list) + n_final - i, "->", n_final, ":", val)
    return wavelength_list


main()
