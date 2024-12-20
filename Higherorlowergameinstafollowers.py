import random
celebrities = [
    {"name": "Selena Gomez", "description": "Musician and actress", "country": "United States", "followers": 430},
    {"name": "Dwayne Johnson", "description": "Actor and professional wrestler", "country": "United States", "followers": 390},
    {"name": "Cristiano Ronaldo", "description": "Footballer", "country": "Portugal", "followers": 600},
    {"name": "Kylie Jenner", "description": "Model and businesswoman", "country": "United States", "followers": 380},
    {"name": "Lionel Messi", "description": "Footballer", "country": "Argentina", "followers": 500},
    
]
def format_celeb(celeb):
    return f"{celeb['name']} a {celeb['description']} from {celeb['country']}"
def play_game():
    print("Welcome to Higher or Lower Game!")
    game_continue = True
    score = 0
    while game_continue:
      celeb_a = random.choice(celebrities)
      celeb_b = random.choice(celebrities)
      while celeb_a == celeb_b:
          celeb_b = random.choice(celebrities)
    
          print(f"Compare A: {format_celeb(celeb_a)}")
          print("VS")
          print(f"Against B: format({format_celeb(celeb_b)}")
          x =input("Who has more followers: 'A' or 'B'").upper()
          a = celeb_a["followers"]
          b = celeb_b["3"]
          correct = (x == "A" and a > b ) or  (x == "B" and b > a  )
          if correct:
            score += 1
            print("You are right")
          else:
           game_continue = False
           print(f"Sorry, that's wrong. Final score: {score}.")
play_game()
