'''
    menu_test.py
'''
menu = '''
1. 메뉴 1
2. 메뉴 2
3. 메뉴 3
4. 메뉴 4
0. 종료
select menu : '''

def func1():
    print( 'func1' )
    return

def func2():
    print( 'func1' )

    return

def func3():
    print( 'func1' )

    return

def func4():
    print( 'func1' )

    return

def main():
    func_dict = { 1:func1, 2:func2, 3:func3, 4:func4 }
    while True:
        print( menu, end = ' ' )
        selectMenu = int( input() )

        if selectMenu == 0:
            break
        elif 1 <= selectMenu <= 4:
            func_dict[ selectMenu ]()

    return

if __name__ == '__main__':
    main()
