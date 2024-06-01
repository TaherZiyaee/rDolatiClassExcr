red_color="\033[91m"
reset_color="\033[0;0m"
l=[1,2,3]

# print(type(dir(l)))
# print(dir(l))
word="len"
# for i in dir(l):
#     if "len" in i:
#         print(f"{red_color}{i}{reset_color} found.")

dl=dir(l)
for i in range(len(dl)):
    if word in dl[i]:
        dl[i]=red_color+dl[i]+reset_color
print(dl)

print(', '.join(str(item) for item in dl))
# print(', '.join(f"{item!r}" for item in dl))


