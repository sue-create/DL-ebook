# 영화 정보 저장용 딕셔너리
# key: 영화 제목, value: (장르, 평점)
movies = {
    "인터스텔라": ("SF", 9.2),
    "기생충": ("드라마", 8.6),
    "어벤져스": ("액션", 8.3)
}

def print_menu():
    print("\n=== 영화 정보 관리 시스템 ===")
    print("1. 영화 추가")
    print("2. 전체 영화 목록 보기")
    print("3. 평점 기준으로 검색")
    print("4. 종료")

def add_movie():
    title = input("영화 제목: ")
    genre = input("장르: ")
    rating = float(input("평점(0~10): "))
    movies[title] = (genre, rating)
    print(f"✅ '{title}' 추가 완료!")

def show_all_movies():
    print("\n🎬 전체 영화 목록")
    print("----------------------")
    for title, (genre, rating) in movies.items():
        print(f"{title} | 장르: {genre} | 평점: {rating}")

def search_by_rating():
    min_rating = float(input("검색할 최소 평점 입력: "))
    print(f"\n⭐️ {min_rating}점 이상인 영화 목록")
    print("----------------------")
    found = False
    for title, (genre, rating) in movies.items():
        if rating >= min_rating:
            print(f"{title} | 장르: {genre} | 평점: {rating}")
            found = True
    if not found:
        print("해당 조건에 맞는 영화가 없습니다.")

# 메인 실행 루프
while True:
    print_menu()
    choice = input("메뉴 선택 (1~4): ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        show_all_movies()
    elif choice == "3":
        search_by_rating()
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
