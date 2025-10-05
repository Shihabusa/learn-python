marks={
    "harry":100,
    "chutia":92,
    "vodai":78,
    90:"puspita"
}
print(marks,type(marks))#class dic it can find out
print(marks["harry"])#print its pair 100
print(marks.items())#all item will be shown in grouply
print(marks.keys())#left side e ja ja thake
print(marks.values())#right side e ja ja thake
marks.update({"harry":95})#mutable means changable
print(marks)
print(marks.get(90))#left element diye search and do not return error