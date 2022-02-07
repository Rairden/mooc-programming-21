def filter_incorrect():
    open("correct_numbers.csv", "w").close()    # clear contents of file

    with open("lottery_numbers.csv", "r") as file:
        for line in file:
            ln = line.replace("\n", "").split(";")
            week = ln[0].split(" ")
            error = False

            try:
                int(week[1])
                nums = set(map(int, ln[1].split(",")))
            except:
                continue

            for n in nums:
                if not 1 <= n <= 39:
                    error = True
                    break

            if len(nums) != 7:
                error = True

            if not error:
                open("correct_numbers.csv", "a").write(line)


if __name__ == '__main__':
    filter_incorrect()
