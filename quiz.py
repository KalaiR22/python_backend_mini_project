quiz={
    "question1":{
        "question":"What is the capital of France?",
        "answer":"Paris"
    },"question2":{
        "question":"What is the capital of Germany?",
        "answer":"Berlin"
    },"question3":{
        "question":"What is the capital of Italy?",
        "answer":"Rome"
    },"question4":{
        "question":"What is the capital of Spain?",
        "answer":"Madrid"
    },"question5":{
        "question":"What is the capital of Portugal?",
        "answer":"Lisbon"
    },"question6":{
        "question":"What is the capital of Austria?",
        "answer":"Vienna"
    },
}

score=0

for key, value in quiz.items():
    print(value['question'])
    answer = input("answer?")

    if answer.lower() == value['answer'].lower:
        print("correct answer")
        score=score+1
        print("score", str(score))
    else:
        print("wrong answer")
        print("score", str(score))
        print("correct answer", value['answer'])