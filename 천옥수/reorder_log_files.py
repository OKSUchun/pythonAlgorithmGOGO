class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        answer = []
        for log in logs:
            log_list = list(log.split())

            if log_list[1].isnumeric():
                digit_logs.append(" ".join(log_list))
            else:
                letter_logs.append((log_list))

        letter_logs = sorted(letter_logs, key=lambda x: (x[1:], x[0]))
        letter_logs = list(map(lambda x: " ".join(x), letter_logs))
        answer = letter_logs + digit_logs
        return answer
