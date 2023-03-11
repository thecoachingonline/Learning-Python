print("Hello Learning")

# Variables
wallet = 41
print(wallet)

wallet = 32
print(wallet)

#Numbers: Ints and floats
day = 21
temp = -15
weight = 190.435623

print(day + 3)
print(weight - 2)
print(day * temp)

#Srings
age = 32
shirt = 'blue'
store = 'Nink\'s Pizza Shop, '

print(store + age + shirt)

#Using variables in strings
day = 21
month = 'October'
temp = 65
day_name = 'Tuesday'

print(f"Today is {day_name} {month} {day} and it's {temp} degrees outside")

#Booleans and if statements
light_is_on = False

if light_is_on:
    print("The light is on!")

print("Hello")

#Comparison and else

light_is_on = True

if light_is_on:
    print("The light is on!")
else:
    print("We're in the dark")

weight = 190.4

if weight != 195:
    print("You're under weight :)")

age = 17

if age >= 18:
    print("Adult")
else:
    print("Child")

#Picking random numbers
import random

print(random.randint(1,10))

print(random.random())

answer = random.randint(1,3)

if answer == 1:
    print("Yes")
if answer == 2:
    print("No")
if answer == 3:
    print("Maybe")

#Choosing what fortune to show
import random

lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)
fortune_text = ''

if fortune_number == 1:
    fortune_text = 'You will have a great day!'
if fortune_number == 2:
    fortune_text = 'Today will be tough...but worth it.'
if fortune_number == 3:
    fortune_text = 'You will get married this year!'

print(f'{fortune_text} Your Lucky Number is: {lucky_number}')

#Lists
fav_movies = ["Sandlot", "The Lego Move", "Dune"]

print(fav_movies[2])

fav_numbers = [4,9,33]

print(fav_numbers[0])

#Add, insert, delete
print(len(fav_movies))

fav_movies.append("Iron Man")
print(fav_movies)

fav_movies.insert(1,"Batman")
print(fav_movies)

del(fav_movies[2])
print(fav_movies)

#For loops
for number in range(10):
    print(number)
    print("Hello")

for movie in fav_movies:
    print(movie * 2)

#Dictionaries
cate = {"Jane":6, "Tom":14, "Sara":8}
 print(cate["Tom"])

