# Question

class Question:
  def __init__(self, text, choices, answer):
    self.text = text
    self.choices = choices
    self.answer = answer
  def checkAnswer(self, answer):
    return self.answer == answer

# Quiz
class Quiz:
  def __init__(self, questions):
    self.questions = questions
    self.score = score = 0
    self.questionIndex = 0

  def getQuestion(self):
    return  self.questions[self.questionIndex]

  def displayQuestion(self):
    question = self.getQuestion()
    print(f'Soru {self.questionIndex + 1}: {question.text}')

    for q in question.choices:
      print('-' + q)

    answer = input('Cevap: ')
    self.guess(answer)
    self.loadQuestion()

  def guess(self, answer):
    question = self.getQuestion()

    if question.checkAnswer(answer):
      self.score += 1
    self.questionIndex += 1

  def loadQuestion(self):
    if len(self.questions) == self.questionIndex:
      self.showScore()
    else:
      self.displayProgress()
      self.displayQuestion()

  def displayProgress(self):
    totalQuestion = len(self.questions)
    questionNumber = self.questionIndex + 1

    if questionNumber > totalQuestion:
      print('Quiz bitti.')
    else:
      print(f' Question {questionNumber} of {totalQuestion} '.center(100, '*'))

  def showScore(self):
    print('Score: ', self.score)

q1 = Question('En şeqil araba nedir?', ['BMW', 'Audi', 'Mercedes'], 'BMW')
q2 = Question('En şeqil soda nedir?', ['Beypazarı', 'Kızılay', 'Akmina'], 'Beypazarı')
q3 = Question('En şeqil tuvalet kağıdı nedir?', ['Papia', 'Solo', 'Teno'], 'Papia')
q4 = Question('En şeqil perde marqası nedir?', ['Brilliant', 'Taç', 'Karaca'], 'Taç')
q5 = Question('En şeqil kolonya marqası nedir?', ['Eyüp Sabri', 'Rebul', 'Karayel'], 'Rebul')

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)

quiz.loadQuestion()










