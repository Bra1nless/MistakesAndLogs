class Districts:
    def __init__(self, main_id, coordinates, sizes):
        self.main_id = main_id
        self.coordinates = coordinates.strip().split(",")
        self.sizes = sizes.strip().split("x")

    def __str__(self):
        return f"District {self.main_id} is located at {self.coordinates}. " \
               f"District size is {self.sizes}"

    def square_culc(self):
        x = int(self.sizes[0])
        y = int(self.sizes[1])
        return x * y

    def district_length(self):
        return self.sizes[0]


fp = open("m7-map-1.txt", "r")
file_dict = [line.strip() for line in fp]
fp.close()

new_list = []
for item in file_dict:
    if item[0] == "I" and item[1] == "D":
        new_list.append(item.split(" :: "))

file_dict = []

for item in new_list:
    file_dict.append(Districts(item[0], item[1], item[2]))

max_sq_dist = file_dict[0]

for item in file_dict:
    if item.square_culc() > max_sq_dist.square_culc():
        max_sq_dist = item

print(max_sq_dist)
