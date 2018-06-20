class MovieDetails:
    def movie(self):
        self.Moviename="Race3"
        self.artistname="Salman Khan"
        self.yearofrelease=2018
        self.rating=7.5
        print("Movie Name:{}\nArtist Name:{}\nYear Of Release:{}\nRating:{}\n".format(self.Moviename,self.artistname,self.yearofrelease,self.rating))

    def update(self,Moviename,artistname,Rating):
        print("After Update Values Are:\n")
        self.Moviename=Moviename
        self.artistname=artistname
        self.rating=Rating
        print("Movie Name:{}\nArtist Name:{}\nYear Of Release:{}\nRating:{}".format(self.Moviename,self.artistname,self.yearofrelease,self.rating))
        
        
m=MovieDetails()
m.movie()
m.update("Sanju","Ranbir Kapoor",9.0)
