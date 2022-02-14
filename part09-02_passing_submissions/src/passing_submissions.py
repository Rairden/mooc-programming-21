# Write your solution after the class ExamSubmission
# Do not make changes to the class!
import operator


class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'


def passed(submissions: list, lowestPassing: int):
    result = []

    submissions.sort(key=operator.attrgetter("points"), reverse=True)
    for sub in submissions:
        if sub.points >= lowestPassing:
            result.append(sub)
        else:
            break

    return result


if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)
