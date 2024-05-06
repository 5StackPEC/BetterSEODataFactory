function myFunction(param1, param2) {
  // Your function logic here
  console.log(param1 + param2);
}

/**
 * Adds two numbers.
 * @param {string} xPos The first number.
 * @param {string} yPos The second number.
 */
const drawPositionLabel = (posX, posY) => {
  var div = document.createElement("div");

  // Set the content of the div (optional)
  div.textContent = `${posX}, ${posY}`;

  div.style.position = "absolute";

  // Append the div to the document body since getting the size is only possible after doing so
  document.body.appendChild(div);

  var centerX = posX - div.offsetWidth / 2;
  var centerY = posY - div.offsetHeight / 2;

  // Apply CSS styles for positioning
  div.style.left = centerX + "px"; // Adjust left position as needed
  div.style.top = centerY + "px"; // Adjust top position as needed
  div.style.backgroundColor = "rgba(255, 0, 0, 0.5)"; // Example background color
};

/**
 * Adds two numbers.
 * @param {number} x The first number.
 * @param {number} y The second number.
 * @returns {number} The sum of x and y.
 */
const drawBoundingBox = (element) => {
  element.style.border = "blue solid 2px";
};
