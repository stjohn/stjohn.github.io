/** To be used for Homework 9.

    This class stores 52 PlayingCards, prints the deck,
    prints the ith card, and shuffles the deck.
**/

public class DeckOfCards
{
    public PlayingCard[] deck = new PlayingCard[52];    
			//the deck of the cards

    /** The default constructor allocates space for each
        card, and then initializes the cards, using 
        for-loops. 
    **/
    public DeckOfCards()
    {
        int i;

        //Allocate space:
        for ( i = 0 ; i < 52 ; i++)
        {
            deck[i] = new PlayingCard();
        }
        
        //Set each suit (first clubs, then diamonds, hearts, 
        // and spades
        for ( i = 0 ; i < 52 ; i++ )
        {
            int div = i / 13; //Divide into groups of 4 (52/4 = 13)
            switch (div)
            {
                case 0: deck[i].suit = "clubs"; break;
                case 1: deck[i].suit = "diamonds"; break;
                case 2: deck[i].suit = "hearts"; break;
                case 3: deck[i].suit = "spades"; break;
            }       
        }

        //Set the ranks for each card:
        for ( i = 0 ; i < 52 ; i++ )
        {
            deck[i].rank = i % 13 + 2; //Divide into groups of
		//4, since there's 4 cards of each rank 
        }
    }

    /** Prints out all 52 cards: **/
    public void print()
    {
        int i;
        for ( i = 0 ; i < 52 ; i++ )
        {
            deck[i].print();
	    //Print 5 cards per line:
            if (  (i+1)%5 == 0 )
                System.out.println();
        }
    }

    /** Prints out the ith card: **/
    public void print(int indexToPrint)
    {
        
        deck[indexToPrint].print();
    }

    /** Shuffles the deck: **/
    public void shuffle()
    {
        int i;

	//Swap 2 random cards, 1000 times
        //  Should be enough times to shuffle
        for ( i = 0 ; i < 1000 ; i++ )
        {
            int c1, c2;
	    //Generate random numbers using functions 
            //  the Math class:
            c1 = (int) Math.round(Math.random()*52)%52;
            c2 = (int) Math.round(Math.random()*52)%52;

            //Swap the 2 cards:
            PlayingCard tmp = deck[c1];
            deck[c1] = deck[c2];
            deck[c2] = tmp;
        }
    }
}

