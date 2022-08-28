var ConecGame = artifacts.require("ConecGame");

module.exports = function(deployer, network, accounts) {

	console.log("deploying a conec for with players: ");
	console.log(accounts[0]);
	console.log(accounts[1]);

	deployer.deploy(ConecGame, accounts[0], accounts[1]);
	console.log("Done.")
};	