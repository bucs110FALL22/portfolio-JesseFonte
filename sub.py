article = ("Playing video games, including violent shooter games, may boost children’s learning, health and social skills.Playing video games, including violent shooter games, may boost children's learning, health and social skills, according to a review of research in American Psychologist. The study comes out as debate continues among psychologists and other health professionals regarding the effects of violent media on youth. An APA task force is conducting a comprehensive review of research on violence in video games and interactive media and will release its findings later this year")

subs = {
  "Playing":"Listening",
  "violent":"Beautiful",
  "psychologists":"President",
  "findings" : "huggings",
  }

for key, value in subs.items():
  article = article.replace(key, value)
 
print(article)