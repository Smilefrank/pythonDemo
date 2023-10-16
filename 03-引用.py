
# A = [12,23,54,"wang"]
# B = A
# B.append("Baofeng")
# print(id(A))
# print(id(B))
# print(B)


# a = 12
# a = 45
# print(a)


#
# 字符串不可变类型
# str = "wang"
# str[0] = "H"
# print(str)

# 不可以修改元祖的值
# temp = (23,43,"hhh")
# temp[2] = 55
# print(temp[2])

#  可变的数据类型：列表、集合、字典
# 数组可以修改
info = [23,24,35,36,56,78]
info[0] = 99
print(info[0])


info = {"name":"wangbaofeng",(23,34):"hhggg"}#元组可以作为Key 可哈希
# info = {"age":23,[23,34]:"hhkkk"}   #错误写法 数组不可以作为key  不可哈希    
print(info)












