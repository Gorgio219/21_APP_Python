from yaml import *
import yaml
# from yaml.loader import SafeLoader
with open('todo.yml') as file:
    data = yaml.load(file, Loader=SafeLoader)

data_yaml = yaml.dump(data)
print(data_yaml)


# print(f'data_yaml = \n{data_yaml}')
for i in data:
    print(i)
    print(data[i])
