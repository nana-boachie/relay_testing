# relay_testing
To aid in testing relay trip time for now


Certainly! Let's walk through the code with the input values psm = 10, tms = 1, and curve = B.

    The code defines four functions (standard_inverse, very_inverse, extremely_inverse, and long_time_inverse) which are mathematical formulas representing different types of time-current characteristic curves used in electrical protection devices.

    In the main() function:
        It initializes a list curves containing the valid curve types: A, B, C, and D.
        Takes user input for psm and tms.
        Asks the user to input the desired curve type until a valid one is provided (A, B, C, or D).

    After obtaining valid inputs, the program checks the value of curve and calculates the operating time using the corresponding function:
        If curve == "A", it calculates the operating time using the standard_inverse function.
        If curve == "B", it calculates the operating time using the very_inverse function.
        If curve == "C", it calculates the operating time using the extremely_inverse function.
        If curve == "D", it calculates the operating time using the long_time_inverse function.

    For the input values psm = 10, tms = 1, and curve = B:
        It uses the very_inverse function: operating_time = 1 * (13.5 / (10 - 1)).
        Calculating this expression gives the operating time.

    The final result is then printed to the console.

Expected output for psm = 10, tms = 1, and curve = B: