/** This program shuffles a deck of cards and then deals
    4 Bridge hands (in Bridge, each player gets 13 cards).
    We then print each hand, sort the hands (using the
    same idea as in lab 9) and print them again.

    We use the class DeckOfCards, which uses PlayingCard.
**/

public class Bridge
{
    public static void main(String[] args)
    {
	//Set up the deck and shuffle the cards.
        DeckOfCards myDeck = new DeckOfCards();
        myDeck.shuffle();

	//Set up 4 players (North, South, East, West):
        PlayingCard[] North = new PlayingCard[13];
        PlayingCard[] South = new PlayingCard[13];
        PlayingCard[] East = new PlayingCard[13];
        PlayingCard[] West = new PlayingCard[13];

	//Deal the cards from the deck to each player:
	int i;
        for (i = 0; i < 52; i++)
        {
            int who = i % 4;  //Whose to get the card
            int num = i / 4;  //The number of the card in their hand
            switch (who)
            {
                case 0: North[num] = myDeck.deck[i]; break;
                case 1: South[num] = myDeck.deck[i]; break;
                case 2: East[num] = myDeck.deck[i]; break;
                case 3: West[num] = myDeck.deck[i]; break;
            }
        }

        //Print each hand, using a method:
	System.out.println("\nNorth has: "); printCards(North);
	System.out.println("\nSouth has: "); printCards(South);
	System.out.println("\nEast has: "); printCards(East);
	System.out.println("\nWest has: "); printCards(West);

	//TO DO: Sort each hand 
        //   (Hint: Use the code from SortCards)
       

        //TO DO: Print each hand again:
        //   (Hint: Copy the code from above)

	System.out.println("\n\nEnd of Program!:");
    }

    public static void printCards(PlayingCard[] handtoPrint)
    {
        for (int i = 0 ; i < handtoPrint.length; i++)
        {
            handtoPrint[i].print();
        }
    }
}

