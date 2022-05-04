from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report = set(report)  # 중복 제거

    user_list_who_i_report = defaultdict(set) # 신고한 유저 : 신고된 유저
    num_of_reported = defaultdict(int) # 신고된 유저 : 신고 횟수
    suspended = [] # 강퇴할 유저 목록

    for r in report:
        do_report, be_reported = r.split()

        num_of_reported[be_reported] += 1 # 신고된 유저 : 신고 횟수
        user_list_who_i_report[do_report].add(be_reported)
        # 신고한 유저 : 신고된 유저

        # k번 당했으면 suspended에 추가
        if num_of_reported[be_reported] == k:
            suspended.append(be_reported)
    for s in suspended:
        for i in range(len(id_list)):
            if s in user_list_who_i_report[id_list[i]]:
                # dict에서 dict[key] 하면 value를 출력함.
                # key = id_list일 때 정지될 유저가 value에 있는지 확인
                # i는 id_list 에서의 index 역할을 하므로
                answer[i] += 1

    return answer