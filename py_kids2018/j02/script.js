var block = document.getElementById("my_block");
var block_2 = document.getElementById("my_block_2");
var all_my_classes = document.getElementsByClassName("usual");

function changeColor() {
	block.style.color = "red";
	block_2.style.color = "blue";
}

function makeKingSize() {
	all_my_classes[0].className += " new";
}