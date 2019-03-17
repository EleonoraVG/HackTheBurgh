// Read from an NFC tag and print to console.
function readNfc() {
  if ('nfc' in navigator) {
    navigator.nfc.watch(function(message) {
        consoleLog("NFC message received from URL " + message.url);
        if (message.records[0].recordType == 'empty') {
          console.log("Tag is empty.");
        }
        processMessage(message);
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
