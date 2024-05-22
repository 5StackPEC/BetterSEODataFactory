/**
 * @param {HTMLElement} element
 * @param {string} color
 */
paintBorder = function (element, color = "blue") {
  element.style.border = color + " 2px solid";
};

/**
 * @param {HTMLElement} element
 * @param {string} borderColor
 * @param {string} backgroundColor
 */
paintBorderAsNewDiv = function (
  element,
  borderColor = "tomato",
  backgroundColor = "rgba(255, 0, 0, 0.1)"
) {
  var rect = element.getBoundingClientRect();

  var div = document.createElement("div");
  div.style.position = "absolute";
  div.style.top = rect.top + "px";
  div.style.left = rect.left + "px";
  div.style.width = rect.width + "px";
  div.style.height = rect.height + "px";

  document.body.appendChild(div);
  console.log(backgroundColor);
  div.style.border = borderColor + " 2px solid";
  div.style.backgroundColor = backgroundColor;
};

/**
 * @param {number} posX
 * @param {number} posY
 * @param {string} color
 */
paintCornerLabels = function (posX, posY, color) {
  var div = document.createElement("div");

  // Set the content of the div (optional)
  div.textContent = `${posX}, ${posY}`;

  div.style.position = "absolute";

  // Append the div to the document body since getting the size is only possible after doing so
  document.body.appendChild(div);

  var centerX = posX - div.offsetWidth / 2;
  var centerY = posY - div.offsetHeight / 2;

  // Apply CSS styles for positioning
  div.style.left = centerX + "px";
  div.style.top = centerY + "px";
  div.style.backgroundColor = color;
};