#Splitting a string
text = """
#ธัม์มปทํ   #Dhammapada   #ธัมมบท

สัพ์พปาปัส์ส อกรณํ, 
กุสลัส์ส อุปสัม์ปทา; 
สจิต์ตปริโยทปนํ, 
เอตํ พุท์ธาน สาสนํ.

ปาฬิภาสา-อักษรสยาม  #ธัม์มปทํ183

ไม่ทำชั่วทั้งปวง,
ทำแต่ความดี;
ทำจิตใจให้ผ่องใส,
นี่คือคำสอนของพระพุทธเจ้าทั้งหลาย.

ภาษาไทย  #ธัมมบท183

To avoid all evil,
to cultivate good,
and to cleanse one’s mind—
this is the teaching of the Buddhas.

ภาษาอังกฤษ #Dhammapadaverse183

sabbapāpassa akaraṇaṁ,
kusalassa upasampadā;
sacittapariyodapanaṁ,
etaṁ buddhāna sāsanaṁ.

ปาฬิภาสา-อักษรโรมัน #Dhammapada183

ดู​ พระไตรปิฎก จปร. #ฉบับอนุรักษ์ดิจิทัล

#Mahāsaṅgīti Tipiṭaka B. E. 2500
in Roman-Script Transliteration
by the #WorldTipiṭaka 
since 2005

“สรุปเรื่องสำคัญ เนื่องในวันมาฆบูชา”

"#มาฆบูชา" ย่อมาจาก "#มาฆปูรณมีบูชา" หมายถึงการบูชาวันเพ็ญกลางเดือนมาฆะ ตามปฏิทินของอินเดีย หรือเดือน ๓ ตามปฏิทินจันทรคติของไทย ซึ่งมักจะตรงกับเดือนกุมภาพันธ์หรือเดือนมีนาคม วันมาฆบูชาเป็นเสมือนวันประชุมกันเป็นพิเศษแห่งพระอรหันตสาวก โดยมิได้มีการนัดหมายล่วงหน้าซึ่งได้มีขึ้น ณ บริเวณเวฬุวันวรมหาวิหาร กรุงราชคฤห์ แคว้นมคธ หลังจากที่พระพุทธเจ้าได้ตรัสรู้เป็นเวลานับได้ ๙ เดือน วันนี้มีชื่อเรียกอีกชื่อหนึ่งว่า “วันจาตุรงคสันติบาต” (มาจากศัพท์บาลี #ปาฬิ คือ จตุ+องค+สนนิปาต แปลว่า การประชุมอันประกอบด้วยองค์ประกอบทั้งสี่ประการ) เนื่องจากมีเหตุการณ์เกิดขึ้นอย่างประจวบเหมาะ ๔ ประการ คือ

 ๑. วันที่พระสงฆ์ทั้งหมดมาชุมนุมกันนี้ ตรงกับวันเพ็ญเดือนมาฆะ (วันขึ้น ๑๕ ค่ำ เดือน ๓)

๒. พระภิกษุ ๑,๒๕๐ รูป มาชุมนุมกันโดยมิได้นัดหมาย

๓. พระภิกษุ เหล่านั้นทั้งหมด ได้รับการอุปสมบทจากพระพุทธเจ้าโดยตรง (เอหิภิกขุอุปสมปทา)

๔. พระภิกษุทั้งหมดล้วนเป็นพระอรหันต์ ประเภทฉฬภิญญา คือ ได้อภิญญา ๖ พระพุทธเจ้าจึงทรงแสดงโอวาทปาฏิโมกข์ เป็นพระพุทธพจน์ ๓ คาถา ซึ่งถือได้ว่า เป็นหัวใจของพระศาสนา มีใจความดังนี้

พระพุทธพจน์คาถาแรก ทรงกล่าวถึง พระนิพพาน ว่าเป็นจุดมุ่งหมายหรืออุดมการณ์อันสูงสุดของบรรพชิตและพุทธบริษัท อันมีลักษณะที่แตกต่างจากศาสนาอื่น ดัง พระบาลีว่า

"นิพพานัง ปรม วทนติ พุทธา"

แปลว่า พระพุทธเจ้าทั้งหลายกล่าวว่า พระนิพพานเป็นบรมธรรม 

พระพุทธพจน์คาถาที่สองทรงกล่าวถึง "วิธีการอันเป็นหัวใจสำคัญเพื่อเข้าถึงจุดมุ่งหมายของพระพุทธศาสนาแก่พุทธบริษัททั้งปวง โดยย่อดังพระบาลีว่า

 "สัพพะปาปัสสะ   อะกะระณัง
  sabbapāpassa akaraṇaṁ,

  กุสะลัสสะ  อุปะสัมปะทา
  kusalassa upasampadā;

  สจิตตะปริโยทะปะนังํ
  sacittapariyodapanaṁ

  เอตังํ  พุทธานะสาสะนังํ"
  etaṁ buddhānasāsanaṁ.

คือ การไม่ทำชั่วทั้งปวง การบำเพ็ญแต่ความดี และการทำจิตของตนให้ผ่องใสเป็นอิสระจากกิเลสทั้งปวง ส่วนนี้เองของโอวาทปาฏิโมกข์ที่พุทธศาสนิกชนมักท่องจำกันไปปฏิบัติ ซึ่งเป็นเพียงคาถาในสามคาถากึ่งของ #โอวาทปาติโมกข์ เท่านั้น
"""

print(len(text.split()))

#Counting the words
word_count = {}

for word in text.lower().split():
    if word in word_count:
       word_count[word] += 1
    else:
       word_count[word] = 1

print(word_count)

#Functions
def bark():
    print("Woof woof!")
    print("I'm a dog!")

for x in range(100):
    bark()

#Parameters
def hello(name):
    print("Hello {name}!")

hello("John")

def add_numbers(num1,num2):
    print(num1 + num2)

add_numbers(4,8)
add_numbers(3,7)

#Return
def double(number):
    return number * 2

new_number = double(5)
print(new_number)

def uppercase(text):
    return text.upper()

print(uppercase("Nick"))

names = ['nick', 'Jane', 'sara']

for name in names:
    print(uppercase(names))