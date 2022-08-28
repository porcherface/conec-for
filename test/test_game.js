const ConecGame = artifacts.require("ConecGame");
const truffleAssert = require('truffle-assertions');

contract("ConecGame", 	function ( accounts ) {
  	

  	beforeEach(async function () {
    	game = await ConecGame.deployed();
      	
  	});
  	
  	describe('Construction', function ( ) {

  		it("should assert true", async function () {
    		return assert.isTrue(true);
  		}
		);

  		it("should return player addresses", async function ( ) {
    		
  			const player0 = await game.player0();
			const player1 = await game.player1();
			assert.equal(player0, accounts[0]);
			assert.equal(player1, accounts[1]);
    		return;
  		}
		);

  		it("should set move as false", async function ( ) {
    		const move = await game.move();
  			assert.isFalse(move);
    		return;
  		}
		);

  		it("should return empty board", async function ( ) {
  			const board = await game.getBoard();
  			assert.equal(board, 0);
    		return;
  		}
		);

  		it("should set winner as 0x0", async function ( ) {
    		
  			const winner = await game.winner();
  			assert.equal(winner, 0);
    		return;
  		}
		);

  			
	}
	);

  	describe('Session', function ( ) {
  		it("should let player0 play a move (col0)", async function ( ) {
    		const move = await game.makeMove(0);
    		return;
  		}
		);

		it("should update the board", async function ( ) {
    		const board = await game.getBoard();
    		assert.equal(board, 1);
  		}
		);  			
		
		it("should set move to true ", async function ( ) {
    		const move = await game.move();
  			assert.isTrue(move);
  			return;  		
  		}
		);  			
	  	
	  	it("should let player1 play a move (col1)", async function ( ) {
    		const res = await game.makeMove(1, {from:accounts[1]});
    		return;
  		}
		);
	
		it("should update the board", async function ( ) {
    		const board = await game.getBoard();
    		assert.equal(board, 8+1);
  		}
		);  			
		
		it("should set move to false again ", async function ( ) {
    		const move = await game.move();
  			assert.isFalse(move);
  			return;  		
  		}
		);  			
	  	it("should move set to true again (col0)", async function ( ) {
    		const res = await game.makeMove(0, {from:accounts[0]});
       		const board = await game.getBoard();
       		const move = await game.move();

  			assert.isTrue(move);
  			return;  		
  		}
		);  	
	}
	);

  	describe('Reverts', function () {

		it("should assert false", async function () {	
			return assert.isFalse(false);
		}
		);
		
		it("should block a non-player", async function () {	
			const malicious = accounts[2];
			await truffleAssert.reverts(game.makeMove(0,{ from: malicious}),"you are not a player");
			return;
		}
		);
  	  	
		it("should block the non-mover (player1 moves)", async function () {	
			const wrong = accounts[0];    
			await truffleAssert.reverts(game.makeMove(0,{ from: wrong}),"not your time to move");
			return;
		}
		);


		it("should block an out of range move", async function () {	
			const player = accounts[1];    
			await truffleAssert.reverts(game.makeMove(10, {from:player}),"column out of range");
			return;
		}
		);
  	}
	);
	
	
	
});
