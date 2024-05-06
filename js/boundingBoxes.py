def paint_corner_labels(posX, posY):
    return f"""
		var div = document.createElement("div");

		// Set the content of the div (optional)
		div.textContent = '{posX}, {posY}';
        
		div.style.position = "absolute";
        
		// Append the div to the document body since getting the size is only possible after doing so
		document.body.appendChild(div);
        
        var centerX = {posX} - (div.offsetWidth / 2);
		var centerY = {posY} - (div.offsetHeight / 2);
        
		const offset_widths = [div.offsetWidth, div.offsetWidth / 2, div.offsetHeight, div.offsetHeight / 2]

		// Apply CSS styles for positioning
		div.style.left = centerX + 'px'; // Adjust left position as needed
		div.style.top = centerY + 'px'; // Adjust top position as needed
		div.style.backgroundColor = "rgba(255, 0, 0, 0.5)"; // Example background color

		"""
