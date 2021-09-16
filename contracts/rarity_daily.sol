// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

interface adventurable {
    function adventure(uint) external;
}

interface rarity_manifested is adventurable {
    function level_up(uint) external;
    function approve(address, uint256) external;
    function getApproved(uint256) external view returns (address);
}

interface rarity_cellar is adventurable {

}

interface rarity_gold {
    function claim(uint) external;
}

contract rarity_daily {

    rarity_manifested constant _rm = rarity_manifested(0xce761D788DF608BD21bdd59d6f4B54b2e27F25Bb);
    rarity_gold constant       _gold = rarity_gold(0x2069B76Afe6b734Fb65D1d099E7ec64ee9CC76B2);
    rarity_cellar constant     _cellar = rarity_cellar(0x2A0F1cB17680161cF255348dDFDeE94ea8Ca196A);


    function adventure(uint256[] calldata _ids) external {
        for (uint i = 0; i < _ids.length; i++) {
            _rm.adventure(_ids[i]);
        }
    }

    function level_up(uint256[] calldata _ids) external {
        for (uint i = 0; i < _ids.length; i++) {
            _rm.level_up(_ids[i]);
        }
    }

    // @dev Requires individual approvals...
    function cellar(uint256[] calldata _delvers, uint256[] calldata _need_approval) external {
        for (uint i = 0; i < _need_approval.length; i++) {
            _rm.approve(address(this), _need_approval[i]);
        }
        for (uint i = 0; i < _delvers.length; i++) {
            _cellar.adventure(_delvers[i]);
        }
    }

    // @dev Requires individual approvals...
    function claim_gold(uint256[] calldata _claimers, uint256[] calldata _need_approval) external {
        for (uint i = 0; i < _need_approval.length; i++) {
            _rm.approve(address(this), _need_approval[i]);
        }
        for (uint i = 0; i < _claimers.length; i++) {
            _gold.claim(_claimers[i]);
        }
    }

    // @dev Check if an array of summoners is approved
    function is_approved(uint256[] calldata _ids) external view returns (bool[] memory _is_approved) {
        _is_approved = new bool[](_ids.length);
        for (uint i = 0; i < _ids.length; i++) {
            _is_approved[i] = _rm.getApproved(_ids[i]) == address(this);
        }
    }

    // @dev Approve an array of summoners
    function approve_all(uint256[] calldata _ids) external {
        for (uint i = 0; i < _ids.length; i++) {
            _rm.approve(address(this), _ids[i]);
        }
    }

}