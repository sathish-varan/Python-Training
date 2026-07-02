from abc import ABC , abstractmethod
class TVshows(ABC):
  @abstractmethod
  def show(self):
    pass
    
class Cartoon(TVshows): 
  def show(self):
    print('Fav. Cartoon is Playing')
class Music(TVshows):
  def show(self):
    print('Fav. Music is Playing')
class Movies(TVshows):
  def show(self):
    print('Fav. Movie is Playing')
    
def tvshow(watch : TVshows):
  watch.show()

entertain = tvshow(Cartoon()) 
entertain = tvshow(Movies()) 
