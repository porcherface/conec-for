// SPDX-License-Identifier: MIT

/*
 * Conec for - Game contract
 * @dev: implementation of the conec for game instance
 * @author: porcherface 
 * @version: 0.0.1
 */

pragma solidity >=0.7.0 <0.9.0;

/* Contract interface: 
 * @name: IConecGame
 * @doc: doc/game_interface.txt 
 * 
 */
abstract contract IConecGame {
	
	/* public variables */
	address public player0;
	address public player1;
	uint8   public winner;
	bool	public move;
	

	modifier isPlayer() { 
		require (msg.sender  == player1 || msg.sender == player0, "you are not a player"); 
		_;
 	}

	modifier isMover() { 
 		if (move) {
			require (msg.sender  == player1, "not your time to move"); 
			_; 
		}
		else {
			require (msg.sender  == player0, "not your time to move"); 
			_;	
		}
 	}

 	bool 	private _locked;
	modifier noReentrancy() {
		require(!_locked, "No reentrancy");
		_locked = true;
		_;
		_locked = false;
	}

	receive() virtual external payable;
	fallback() virtual external payable;
	function makeMove(uint8 column) virtual public returns (bool); //isMover
	function getBoard() virtual public view returns (uint256);     //isPlayer
	
	event gameStarted(address game_address, address player0, address player1);
	event moveLogged(address player, uint8 column, uint8 move_number);
	event gameOver(address game_address, address winner, uint256 prize);

} 
