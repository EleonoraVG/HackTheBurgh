// Write a dummy fake-id to the NFC tag.
function writeNfc() {
  if ('nfc' in navigator) {
    navigator.nfc.watch((message) => {
        navigator.nfc.push({
          url: "/id",
          records: [{
            recordType: "text",
            data: 'fake-id-11111'
          }]
        });
      }, {
        mode: 'any'
      }).then(() =>
        console.log("Added a watch."))
      .catch(err => console.log("Adding a watch failed: " + err.name));
  } else {
    consoleLog('NFC API not supported.');
  }
}

function consoleLog(data) {
  console.log(data);
}