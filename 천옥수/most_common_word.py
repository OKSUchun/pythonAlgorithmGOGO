from collections import defaultdict
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        answer = ""

        def multi_split(paragraph):
            paragraph_list = re.split("! | ? | ' |,| ; | \.|, ", paragraph)
            while "" in paragraph_list:
                paragraph_list.remove("")
            return paragraph_list

        def remove_punctuation(string: str) -> str:
            lst = [chr for chr in list(string) if chr.isalpha()]
            string = "".join(lst)
            return string

        def remove_banned(paragraph_list, banned_list):
            if banned_list and paragraph_list:
                for ban in banned_list:
                    while ban in paragraph_list:
                        paragraph_list.remove(ban)
            return paragraph_list

        paragraph_list = multi_split(paragraph)
        revised_list = list(
            map(lambda x: remove_punctuation(x.lower()), paragraph_list)
        )
        removed_list = remove_banned(revised_list, banned)

        def count_freq(revised_list):
            counter = defaultdict(int)
            for word in revised_list:
                counter[word] += 1
            return counter

        counter = count_freq(revised_list)
        answer = max(counter, key=counter.get)

        return answer
