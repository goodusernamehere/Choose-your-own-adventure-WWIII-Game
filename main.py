import random
import time as t

#a is for if you need a for i in x type thing
a = str(12343274823748723984728141324831789147893748173715849838437857318507089734897582371480732198407328914739821470328174123084071843274180740124780312741047213847019740382478274827384732758923748972938478927438274927581784787481748374729834729874982397427942479782374892749274923847)
#death screen deathcause is a string and it will be like this let's just say deathcause = abc it would be abc. and then the link to rick astley
def wrong(deathcause) :
  print('WRONG!')
  
  for i in a:
    #rickroll
    print(deathcause + ' https://www.youtube.com/watch?v=dQw4w9WgXcQ')

#the game
def adventure():
  #origin of the storyline
  print('You walk in a cobblestone path in the now devasted Spain after WWIII')
  #table of nationales
  countryNationalies = ['french', 'german', 'nordic', 'american', 'mexican', 'russian', 'chinese', 'japanese', 'vietnamese', 'indian', 'pakistani', 'spanish', 'italian', 'polish', 'portuguese', 'brazilian']
  #
  yourNationaly = random.choice(countryNationalies)
  t.sleep(1)
  print('\nYou are ' + yourNationaly + '.')
  t.sleep(1)
  first = input('\nLeft or Right(l/r)')
  if (first == 'l'):
    for i in a:
      wrong('You were stabbed by a man in the alley.')
  elif (first == 'r'):
    t.sleep(1)
    print('\nYou move on and find a store')
    t.sleep(0.5)
    print('The man there is very friendly')
    t.sleep(1)
    print('The man: Hello, my name is Alejandro. When are you looking for?')
    t.sleep(1)
    print('You: Can you help me?')
    t.sleep(1)
    name = input('Alejandro: Sure, what\'s your name? ')
    randomNationaly = random.choice(countryNationalies)
    t.sleep(0.5)
    print('Alejandro: ' + name + '? ' + 'It sounds ' + randomNationaly + '.' ' I\'ll have to get used to it.')
    t.sleep(1)
    print('You: Really? How? Eh, whatever.')
    #The class for any person
    class Person:
          def __init__ (person, money, age, integrity):
            person.money = money
            person.age = age
            person.integrity = integrity
    t.sleep(1)
    # age
    e1 = int(input('David: I need to ask one more question. What is your age? '))
    #the person doing the adventure
    p1 = Person(100, e1, 0.32)
    #get the street cred / integrity into a percentage
    def getP1IntegrityPercentage():
      p1IntegrityPercentage = p1.integrity * 100
      p1IntegrityPercentage = str(p1IntegrityPercentage)
      p1IntegrityPercentage += '%'
      print(p1IntegrityPercentage)
    t.sleep(3)
    #asking if you're confidenet in your luck
    print('David: Also a tip for the street, if you have less than 0.25 or 25% integrity, the more likely you are to die and be denied/attacked. Right now you have ' + str(p1.integrity))
    b = input('David: Do you have good luck? (y/n): ')
    if(b == 'y'):
      countryArray = ['Afghanistan', 'Iraq', 'France', 'Somalia', 'China']
      #You only have a 20% chance of something good and c determintes whoich country
      c = random.choice(countryArray)
      if (c == 'Afghanistan'):
        t.sleep(1)
        print('David: We ended up here huh...')
        t.sleep(1)
        print('You: Why did I think I was lucky...')
        t.sleep(1)
        print('David: Are you an American citizen?')
        t.sleep(1)
        # if you are an american citizen you'll be saved
        if(yourNationaly == 'american'):
          print('You: Yep.')
          t.sleep(1)
          print('David: Great! See if there\'s any Americans near by.')
          t.sleep(1)
          print('You find an American and they bring you to America.')
          t.sleep(0.25)
          s = "Going to America"
          for i in range(5):
            t.sleep(1)
            s += str('.')
            print(s)

        else:
          print('David: Well, then...')
          wrong('You ask an American soldier for help, he laughs at you and shoots you. He was arrested soon after')
      elif (c == 'Iraq'):
        print('You ended up in Iraq.')
        t.sleep(1)
        wrong('You died under Suspicions circumstances. The investagation is still going on.')
      #only country you live in (if you go in afghanistan and you're lucky enough to be american you can go to america)
      elif (c == 'France'):
        #picks what city in france it'll be
        frenchCity = random.choice(['Paris, Nice'])
        if(frenchCity == 'Paris'):
          print('You: So, um... David, how are we gonna get money? We\'re in Paris.')
      elif (c == 'Somalia'):
        wrong('You have terrible luck, you ended up in SOMALIA, never EVER trust in YOUR LUCK EVER')
      elif (c == 'China'):
        wrong('You insulted the Chinese government years ago!')
    #ifyou decide you have bad luck then you can stay in spain
    elif(b == 'n'):
  
      print('David: You\'ll stay here I guess.') 
      # y = store, n = explore
      d = input('David: So do you want something from the store or explore? (y/n): ')
      t.sleep(1)
      print('David: (PS: If you don\'t by food you\'ll die from hunger, oh and one more think if you forgot this is war. Stock up on extra food when possible and be careful wherever you go)')
      # if you want to go the store
      if (d == 'y'):
        #items from the spanish store
        class spainStoreItems:
          def __init__(spainStoreItem, money, item, id):
            spainStoreItem.money = money
            spainStoreItem.item = item
            spainStoreItem.id = id
        # the objects for the items in the storm
        foodAndWater = spainStoreItems(50, 'food', 1)
        flashlight = spainStoreItems(3, 'flashlight', 2)
        console = spainStoreItems(99, 'console', 3)
        phone = spainStoreItems(150, 'phone', 4)
        laptop = spainStoreItems(400, 'laptop', 5)
        gps = spainStoreItems(34, 'gps', 6)
        map = spainStoreItems(12, 'map', 7)
        #loading
        s2 = 'Going to the store'
        for i in 5:
          t.sleep(1.5)
          s2 += '.'
          print(s2)
        #first trip if you stayed in spain to the store  
        f = input('What do you want, (you can only buy one think from the store at once) you have $' + str(p1.money) + ' dollars, say the number for the item: \n(1) Food and Water, $50 \n(2) Flashlight, $3 \n(3) (Video game) Console, $99 \n(4) Phone, $150 \n(5) Laptop, $400 \n(6) GPS, $34 \n(7) Map, $12: ')
        #if you bought food and water
        if (f == '1'):
          t.sleep(1)
          print('You bought some food, good choice. You live another day.')
          p1.money = p1.money - 50
          t.sleep(1)
          print ('You have $ ' + str(p1.money) + ' now.')
        if (f == '2'):
          #if they don't buy food and water then you die
          t.sleep(1)
          g = input('You bought a flashlight. Do you want to buy food also? (y/n): ')
          if (g == y): 
            t.sleep(1)
            print('You live another day')
            t.sleep(1)
            #lose integrity because you didn't buy 
            p1.integrity - 0.04
            print('But you also lose 4% integrity, come on. Shoulda picked food. (You have 28% integrity or 0.28 (you\'re walking on thin ice')
          if (g == n):
            t.sleep(1)
            s3 = ''
            for i in 10:
              t.sleep(1)
              s3 += '.'
              print(s3)
            print('You moron, you are going to starve to death. WHY WOULD YOU BUY A FLASHLIGHT')
            print('Either you starve to death or you find someone and kill/steal from them, David will split with you if he knows so keep it a secret. You ')
            



      
adventure()