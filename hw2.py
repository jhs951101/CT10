books = []

while True:
    order = input('삽입/추출/종료   :   ')

    if order == '종료':
        break
    elif order == '입력' or order == '삽입':
        name = input('책제목   :   ')
        author = input('저자   :   ')
        publisher = input('출판사   :   ')

        books.append( [name, author, publisher] )
    elif order == '추출':
        if len(books) <= 0:
            print('해당 책은 없습니다')
        else:
            print(books[0])
            del books[0]
    else:
        print('올바른 메뉴를 입력해주세요')

    print()
