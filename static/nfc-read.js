// Read from an NFC tag and print to console.
function readNfc() {
  if ('nfc' in navigator) {
    navigator.nfc.watch(function(message) {
        consoleLog("NFC message received from URL " + message.url);
        if (message.records[0].recordType == 'empty') {
          console.log("Tag is empty.");
        }
        else {
          const http_req = new XMLHttpRequest();
          const url="/";
          var data = {uid: message.records[0].data}
          http_req.open("POST", url, true);
					http_req.setRequestHeader("Content-type","application/x-www-form-urlencoded");
					http_req.onreadystatechange = function () {
							 if (http_req.readyState == 4 && http_req.status == 200) {
									 // do something with response
									 console.log(http_req.responseText);
							 }
					};
					http_req.send(data);
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
