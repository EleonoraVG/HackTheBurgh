// Read from an NFC tag and print to console.
function readNfc() {
	if ('nfc' in navigator) {
		navigator.nfc.watch(function(message) {
				consoleLog("NFC message received from URL " + message.url);
				if (message.records[0].recordType == 'empty') {
					console.log("Tag is esic information mpty.");
				} else {
					var form = document.createElement("form");
					form.setAttribute("method", "post");
					form.setAttribute("url", "/");

					var hiddenField = document.createElement("input");
					hiddenField.setAttribute("type", "hidden");
					hiddenField.setAttribute("name", "uid");
					hiddenField.setAttribute("value", message.records[0].data);

					form.appendChild(hiddenField);
					document.body.appendChild(form);
					form.submit();
				}
			}, {
				mode: 'any'
			})
			.then(() => consoleLog("Added a watch."))
			.catch(err => consoleLog("Adding watch failed: " + err.name));
	} else {
		consoleLog('NFC API not supported.');
	}
}

function consoleLog(data) {
	console.log(data);
}

function testPost() {
	var form = document.createElement("form");
	form.setAttribute("method", "post");
	form.setAttribute("url", "/");

	var hiddenField = document.createElement("input");
	hiddenField.setAttribute("type", "hidden");
	hiddenField.setAttribute("name", "uid");
	hiddenField.setAttribute("value", "5c8d398b39c16384ceb37c78");

	form.appendChild(hiddenField);
	document.body.appendChild(form);
	form.submit();
}
