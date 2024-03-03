#class vinyl
class Vinyl:
   def __init__(self, album, artist, year):
       self.__album = album
       self.__artist = artist
       self.__year = year

   def upgrade(self):
       return 0

   def display(self):
       print (self.__album + ' , ' + self.__artist + ' , ' + str(self.__year))

def run():
   hollywoods_bleeding = Vinyl('Hollywoods Bleeding','Post Malone','2019')
   midnights = Vinyl('Midnights','Taylor Swift','2023')
   the_game = Vinyl('The Game','Queen','1980')
   apricot_princess = Vinyl('Apricot Princess', 'Rex Orange County', '2017')

   hollywoods_bleeding.display()
   midnights.display()
   the_game.display()
   apricot_princess.display()
