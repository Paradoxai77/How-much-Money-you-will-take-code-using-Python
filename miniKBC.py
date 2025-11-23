import time
import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
      {
        "question": "Who developed the theory of General Relativity?",
        "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "D) Stephen Hawking"],
        "answer": "B"
    },
    {
        "question": "Which algorithm is used in Google's PageRank?",
        "options": ["A) BFS", "B) DFS", "C) Markov Chain", "D) Dijkstra"],
        "answer": "C"
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["A) O(n)", "B) O(n log n)", "C) O(log n)", "D) O(1)"],
        "answer": "C"
    },
    {
        "question": "Who is known as the father of AI?",
        "options": ["A) John McCarthy", "B) Alan Turing", "C) Marvin Minsky", "D) Geoffrey Hinton"],
        "answer": "A"
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["A) Saturn", "B) Jupiter", "C) Uranus", "D) Neptune"],
        "answer": "A"
    },
    {
"question": "Which sorting algorithm is best for nearly sorted data?",
        "options": ["A) Quick Sort", "B) Merge Sort", "C) Bubble Sort", "D) Insertion Sort"],
        "answer": "D"
    },
    {
        "question": "In which year did the C language appear?",
        "options": ["A) 1969", "B) 1972", "C) 1979", "D) 1983"],
        "answer": "B"
    },
    {
        "question": "What is the full form of HTTP?",
        "options": ["A) Hyper Transfer Text Protocol", "B) Hyper Text Transfer Protocol", "C) High Text Transfer Protocol", "D) Hyper Text Transmission Protocol"],
        "answer": "B"
    },
    {
        "question": "Who is the current CEO of Google (as of 2025)?",
        "options": ["A) Satya Nadella", "B) Tim Cook", "C) Sundar Pichai", "D) Jeff Bezos"],
        "answer": "C"
    },
    {
        "question": "Which logic gate outputs true only when inputs differ?",
        "options": ["A) AND", "B) OR", "C) XOR", "D) NOR"],
        "answer": "C"
    },
    {
        "question": "Which Indian scientist won a Nobel Prize in Physics?",
        "options": ["A) C.V. Raman", "B) Homi Bhabha", "C) A.P.J. Abdul Kalam", "D) Vikram Sarabhai"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Kazakhstan?",
"options": ["A) Astana", "B) Almaty", "C) Tashkent", "D) Bishkek"],
        "answer": "A"
    },
    {
        "question": "Which country has the largest proven oil reserves?",
        "options": ["A) USA", "B) Saudi Arabia", "C) Venezuela", "D) Russia"],
        "answer": "C"
    },
    {
        "question": "Which number is neither prime nor composite?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "B"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A) Quartz", "B) Gold", "C) Diamond", "D) Graphite"],
        "answer": "C"
    },
    {
        "question": "Which Indian city is known as 'Silicon Valley of India'?",
        "options": ["A) Pune", "B) Bengaluru", "C) Hyderabad", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "Which programming language is used for AI the most?",
        "options": ["A) Java", "B) Python", "C) C#", "D) Ruby"],
        "answer": "B"
    },
    {
        "question": "Which planet has the longest day?",
        "options": ["A) Mercury", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "Which Indian satellite was first launched into space?",
"options": ["A) INSAT-1", "B) Aryabhata", "C) PSLV", "D) Bhaskara"],
        "answer": "B"
    },
    {
        "question": "What is the full form of RAM?",
        "options": ["A) Read All Memory", "B) Random Access Memory", "C) Run Access Mode", "D) Real Action Memory"],
        "answer": "B"
    }
]

lifelines = {
    "50:50": True,
    "Audience Poll": True,
    "Phone a Friend": True,
    "Flip the Question": True
}

def use_lifeline(q, ans):
    print("\nAvailable Lifelines:")
    for key, val in lifelines.items():
        if val:
            print(f"- {key}")
    choice = input("Choose a lifeline or press Enter to skip: ").strip()
    
    if choice == "50:50" and lifelines["50:50"]:
        lifelines["50:50"] = False
        wrong = [opt for opt in ['A', 'B', 'C', 'D'] if opt != ans]
        removed = random.sample(wrong, 2)
        print("\n50:50 Lifeline: Remaining options:")
        for opt in q["options"]:
            if opt[0] not in removed:
                print(opt)

    elif choice == "Audience Poll" and lifelines["Audience Poll"]:
        lifelines["Audience Poll"] = False
        print("Audience Poll suggests:", ans)

    elif choice == "Phone a Friend" and lifelines["Phone a Friend"]:
        lifelines["Phone a Friend"] = False
        print("Your friend thinks the answer is:", ans)

    elif choice == "Flip the Question" and lifelines["Flip the Question"]:
        lifelines["Flip the Question"] = False
        print("Question flipped!\n")
        return "flip"
    else:
        print("Invalid or already used lifeline.")
    return None


score = 0
prize_money = [1000]
asked = []
for i in range(10):  # Random 10 questions
    q = random.choice(questions)
    questions.remove(q)
    print(f"i+1: {q['question']}")
    for opt in q["options"]:
        print(opt)
    
    lifeline_result = use_lifeline(q, q["answer"])
    if lifeline_result == "flip":
        continue  # skip question

    print("You have 4 minutes to answer...")
    start_time = time.time()
    while True:
        if time.time() - start_time > 20:
            print("Time's up!")
            break
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            break

    end = time.time()

    if answer.upper() == q['answer']:
        prize_money.append(prize_money[-1] * 2)
        print(f"Correct! You won ₹{prize_money[-1]}")
    else:
        print("Wrong answer. Game over.")
        break

print(f"Your total winning amount: ₹{prize_money[-1]}")
print(f"\nTotal Correct Answers: {score}")
