/** This program prints out a deck of cards, then shuffles
    the deck and prints them again.

    It uses the class DeckOfCards, which uses PlayingCard.
**/

public class PrintDeck
{
    public static void main(String[] args)
    {
        DeckOfCards myDeck = new DeckOfCards();

	System.out.println("The initial deck:");
        myDeck.print();
        myDeck.shuffle();
	System.out.println("\n\nThe shuffled deck:");
        myDeck.print();
        myDeck.shuffle();
	System.out.println("\n\nThe shuffled deck:");
        myDeck.print();

	System.out.println("\n\nEnd of Program!:");
    }
}

