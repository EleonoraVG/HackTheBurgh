// Read from an NFC tag and print to console.
function readNfc() {
  if ('nfc' in navigator) {
    navigator.nfc.watch(function(message) {
        consoleLog("NFC message received from URL " + message.url);
        if ( message.data == null || message.data[0].recordType === 'empty') {
          navigator.nfc.push([{
            url: "/",
            data: [{
              recordType: "text",
              data: 'Empty tag'
            }]
          }]);
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

// Write a dummy fake-id to the NFC tag.
function writeNfc() {
  if ('nfc' in navigator) {
    navigator.nfc.watch((message) => {
        navigator.nfc.push("fake-id");
      }, { mode: 'any'}).then(() => 
        console.log("Added a watch."))
        .catch(err => console.log("Adding a watch failed: " + err.name));
  } else {
    consoleLog('NFC API not supported.');
  }
}

function consoleLog(data) {
  var logElement = document.getElementById('log');
  logElement.innerHTML += '\n' + data;
}

function processMessage(message) {
  message.data.forEach(function(record) {
    if (record.recordType == "string") {
      consoleLog('Data is string: ' + record.data);
    } else if (record.recordType == "json") {
      processJSON(record.data);
    } else if (record.recordType == "url") {
      consoleLog("Data is URL: " + record.data);
    } else if (record.recordType == "opaque" && record.mediaType == 'image/png') {
      processPng(record.data);
    };
  });
}

function processPng(data) {
  consoleLog("Known image/png data");

  var img = document.createElement("img");
  img.src = URL.createObjectURL(new Blob(data, 'image/png'));
  img.onload = function() {
    window.URL.revokeObjectURL(this.src);
  };
};

function processJSON(data) {
  var obj = JSON.parse(data);
  consoleLog("JSON data: " + obj.myProperty.toString());
};
