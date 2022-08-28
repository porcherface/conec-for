const Caos = artifacts.require("Caos");
const caos_instance = await Caos.deployed();




contract("ConecGame", 	function ( accounts ) {


  	describe('Basic Functions', function () {

  		it("should deploy and assert true", async function () {
    		

    		return assert.isTrue(true);
  		}
		);
  


	}
	);

  	describe('Reverts', function () {

		it("should assert false", async function () {	
			//await truffleAssert.reverts(/* FAILED CALL*/ );
			return assert.isFalse(false);
		}
		);
  	}
	);
	
	
	
});
