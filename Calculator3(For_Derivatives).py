import copy


def is_int(float_number):
    for value in range(0, len(str(float_number))):
        float_character = str(float_number)[value]
        if float_character == ".":
            if value == len(str(float_number))-2:
                if str(float_number)[len(str(float_number))-1] == "0":
                    return True
                else:
                    return False


def take_derivative(derivative_variable, input_term, derivative_term_list):
    constant_list = []
    if derivative_variable in input_term:
        for number in range(len(input_term)):
            character2 = input_term[number]
            if character2 != derivative_variable and character2 != "^":
                constant_list.append(character2)
            elif character2 == derivative_variable:
                try:
                    constant = float("".join(constant_list))
                except ValueError:
                    constant = 1
            else:
                exponent = int(input_term[number + 1:len(input_term)])
                break
        if not "^" in input_term:
            if "-" in str(constant):
                derivative_term_list.append(constant)
            else:
                safe_constant = "+" + str(constant)
                derivative_term_list.append(safe_constant)
        else:
            derivative_constant = constant * exponent
            derivative_exponent = exponent - 1
            if is_int(derivative_constant):
                derivative_constant = int(derivative_constant)
            if derivative_constant > 0 and function_terms.index(input_term) != 0:
                safe_derivative_constant = "+" + str(derivative_constant)
            else:
                safe_derivative_constant = str(derivative_constant)
            if derivative_exponent == 1.0:
                derivative_term_string = str(safe_derivative_constant) + derivative_variable
            elif derivative_exponent == 0:
                derivative_term_string = str(derivative_constant)
            else:
                derivative_term_string = safe_derivative_constant + derivative_variable + "^" + str(derivative_exponent)
            derivative_term_list.append(derivative_term_string)


print("Welcome to Meow Cat's Polynomial Derivative Calculator.")
print("Use ^ for exponents.")
print("Also it only supports decimal form constants.")
print("Enter a polynomial in the space below.")
function_variable = input("Input your variable: ")
polynomial = input("f(" + function_variable + ")=")

current_term = []
function_terms = []
safe_polynomial = polynomial + "+"

for item in range(len(safe_polynomial)):
    character = safe_polynomial[item]
    if character != "+" and character != "-":
        current_term.append(character)
    else:
        term_string = "".join(current_term)
        function_terms.append(copy.deepcopy(term_string))
        current_term = [character]

derivative_terms = []

for term in function_terms:
    take_derivative(function_variable, term, derivative_terms)

joined_derivative_terms = ""

for term1 in derivative_terms:
    joined_derivative_terms += (str(term1))

print("Here is your result!")
print("f'(" + function_variable + ")=" + joined_derivative_terms)
