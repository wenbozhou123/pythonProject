all_products=[]
shopping_cart=[]
for i in range(5):
    product = input("请输入商品:")
    all_products.append(product)
while True:
    select_num = input('请选择商品:')
    if 'q' == select_num:
        print('------------')
        print('您购物车选择的商品：')
        print(shopping_cart)
        break
    # if any(select_num in ele for ele in all_products):
    #     shopping_cart.append(select_num)
    flag = False
    for ele in all_products:
        if select_num in ele:
            shopping_cart.append(ele)
            flag = True
    if not flag:
        print('不存在该商品')


