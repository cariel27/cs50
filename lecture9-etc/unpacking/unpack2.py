def f(*args, **kwargs):
    print("Positional args:", args)
    print("Positional kwargs:", kwargs)


list_tmp = [1, 2, 3]
dict_tmp = {"name": "Jax", "power": 9.8}

# print("\nf(100, 50, 25, name='ariel')")
# f(100, 50, 25, name="ariel")
#
# print("\nf(name='ariel')")
# f(name="ariel")

print("\nf(list_tmp, dict_tmp)")
f(list_tmp, dict_tmp)

print("\nf(list_tmp, new_dict=dict_tmp)")
f(list_tmp, new_dict=dict_tmp)
