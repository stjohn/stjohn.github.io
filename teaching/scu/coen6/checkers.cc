/*
 * Checkers program
 */

#include <iostream>

class Checkers
{
	public:
		Checkers();	// Default constructor
			// sets the board to the beginning checkers 
			// configutation
		int move(char player, int old_x, int old_y,
				  int new_x, int new_y);
			// moves player's piece from (old_x, old_y)
			// to (new_x, new_y)
		friend ostream& operator <<(ostream& outs, Checkers game);
			// Prints game board with coodinates
	
	private:
		char board[8][8];
			// Stores the board as an 8 x 8, 2 dimensional array
			// with the x coodinate first, then the y coordinate
};

main()
{
	char answer;
	Checkers game;
	int old_x, old_y, new_x, new_y;
	
	cout << "Welcome to checkers!\n";
	cout << "There are two players, black and red\n\n";
	cout << "Would you like to play a game? ";
	cin >> answer;
	
	while ( answer == 'y' )
	{
		do {
			cout << game;
			cout << "Black's move:\n";
			cout << "What is the x-coordinate for the piece: ";
			cin >> old_x;
			cout << "What is the y-coordinate for the piece: ";
			cin >> old_y;
			cout << "What is the x-coordinate for the new position: ";
			cin >> new_x;
			cout << "What is the y-coordinate for the new position: ";
			cin >> new_y;
		}
		while (!game.move('b', old_x, old_y, new_x, new_y));
		
		do {
			cout << game;
			cout << "Red's move:\n";
			cout << "What is the x-coordinate for the piece: ";
			cin >> old_x;
			cout << "What is the y-coordinate for the piece: ";
			cin >> old_y;
			cout << "What is the x-coordinate for the new position: ";
			cin >> new_x;
			cout << "What is the y-coordinate for the new position: ";
			cin >> new_y;
		}
		while ( !game.move('r', old_x, old_y, new_x, new_y));

		cout << game;
		cout << "Would you like to keep playing? ";
		cin >> answer;
	}
	
	cout << "Thank you for playing!\n Bye!\n";
	
}


Checkers::Checkers()	
// Default constructor
// sets the board to the beginning checkers 
// configutation
{
	int i, j;
	
	// set everything to blanks first:
	for ( j=0; j < 8 ; j++ )
		for ( i=0 ; i<8 ; i++ )
			board[i][j] = ' ';
			
	// put in black's pieces:
	for ( j=0; j < 3 ; j++ )
		for ( i=0 ; i<8 ; i++ )
			if ( (i+j)%2 == 0 )
				board[i][j] = 'b';
			
	// put in red's pieces:
	for ( j=5; j < 8 ; j++ )
		for ( i=0 ; i<8 ; i++ )
			if ( (i+j)%2 == 0 )
				board[i][j] = 'r';
	
}
int Checkers::move(char player, int old_x, int old_y, 
	int new_x, int new_y)
// moves player's piece from (old_x, old_y)
// to (new_x, new_y)
{
	// simple move, no checking:
	board[old_x-1][old_y-1] = ' ';
	board[new_x-1][new_y-1] = player;

	return(1);
}

ostream& operator <<(ostream& outs, Checkers game)
// Prints game board with coodinates
{
	int i, j;
	
	outs << endl;
	outs << "  ";
	for ( i=0; i < 8 ; i++)
		outs << "   " << i+1;
		
	outs << endl << "   ";
	
	for ( i=0; i < 8 ; i++)
		outs << "----";
		
	outs << endl;	
	
	for ( j=0; j < 8 ; j++ )
	{
		outs << " " << j+1 << " | ";
		for ( i=0 ; i<8 ; i++ )
		{
			outs << game.board[i][j] << " | ";
		}
		outs << endl << "   ";	
		for ( i=0; i < 8 ; i++)
			outs << "----";
		outs << "-" << endl;
	}
	
	outs << endl;
	return(outs);
}	
