/** This program reads in 5 playing cards from the user, sorts
    them by rank, and prints out the sorted hand.

    It uses the class PlayingCard, which assumes that ranks are
    entered 2,3,4,5,6,7,8,9,10,11,12,13,14 where the face cards
    are represented by 11 for Jack, 12 for Queen, 13 for King, 
    and 14 for Ace.
**/

public class SortCards
{
    public static void main(String[] args)
    {
	int i, j;	//Indices for the arrays 
        PlayingCard[] hand = new PlayingCard[5];
			// the 5 playing cards in our hand

	System.out.println("Welcome to the sorting demonstration.\n");

	//Read in the cards:
        for (i = 0; i < 5; i++ )
        {
	    hand[i] = new PlayingCard();
	    hand[i].read();
        }

	//Print out the cards, in the order entered:
	System.out.println("\nYou entered:");
        for (i = 0; i < 5; i++ )
        {
	    hand[i].print();
        }

	//Sort the cards by rank:
        for (i = 0; i < 5; i++ )
        {
	    for (j = 0 ; j < 4 ; j++)
            {
                if ( hand[j].rank > hand[j+1].rank )
                {
                    //Swap cards if jth one is bigger
                    PlayingCard tmp = hand[j];
                    hand[j] = hand[j+1];
                    hand[j+1] = tmp;
                }
            }
        }

	//Print out the cards, sorted:
	System.out.println("Sorted:");
        for (i = 0; i < 5; i++ )
        {
	    hand[i].print();
        }

    }
}

