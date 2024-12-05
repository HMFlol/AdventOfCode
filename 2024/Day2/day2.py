from aocd import get_data
from time import time

data = get_data(day=2, year=2024)
# data = open('test.txt').read()
data = [[int(x) for x in line.split()] for line in data.splitlines()]

# How many reports are safe?
# Safe if all increasing or all decreasing AND reports differ by 1-3. More or less is not "safe".

# Part 1
def safe1(reports):
    safe_reports = []
    for report in reports:
        # I liked sorted. sorted is my friend. I also like reversing crap with ::-1. Oh.. I also really like zip. It zips! Teehee!
        if (report == sorted(report) or report == sorted(report)[::-1]) and \
        all(1 <= abs(num1 - num2) <= 3 for num1, num2 in zip(report, report[1:])):
            safe_reports.append(report)
    
    return(safe_reports)

# Part 2
def safe2(reports):
    safe_reports = []
    for report in reports:
        if safe1([report]):
            safe_reports.append(report)
        else:
            for i in range (len(report)):
                # I slice this way. I slice that way. I take out middle. Goodbye stupid useless number. haha!
                new_report = report[:i] + report[i + 1 :]
                if safe1([new_report]):
                    safe_reports.append(report)
                    break

    return(safe_reports)



start_time = time()

print(f"Part1:", len(safe1(data)))
print(f"Part2:", len(safe2(data)))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")