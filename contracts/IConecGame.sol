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
	address public player1;
	address public player2;
	bool	public move;

	function makeMove(uint8 column) public returns (bool);
	function getBoard() public returns (uint256);
	
	event gameStarted(address game_address, address player1, address player2);
	event moveLogged(address player, uint8 move_number, uint8 move);
	event gameOver(address game_address, address winner, uint256 prize);

} 
