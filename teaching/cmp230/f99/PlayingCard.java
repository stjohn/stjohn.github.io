/** To be used the week of 15 November in lecture and lab.

    This class stores playing cards from a standard deck
    of 52 cards.  

    The rank of the card is entered as an integer: 
	2,3,4,5,6,7,8,9,10,11,12,13,14 
    where the face cards are represented by 11 for Jack, 
    12 for Queen, 13 for King, and 14 for Ace.  The rank 
    is printed as
        2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace.  

    The possible suits are: Clubs, Diamonds, Hearts, and 
    Spades.
   
    This class has a print() and read() function.  We
    will add more to it later.
**/

import SavitchIn.*;

public class PlayingCard
{
    public int rank;    //the rank of the card
    public String suit; //the suit of the card

    public void read()
    {
        do {
	    System.out.println("Please enter the rank (2-14):");
            rank = SavitchIn.readLineInt();
        } while ( rank < 2 || rank > 14 );

        do {
	    System.out.println("Please enter the suit "
                  + "(clubs, diamonds, hearts, spades):");
            suit = SavitchIn.readLine().toLowerCase();
        } while ( !suit.equals("clubs") && !suit.equals("diamonds") &&
                  !suit.equals("hearts") && !suit.equals("spades") );
    }
    public void print()
    {
        if ( rank < 11 )
            System.out.print(rank + " ");
        else //it's a face card:
        {
            switch (rank)
            {
                case 11: System.out.print("Jack "); break;
                case 12: System.out.print("Queen "); break;
                case 13: System.out.print("King "); break;
                case 14: System.out.print("Ace "); break;
            }
        }
        
        System.out.print(suit+" ");
    }
}

