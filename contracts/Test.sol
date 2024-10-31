// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Test {
    string private content;

    function readContent() external view returns (string memory) {
        return content;
    }

    function writeContent(string memory _content) external {
        content = _content;
    }
}
