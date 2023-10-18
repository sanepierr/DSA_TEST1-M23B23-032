import numpy as np

# Create a NumPy array with a mix of complex and real numbers
array = np.array([1 + 1j, 1 + 0j, 4.5, 3, 2, 2j])

# Test element-wise for complex numbers
is_complex = np.iscomplex(array)

# Test element-wise for real numbers
is_real = np.isreal(array)

# Test if a given number is of a scalar type
is_scalar = np.isscalar(3.1)

# Print the results
print("Is complex:", is_complex)
print("Is real:", is_real)
print("Is scalar:", is_scalar)
