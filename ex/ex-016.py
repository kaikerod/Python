nums = [{},{},{},{},{}]

for i in nums:
    i['num'] = int(input('Digite um número: '))
    print(f'O número {i["num"]} foi adicionado com sucesso!')

print(nums)