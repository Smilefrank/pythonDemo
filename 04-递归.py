# def nums_fuc(num):
#     result = 1
#     while num > 0:
#         result *= num
#         num -= 1
#     return result
#
# print(nums_fuc(4))

def getNums(num):
    if(num > 1):
        return num * getNums(num-1)
    else:
        return num

print(getNums(4))