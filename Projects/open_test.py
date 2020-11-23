from Projects.proj09.proj09 import build_dictionary


fp = open("2015_small.csv")
print("Opened 2015_small.csv")
instructor = {'Western Europe': {'Switzerland': ((1, 7.587), (1.39651, 0.41978), (1.34951, 0.94143, 0.66557)), 'Iceland': ((2, 7.561), (1.30232, 0.14145), (1.40223, 0.94784, 0.62877)), 'Denmark': ((3, 7.527), (1.32548, 0.48357), (1.36058, 0.87464, 0.64938)), 'Norway': ((4, 7.522), (1.459, 0.36503), (1.33095, 0.88521, 0.66973))}, 'North America': {'Canada': ((5, 7.427), (1.32629, 0.32957), (1.32261, 0.90563, 0.63297))}}
print("Instructor:")
print(instructor)
student = build_dictionary(fp)
print("Student:")
print(student)
assert instructor == student