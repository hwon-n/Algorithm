"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
"""

# 효율성 테스트 3, 4 시간 초과로 실패
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True


def solution2(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        x = ""
        for number in phone_number:
            x += number
            if x in hash_map and x != phone_number:
                return False
    return True