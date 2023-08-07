from questions import Questions

questions = Questions.from_text(
    """
How many sites are there?
How many birds were counted at the 7th site?
How many birds were counted at the last site?
What is the total number of birds counted across all sites?
What is the average number of birds seen on a site?
What is the total number of birds counted on sites with codes beginning with C? (don’t just identify this sites by eye, in the real world there could be hundreds or thousands of sites)
"""
)


def answer(*args):
    questions.answer(*args)


raw_data = [
    ["A1", 28],
    ["A2", 32],
    ["A3", 1],
    ["A4", 0],
    ["A5", 10],
    ["A6", 22],
    ["A7", 30],
    ["A8", 19],
    ["B1", 145],
    ["B2", 27],
    ["B3", 36],
    ["B4", 25],
    ["B5", 9],
    ["B6", 38],
    ["B7", 21],
    ["B8", 12],
    ["C1", 122],
    ["C2", 87],
    ["C3", 36],
    ["C4", 3],
    ["D1", 0],
    ["D2", 5],
    ["D3", 55],
    ["D4", 62],
    ["D5", 98],
    ["D6", 32],
]

data = dict(raw_data)

answer(1, len(data))
answer(2, raw_data[6][1])
answer(3, raw_data[-1][1])
answer(4, sum(data.values()))
answer(5, sum(data.values()) / len(data))
answer(6, sum(val for key, val in data.items() if key.startswith("C")))

# Produces:
"""
1. How many sites are there?
   26
2. How many birds were counted at the 7th site?
   30
3. How many birds were counted at the last site?
   32
4. What is the total number of birds counted across all sites?
   955
5. What is the average number of birds seen on a site?
   36.73076923076923
6. What is the total number of birds counted on sites with codes beginning with C? (don’t just identify this sites by eye, in the real world there could be hundreds or thousands of sites)
   248
"""
